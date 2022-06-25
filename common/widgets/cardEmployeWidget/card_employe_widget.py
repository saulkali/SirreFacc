from PySide6.QtWidgets import QWidget,QMessageBox

#gui
from .card_employe_widget_gui import Ui_Form

#entites
from common.entities.employe_entity import EmployeEntity

#helper
from helper import loadImage

#modules
from modules.moduleEmploye.signals.employe_aux_widget import EmployeAuxWidget
from modules.moduleDetailEmploye.detail_employe_dialog import DetailsEmployeDialog
#firebase
from common.database.firebase import employes

#values
from common.values import strings

class CardEmployeWidget(QWidget,Ui_Form):
    listener:EmployeAuxWidget
    employeEntity:EmployeEntity

    def __init__(self, parent,employeEntity:EmployeEntity,listener:EmployeAuxWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.employeEntity = employeEntity
        self.listener = listener

        self.setEmployeEntity()

        self.setupButtons()
    
    def setupButtons(self):
        self.button_delete.clicked.connect(self.deleteArticle)
    
    def deleteArticle(self):
        msg = QMessageBox.warning(self,strings.msg_delete,strings.msg_delete_ask,QMessageBox.Yes|QMessageBox.No)
        if msg == QMessageBox.Yes:
            employes.deleteEmploye(self.employeEntity)
            self.listener.reloadListEmployes.emit()
            self.close()

    def setEmployeEntity(self):
        self.label_name_employe.setText(f"{self.employeEntity.firstName} {self.employeEntity.lastName}")
        self.label_rfc.setText(self.employeEntity.rfc)
        self.label_phone.setText(self.employeEntity.phone)
        self.label_email.setText(self.employeEntity.email)
        loadImage(self.label,self.employeEntity.photoUrl)
    
    def openDetailsEmploye(self):
        DetailsEmployeDialog(self.listener,self,self.employeEntity).exec()
    def mousePressEvent(self, event) -> None:
        self.openDetailsEmploye()
        return super().mousePressEvent(event)