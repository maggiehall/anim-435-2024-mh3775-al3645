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
        file = QFile(r"C:\Users\maggi\OneDrive - Drexel University\Year3\fallWinter\techDirecting\anim-435-2024-mh3775-al3645\final\ui\final.ui" ) # Add your C:\path to your .UI file 
        
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, parentWidget=self)         
        file.close()

        # Connect buttons to methods
        self.ui.createGroup.clicked.connect(self.createGroup)
        #temorarily commenting these out until we finish ccode for them
        #self.ui.placeLocators.clicked.connect(self.placeLocators)
        #self.ui.buildRig.clicked.connect(self.buildRig)
     
    def createGroup(self):
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


# Instantiate and show the widget
myWidget = propRigWidget()      
myWidget.show()