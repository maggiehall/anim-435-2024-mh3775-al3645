import maya.cmds as cmds
import os

#def createGroup():
    
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


