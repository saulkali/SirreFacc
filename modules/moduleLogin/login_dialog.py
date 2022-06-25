from PySide6.QtWidgets import QDialog,QMessageBox

from .login_dialog_gui import Ui_Dialog

from common.database.firebase import employes
from common.values import strings
from modules.moduleRoot.root_window import RootWindow

class LoginDialog(QDialog,Ui_Dialog):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.getEmployes()
        self.setupButtons()
    
    def setupButtons(self):
        self.button_login.clicked.connect(lambda: self.login(self.combo_box_email.currentText(),self.input_password.text()))

    def getEmployes(self):
        listEmailEmployes = []
        listEmployes = employes.getAllEmployes()
        for employe in listEmployes:
            listEmailEmployes.append(employe.email)
        self.combo_box_email.addItems(listEmailEmployes)
    
    def login(self,email:str,password:str):
        if employes.loginEmploye(email,password):
            root_window = RootWindow()
            root_window.show()
            self.close()
        else:
            QMessageBox.warning(self,strings.msg_error,strings.msg_employe_not_eq_password)
        self.input_password.clear()