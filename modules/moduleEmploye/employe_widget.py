#pyside6
from PySide6.QtWidgets import QWidget,QTableWidgetItem,QVBoxLayout

#modules
from modules.moduleDetailEmploye.detail_employe_dialog import DetailsEmployeDialog

#firebase
from common.database.firebase import employes

from common.widgets.cardEmployeWidget.card_employe_widget import CardEmployeWidget

#gui
from .employes_widget_gui import Ui_Form
from .signals.employe_aux_widget import EmployeAuxWidget

class EmployeWidget(QWidget,Ui_Form):
    listener: EmployeAuxWidget
    listCardEmployes:list = []
    recycleEmployes:QVBoxLayout
    widgetRecycleRoot:QWidget

    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setupListener()
        self.getEmployes()
        self.setupButtons()
    
    def setupListener(self):
        self.listener = EmployeAuxWidget(self)
        self.listener.reloadListEmployes.connect(self.getEmployes)

    def setupQWidget(self):
        self.recycleEmployes = QVBoxLayout(self)
        self.widgetRecycleRoot = QWidget(self)
        self.widgetRecycleRoot.setLayout(self.recycleEmployes)
        self.scroll_area_employes.setWidget(self.widgetRecycleRoot)

    def getEmployes(self):
        self.listCardEmployes.clear()
        listEmployes = employes.getAllEmployes()
        for employe in listEmployes:
            cardEmploye = CardEmployeWidget(self,employe,self.listener)
            self.listCardEmployes.append(cardEmploye)
        self.setCardEmployesList(self.listCardEmployes)

    def setCardEmployesList(self,listCardEmployes:list):
        self.setupQWidget()
        for cardEmploye in listCardEmployes:
            self.recycleEmployes.addWidget(cardEmploye)

    def setupButtons(self):
        self.button_add_employe.clicked.connect(lambda:DetailsEmployeDialog(self.listener,self).exec())
        