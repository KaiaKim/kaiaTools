import importlib

import maya.cmds as mc
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets as qw

from kaiaTools import global_util as util
importlib.reload(util)
#-------------------------------------GLOBAL VARIABLE-----------------------------------------
trash_icon = QtGui.QIcon(':/trash.png')
refresh_icon = QtGui.QIcon(':/refresh.png')

bold_font = QtGui.QFont()
bold_font.setBold(True)

#-----------------------------------------CLASS-----------------------------------------------
class TransferSkinWindow(qw.QDialog):
    def __init__(self, parent=util.maya_main_window()):
        super().__init__(parent)
        
        ###
        self.setWindowTitle("Transfer Skin")
        self.setMinimumWidth(300)
        
        # Remove the ? from the dialog on Windows
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        
        # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
        # Then we create a QSettings for our tool. Qt stores this using your company name and your application name
        # This setting is then saved in the correct place for your user and their operating system
        # Qt takes care of that for you, so you don't need to worry about handling it on different operating systems etc..
        # Your company name can be just your name but should remain consistent between your tools.
        # Your tool name should however be unique to each tool or application you create.
        self.settings = QtCore.QSettings('KaiaTools', 'TransferSkin')
        
        # Then we look at our settings to see if there is a setting called geometry saved. Otherwise we default to an empty string
        geometry = self.settings.value('geometry', bytes('', 'utf-8'))
        
        # Then we call a Qt built in function called restoreGeometry that will restore whatever values we give it.
        # In this case we give it the values from the settings file.
        self.restoreGeometry(geometry)
        
    def create_widgets(self):
        t1 = "Transfer skinCluster to a different mesh."
        t2 = "Can be operated on multiple selections."
        self.discription = qw.QLabel( t1 + "\n" + t2 + "\n")
        
        self.copy_btn = qw.QPushButton("Copy")
        self.paste_btn = qw.QPushButton("Paste")
        self.inf_btn = qw.QPushButton("Select Influence")
        self.paste_btn.setEnabled(False)
        self.inf_btn.setEnabled(False)
        
        
        self.clipboard_lab = qw.QLabel("Clipboard")
        self.clipboard_lab.setFont(bold_font)
        self.clipboard_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_btn = qw.QPushButton("")
        self.empty_btn.setIcon(trash_icon)
        self.empty_btn.setFlat(True)

        self.refresh_btn = qw.QPushButton("")
        self.refresh_btn.setIcon(refresh_icon)
        self.refresh_btn.setFlat(True)
        
        self.clipboard_ls = qw.QListWidget()
    
    def create_layout(self):
        disc_layout = qw.QHBoxLayout()
        disc_layout.addWidget(self.discription)
        
        button_layout = qw.QHBoxLayout()
        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.paste_btn)
        button_layout.addWidget(self.inf_btn)
        
        clipboard_layout = qw.QHBoxLayout()
        clipboard_layout.addWidget(self.clipboard_lab)
        clipboard_layout.addStretch()
        clipboard_layout.addWidget(self.refresh_btn)
        clipboard_layout.addWidget(self.empty_btn)
        
        list_layout = qw.QVBoxLayout()
        list_layout.setSpacing(0)
        list_layout.addLayout(clipboard_layout)
        list_layout.addWidget(self.clipboard_ls)
        
        main_layout = qw.QVBoxLayout(self)
        main_layout.addLayout(disc_layout)
        main_layout.addLayout(clipboard_layout)
        main_layout.addLayout(list_layout)
        main_layout.addLayout(button_layout)

        
    def create_connections(self):    
        #self.but1.clicked.connect()
        for i in range(2):
            self.clipboard_ls.addItem('meshName' + ' > '+'skinCluster1')
            self.clipboard_ls.addItem('meshName' + ' > '+'skinCluster2')
            self.clipboard_ls.addItem('meshName' + ' > '+'skinCluster3')
            self.clipboard_ls.addItem('meshNameLong' + ' > '+'skinCluster1')
            self.clipboard_ls.addItem('meshNameLonger' + ' > '+'skinCluster1')
            self.clipboard_ls.addItem('meshNameLonger' + ' > '+'skinCluster2')
    
    
    def closeEvent(self,event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('geometry', geometry)
        '''
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(MyWindow, self).closeEvent(event)
        '''
###------------------EXECUTE-------------------------------
if __name__ == "__main__":
    try:
        test_dialog_1.close() # pylint: disable=E0601 # << removing the error message for this specific line
        test_dialog_1.deleteLater()

    except:
        pass

    test_dialog_1 = TransferSkinWindow()
    test_dialog_1.setWindowTitle("Transfer Skin : Test")
    test_dialog_1.show()

    
