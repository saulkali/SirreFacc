from PySide6.QtWidgets import QApplication
from modules.moduleLogin.login_dialog import LoginDialog
import sys

__version__ = "1.0.0.0"

DEBUG = True

def production():
    pass

def debug():
    app = QApplication(sys.argv)
    loginDialog = LoginDialog()
    loginDialog.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    if DEBUG:
        debug()
    else:
        production()