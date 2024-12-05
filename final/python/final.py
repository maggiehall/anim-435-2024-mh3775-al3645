#final project
#prop rig

#import required methods
import maya.cmds as cmds
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

myWidget = propRigWidget()      
myWidget.show()