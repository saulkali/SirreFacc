from PySide6.QtWidgets import QApplication
from modules.moduleRoot.root_window import RootWindow
import sys

__version__ = "1.0.0.0"

DEBUG = True

def production():
    pass

def debug():
    app = QApplication(sys.argv)
    root_window = RootWindow()
    root_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    if DEBUG:
        debug()
    else:
        production()