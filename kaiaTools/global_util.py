import sys, os
from shiboken2 import wrapInstance

import maya.cmds as mc
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets as qw

#-------------------------------------FUNCTION-----------------------------------------
def maya_main_window():
    """Return the Maya main window widget as a Python object"""
    main_window_ptr = omui.MQtUtil.mainWindow()
    
    if sys.version_info.major >= 3: # Python 3 or higher
        return wrapInstance(int(main_window_ptr), qw.QMainWindow)
    else:
        return wrapInstance(long(main_window_ptr), qw.QMainWindow)

def get_directory():
    #get the parent directory for relative import
    return sys.path[-1]

def add_scripts_to_menu():
    mainDir = get_directory()
    scriptDir = mainDir + '/kaiaTools/extra_scripts'
    file_ls = os.listdir(scriptDir)
    #iterator
    #import python files from the directory .extra_scripts
    #get each file names
    #add them to the menu
    #connect the button to execute the script
    pass
    
###------------------EXECUTE-------------------------------
if __name__ == "__main__":
    pass