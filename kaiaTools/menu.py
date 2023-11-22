import importlib
from functools import partial

import maya.cmds as mc
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets as qw

from kaiaTools import global_util as util
importlib.reload(util)

from kaiaTools.transferSkin import ui as tscUI
importlib.reload(tscUI)

from kaiaTools.copyWeights import ui as cdwUI
importlib.reload(cdwUI)

#-----------------------------------------CLASS-----------------------------------------------
class KaiaToolsMenu(qw.QMenu):
    def __init__(self, parent=util.maya_main_window()):
        super().__init__("Kaia_Tools",parent)
        
        #self.actionList = []
        
        toolList = [
                    tscUI.TransferSkinWindow(),
                    cdwUI.CopyWeightsWindow()
                    ]
        self.add_tools_to_menu(toolList)

        scriptList = []
        self.add_scripts_to_menu(scriptList)
        
        mainWindow = util.maya_main_window()
        menuBar = mainWindow.menuBar()
        menuBar.addMenu(self)
    
    def add_tools_to_menu(self, tools):
        '''
        self.addAction(tools[0].windowTitle(), lambda: self.tool_clicked(tools[0]))
        self.addAction(tools[1].windowTitle(), lambda: self.tool_clicked(tools[1]))
        '''
        for t in tools:
            ac = self.addAction(t.windowTitle(), partial(self.tool_clicked, t))
            #self.actionList.append(ac)
            # ^return type: QActiong
            #break

    def add_scripts_to_menu(self, scripts):
        pass
        
    def tool_clicked(self,toolWindow):
        toolWindow.close()
        toolWindow.show()
        
    def script_clicked(self):
        pass

    

