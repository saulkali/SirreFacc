#pyside6
from PySide6.QtWidgets import QWidget,QTableWidgetItem

#modules
from modules.moduleDetailEmploye.detail_employe_dialog import DetailsEmployeDialog

#firebase
from common.database.firebase import employes

#gui
from .employes_widget_gui import Ui_Form

class EmployeWidget(QWidget,Ui_Form):
    
    listEmployes:list = []
    
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.listEmployes = employes.getAllEmployes()


        self.setupButtons()
    
        self.setEmployesTable()

    def setEmployesTable(self):
        row = 0
        for employe in self.listEmployes:
            index = self.table_widget_employes.currentIndex().row()
            self.table_widget_employes.setRowCount(index + 1)
            self.table_widget_employes.setItem(row,0,QTableWidgetItem(employe.id))
            row += 1

    def setupButtons(self):
        self.button_add_employe.clicked.connect(lambda:DetailsEmployeDialog().exec())
        