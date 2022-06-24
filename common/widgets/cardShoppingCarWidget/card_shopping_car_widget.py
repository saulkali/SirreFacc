from PySide6.QtWidgets import QWidget
from common.entities.shopping_car_entity import ShoppingCardEntity
from .card_shopping_car_widget_gui import Ui_Form
from helper import loadImage
from modules.moduleMain.signals.main_aux_signal import MainAuxSignal

class CardShoppingCarWidget(QWidget,Ui_Form):

    shoppingCarEntity:ShoppingCardEntity
    listener:MainAuxSignal

    def __init__(self,shoppingCarEntity:ShoppingCardEntity, listener:MainAuxSignal ,parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self.shoppingCarEntity = shoppingCarEntity
        self.listener = listener

        self.loadShoppingCarEntity()
        self.setupButtons()
    
    def setupButtons(self):
        self.button_delete.clicked.connect(self.deleteThisWidget)
        
    def deleteThisWidget(self):
        self.listener.deleteItemShoppingCar.emit(self)
        
    def loadShoppingCarEntity(self):
        loadImage(self.label_photo,self.shoppingCarEntity.photoUrlArticle)
        self.label_code_bar.setText(self.shoppingCarEntity.idArticle)
        self.label_name.setText(self.shoppingCarEntity.nameArticle)
        self.label_amount.setText(self.shoppingCarEntity.amountArticle.__str__())
        self.label_price_unitary.setText(self.shoppingCarEntity.priceUniArticle.__str__())
        self.label_total_pay.setText(self.getTotal().__str__())
    
    def getTotal(self) -> float:
        return self.shoppingCarEntity.amountArticle * self.shoppingCarEntity.priceUniArticle