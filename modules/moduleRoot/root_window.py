from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout
from PySide6.QtCore import Qt

#widgets windows
from modules.moduleMain.main_widget import MainWidget
from modules.moduleInventory.inventory_widget import InventoryWidget
from modules.moduleEmploye.employe_widget import EmployeWidget
from .root_window_gui import Ui_MainWindow

class RootWindow(QMainWindow,Ui_MainWindow):

    widget_active:QWidget = None
    box_root:QVBoxLayout = QVBoxLayout()
    widget_root:QWidget

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        

        self.setup_widget_root()
        self.setup_buttons()
    
    def setup_widget_root(self):
        self.widget_root = QWidget(self)
        self.widget_root.setLayout(self.box_root)
        self.setCentralWidget(self.widget_root)
        

    def setup_buttons(self):
        #root widget
        main_widget = MainWidget()
        
        #inventory widget
        inventory_widget = InventoryWidget()
        inventory_widget.hide()
        
        #employe widget
        employe_widget = EmployeWidget()
        employe_widget.hide()

        self.widget_active = main_widget
        
        self.box_root.addWidget(main_widget)

        self.button_open_inventory.clicked.connect(lambda:self.show_widget(self.widget_active,inventory_widget))
        self.button_open_shopping_card.clicked.connect(lambda:self.show_widget(self.widget_active,main_widget))
        self.button_open_employes.clicked.connect(lambda:self.show_widget(self.widget_active,employe_widget))
    
    def show_widget(self,oldWidget:QWidget,newWidget:QWidget):
        self.widget_active = newWidget
        oldWidget.hide()
        newWidget.show()
        self.box_root.addWidget(newWidget)
    
    def showDockWidget(self):
        if self.dock_widget_control.isHidden():
            self.dock_widget_control.show()
        else:
            self.dock_widget_control.hide()
            
    def keyPressEvent(self, event) -> None:
        key = event.key()
        match key:
            case Qt.Key_F10:
                self.showDockWidget()
            case _:
                return super().keyPressEvent(event)