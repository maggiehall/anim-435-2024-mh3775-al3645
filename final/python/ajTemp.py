import maya.cmds as cmds
import os

#GROUPING FUNCTION  
#Take selection and create selectedObject variable
selectedObject = cmds.ls(sl=1)
if selectedObject == False:
    print('No object is selected. Script Ended.')

#Get asset name from environmental variable
assetName = os.getenv('ASSET')
#If environmental name is not found the name is defaulted.
if assetName == True:
    print('Yes')
else:
    print('Asset Name not found. Name is defaulted.')
    assetName = 'default'

#Create Groups
cmds.group(selectedObject, name='GRP_geom')
cmds.group(em=True, name='GRP_rig')
cmds.group('GRP_geom','GRP_rig', name=assetName)

#LOCATOR MODULE
if not cmds.objExists('LOC_root') and not cmds.objExists('LOC_base') and not cmds.objExists('LOC_move'):
    #Creates locators
    locRoot = cmds.spaceLocator(name='LOC_root')
    locBase = cmds.spaceLocator(name='LOC_base')
    locMove = cmds.spaceLocator(name='LOC_move')
    #Creates labels
    labelRoot = cmds.annotate(locRoot, text="LOC_root")
    labelBase = cmds.annotate(locBase, text="LOC_base")
    labelMove = cmds.annotate(locMove, text="LOC_move")
    #Groups labels together
    cmds.group(labelRoot, labelBase, labelMove, name='LOC_label_grp')
    #Parents labels to locators
    cmds.parent(labelRoot, locRoot, relative=True, shape=True)
    cmds.parent(labelBase, locBase, relative=True, shape=True)
    cmds.parent(labelMove, locMove, relative=True, shape=True)
    #Moves locators for readability
    cmds.xform(locRoot, worldSpace=True, translation=(-2,0,0))
    cmds.xform(locMove, worldSpace=True, translation=(2,0,0))
else:
    print('ERROR: Rigging Locators already exist.')


