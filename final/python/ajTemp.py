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

locRoot = cmds.spaceLocator(name='LOC_root',position=(0,0,0))
locBase = cmds.spaceLocator(name='LOC_base',position=(0,0,0))
locMove = cmds.spaceLocator(name='LOC_move',position=(0,0,0))



labelRoot = cmds.annotate(locRoot, text="LOC_root", point=(-2,0,0))
labelBase = cmds.annotate(locBase, text="LOC_base", point=(0,0,0))
labelMove = cmds.annotate(locMove, text="LOC_move", point=(2,0,0))

cmds.parent(labelRoot, locRoot, relative=True)
cmds.parent(labelBase, locBase, relative=True)
cmds.parent(labelMove, locMove, relative=True)
