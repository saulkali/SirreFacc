#pyside6
from PySide6.QtWidgets import QDialog,QMessageBox

#pydantic
from pydantic import ValidationError

#values
from common.values import strings

#gui
from .details_employe_dialog_gui import Ui_Dialog

#entities
from common.entities.employe_entity import EmployeEntity

from modules.moduleEmploye.signals.employe_aux_widget import EmployeAuxWidget

#firebase
from common.database.firebase import employes

class DetailsEmployeDialog(QDialog,Ui_Dialog):

    isEdit:bool = False
    listener:EmployeAuxWidget
    employeEntity:EmployeEntity

    def __init__(self, listener:EmployeAuxWidget,parent = None,employeEntity:EmployeEntity = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.listener = listener
        self.employeEntity = employeEntity

        self.setWindowTitle(strings.title_create_employe)
        if self.employeEntity is not None:
            self.isEdit = True
            self.loadEmploye()
            self.setWindowTitle(strings.title_edit_employe)
        self.setupButtons()
    
    def loadEmploye(self):
        self.input_photo_url.setText(self.employeEntity.photoUrl)
        self.input_first_name.setText(self.employeEntity.firstName)
        self.input_last_name.setText(self.employeEntity.lastName)
        self.input_password.setText(self.employeEntity.password)
        self.input_confirm_password.setText(self.employeEntity.password)
        self.input_phone.setText(self.employeEntity.phone)
        self.input_address.setText(self.employeEntity.address)
        self.input_email.setText(self.employeEntity.email)
        self.input_rfc.setText(self.employeEntity.rfc)

    def setupButtons(self):
        self.button_accept.clicked.connect(self.validateEmploye)
    
    def validateEmploye(self):
        try:
            employe = EmployeEntity(
                photoUrl = self.input_photo_url.text(),
                firstName = self.input_first_name.text(),
                lastName = self.input_last_name.text(),
                password = self.input_password.text(),
                phone = self.input_phone.text(),
                address = self.input_address.text(),
                cp = self.spin_box_cp.value(),
                email = self.input_email.text(),
                rfc = self.input_rfc.text(),
                permissions = self.combo_box_permissions.currentIndex()
            )
            if self.isEdit:
                employe.id = self.employeEntity.id
                employes.updateEmploye(employe)
            else:
                employes.saveEmploye(employe)
            self.clearFields()
            self.listener.reloadListEmployes.emit()
        except ValidationError as error:
            QMessageBox.warning(self,strings.msg_error,error.errors().__str__())
    
    def clearFields(self):
        self.input_photo_url.setText(""),
        self.input_first_name.setText(""),
        self.input_last_name.setText(""),
        self.input_password.setText(""),
        self.input_phone.setText(""),
        self.input_address.setText(""),
        self.spin_box_cp.setValue(0),
        self.input_email.setText(""),
        self.input_rfc.setText(""),
        self.combo_box_permissions.setCurrentIndex(0)