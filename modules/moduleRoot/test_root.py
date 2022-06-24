from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .root_window import RootWindow

from modules.moduleEmploye.employe_widget import EmployeWidget


def testInitRootWidget(qtbot):
    root_widget = RootWindow()
    assert root_widget != None

def testDockSelection(qtbot):
    root_widget = RootWindow()
    #clicked employes
    qtbot.mouseClick(root_widget.button_open_employes,Qt.LeftButton)
    assert type(root_widget.centralWidget()) is QWidget
    #clicked shopping card
    qtbot.mouseClick(root_widget.button_open_shopping_card,Qt.LeftButton)
    assert type(root_widget.centralWidget()) is QWidget
    #clicked inventory
    qtbot.mouseClick(root_widget.button_open_inventory,Qt.LeftButton)
    assert type(root_widget.centralWidget()) is QWidget
    
