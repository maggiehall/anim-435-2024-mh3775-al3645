#final project
#prop rig

#TO PROPERLY USE THIS
    # define environement variable ASSET
        # in gitbash use: export ASSET="yournamehere"
    #open maya after defining environment variable in gitbash
        #open maya:   /c/Program\ Files/Autodesk/Maya2025/bin/maya.exe


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
        #COMMENT OUT FILE PATHS!
        file = QFile(r"C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\anim-435-2024-mh3775-al3645\final\ui\final.ui" ) # Add your C:\path to your .UI file 
        #file = QFile(r"C:\Users\ajluc\OneDrive - Drexel University\Year 3\Fall 2024\ANIM435- Pipeline Direction for Animation\anim-435-2024-al3645\final\anim-435-2024-mh3775-al3645\final\ui\final.ui")
        
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
        #Take selection and create selectedObject variable
        selectedObject = cmds.ls(sl=1)
        if selectedObject == False:
            print('No object is selected. Script Ended.')
            exit()
        #Create Groups
        cmds.group(selectedObject, name='GRP_geom')
        cmds.group(em=True, name='GRP_rig')
        cmds.group('GRP_geom','GRP_rig', name=groupName)
        
    def placeLocators(self):
        #LOCATOR MODULE
        #Test if locators already exist
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


# Instantiate and show the widget
myWidget = propRigWidget()      
myWidget.show()