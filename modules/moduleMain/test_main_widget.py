from PySide6.QtCore import Qt

from .main_widget import MainWidget

from common.values import strings

from pytestqt.qtbot import QtBot


def testInitMainWidget(qtbot):
    mainWidget = MainWidget()
    assert mainWidget != None

def testSearchArticle(qtbot:QtBot):
    mainWidget = MainWidget()
    mainWidget.input_code_bar.setText("123")
    assert mainWidget.input_code_bar.text() == "123"
    qtbot.keyPress(mainWidget.input_code_bar,Qt.Key_Enter)
    assert mainWidget.input_code_bar.text() == ""

def testModeSystemKeyEvent(qtbot:QtBot):
    mainWidget = MainWidget()
    #mode shopping car
    qtbot.keyPress(mainWidget,Qt.Key_Escape)
    assert mainWidget.label_mode_system.text() == strings.mode_system_shopping_car

    #mode pay efective
    qtbot.keyPress(mainWidget,Qt.Key_F1)
    assert mainWidget.label_mode_system.text() == strings.mode_system_pay_efective
    
    
