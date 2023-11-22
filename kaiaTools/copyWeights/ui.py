import importlib

import maya.cmds as mc
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets as qw

from kaiaTools import global_util as util
importlib.reload(util)

#-----------------------------------------CLASS-----------------------------------------------
class CopyWeightsWindow(qw.QDialog):
    def __init__(self, parent=util.maya_main_window()):
        super().__init__(parent)
        
        ###        
        self.setWindowTitle("Copy Deformer Weights")
        self.setMinimumWidth(300)
        
        # Remove the ? from the dialog on Windows
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
        self.settings = QtCore.QSettings('KaiaTools', 'CopyWeights')
        geometry = self.settings.value('geometry', bytes('', 'utf-8'))

        self.restoreGeometry(geometry)
    
    def create_widgets(self):
        t1 = "Transfer a single weight across \nskinCluster, blendShape, nCloth, deformers."
        t2 = "Select an influence inside any Paint Tool."
        self.discription = qw.QLabel( t1 + "\n" + t2 + "\n")
        self.timer_lb = qw.QLabel("timer:")
        
        self.copy_btn = qw.QPushButton("Copy")
        self.paste_btn = qw.QPushButton("Paste")
        self.paste_btn.setEnabled(False)
        
        self.replace_rb = qw.QRadioButton("Replace")
        self.add_rb = qw.QRadioButton("Add")
        self.subtract_rb = qw.QRadioButton("Subtract")
        self.scale_rb = qw.QRadioButton("Scale")
        self.replace_rb.setChecked(True)
        
    
    def create_layout(self):
        disc_layout = qw.QHBoxLayout()
        disc_layout.addWidget(self.discription)
        
        option_layout = qw.QHBoxLayout()
        option_layout.addWidget(self.replace_rb)
        option_layout.addWidget(self.add_rb)
        option_layout.addWidget(self.subtract_rb)
        option_layout.addWidget(self.scale_rb)
        
        button_layout = qw.QHBoxLayout()
        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.paste_btn)
        

        main_layout = qw.QVBoxLayout(self)
        main_layout.addLayout(disc_layout)
        main_layout.addLayout(option_layout)
        main_layout.addLayout(button_layout)

        
    
    def create_connections(self):    
        #but1.clicked.connect()
        pass
        
    def closeEvent(self,event):
        geometry = self.saveGeometry()
        self.settings.setValue('geometry', geometry)

        
###------------------EXECUTE-------------------------------
if __name__ == "__main__":
    try:
        test_dialog_2.close() # pylint: disable=E0601 # << removing the error message for this specific line
        test_dialog_2.deleteLater()
    except:
        pass

    test_dialog_2 = CopyWeightsWindow()
    test_dialog_2.setWindowTitle("Copy Deformer Weights : Test")
    test_dialog_2.show()
