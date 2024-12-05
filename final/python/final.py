#final project
#prop rig
#TO PROPERLY USE THIS
    # define environement variable ASSET
    #open maya after defining environment variable in gitbash


#import required methods
import maya.cmds as cmds
import os
from maya import OpenMayaUI as omui  
from PySide6.QtCore import *  
from PySide6.QtGui import *  
from PySide6.QtWidgets import * 
from PySide6.QtUiTools import * 
from shiboken6 import wrapInstance

#get maya main window
mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

# define the widget
class propRigWidget(QWidget):     
    def __init__(self, *args, **kwargs):         
        super(propRigWidget, self).__init__(*args, **kwargs) 
         
        #Parent widget under Maya main window         
        self.setParent(mayaMainWindow)         
        self.setWindowFlags(Qt.Window)    
         
        #Set the object name      
        self.setWindowTitle('Prop Rig Widget')         
        self.setGeometry(250, 250, 425, 250)      # Change your window size here 
         
        self.initUI()   
          
    def initUI(self):         
        loader = QUiLoader()               
        file = QFile(r"C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\anim-435-2024-mh3775-al3645\final\ui\final.ui" ) # Add your C:\path to your .UI file 
        
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, parentWidget=self)         
        file.close()

        # Connect buttons to methods
        self.ui.createGroup.clicked.connect(self.createGroup)
        self.ui.placeLocators.clicked.connect(self.placeLocators)
        self.ui.buildRig.clicked.connect(self.buildRig)
     
    def createGroup(self):
        # Retrieve asset name from the environment variable
        assetName = os.getenv("ASSET", "defaultAsset")  # Fallback to "defaultAsset" if ASSET is not set
        groupName = f"GRP_{assetName}"
       
        # Create the group hierarchy in Maya
        if not cmds.objExists(groupName):
            parentGroup = cmds.group(em=True, name=groupName)
            cmds.group(em=True, name=f"{groupName}_geom", parent=parentGroup)
            cmds.group(em=True, name=f"{groupName}_rig", parent=parentGroup)
            cmds.warning(f"Group hierarchy created for asset: {assetName}")
        else:
            cmds.warning(f"Group hierarchy already exists for asset: {assetName}")

# Instantiate and show the widget
myWidget = propRigWidget()      
myWidget.show()