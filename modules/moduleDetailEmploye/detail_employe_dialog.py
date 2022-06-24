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

#firebase
from common.database.firebase import employes

class DetailsEmployeDialog(QDialog,Ui_Dialog):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setupButtons()
        

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
            employes.saveEmploye(employe)
            self.clearFields()
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