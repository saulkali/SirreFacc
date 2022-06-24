#pyside6
from PySide6.QtWidgets import QWidget,QMessageBox,QGridLayout
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

#helper
from helper import singleton

#entities
from common.entities.article_entity import ArticleEntity
from common.entities.shopping_car_entity import ShoppingCardEntity

#gui
from .main_widget_gui import Ui_Form

#firebase database
from common.database.firebase import articles


#values
from common.values import strings

#widgets
from common.widgets.cardShoppingCarWidget.card_shopping_car_widget import CardShoppingCarWidget

#signals
from .signals.main_aux_signal import MainAuxSignal

@singleton
class MainWidget(QWidget,Ui_Form):
    
    listener:MainAuxSignal = MainAuxSignal()

    listArticleShopping:list = [] #cardShoppingcar
    recycleBoxShoppingCar: QGridLayout
    
    rowCounterShoppingCar:int = 0
    columnCounterShoppingCar:int = 0
    columnSizeShoppingCar:int = 4

    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.recycleBoxShoppingCar = QGridLayout(self)

        self.setupScrollArea()

        self.setupEditLine()
        self.setupMainAuxSignal()
        self.setupModeSystem()
    def setupModeSystem(self):
        self.label_mode_system.setText(strings.mode_system_shopping_car)
    
    def setupMainAuxSignal(self):
        self.listener.deleteItemShoppingCar.connect(self.deleteShoppingCar)
    

    def setupScrollArea(self):
        widget_root = QWidget(self)
        widget_root.setLayout(self.recycleBoxShoppingCar)
        self.scroll_area_shopping_car.setWidget(widget_root)
    
    def setupEditLine(self):
        self.input_code_bar.returnPressed.connect(lambda: self.searchArticle(self.input_code_bar.text()))

    def searchArticle(self,codeBar):
        article = articles.getArticleById(codeBar)
        if article == None:
            QMessageBox.warning(self,strings.msg_error,strings.msg_article_not_found)
        else:
            self.createShoppingEntity(article)
        self.input_code_bar.clear()
    
    def createShoppingEntity(self,article:ArticleEntity):
        shoppingEntity = ShoppingCardEntity(
            idArticle = article.id,
            nameArticle = article.name,
            photoUrlArticle = article.photoUrl,
            amountArticle = article.amount,
            priceUniArticle = article.price
        )
        cardShoppingCarWidget = CardShoppingCarWidget(shoppingEntity,self.listener,self)
        self.listArticleShopping.append(cardShoppingCarWidget)
        self.addArticleShoppingCard(cardShoppingCarWidget)

    def addArticleShoppingCard(self,cardShoppingCar:ArticleEntity):
        self.recycleBoxShoppingCar.addWidget(cardShoppingCar,self.rowCounterShoppingCar,self.columnCounterShoppingCar)
        self.columnCounterShoppingCar += 1
        if self.columnCounterShoppingCar == self.columnSizeShoppingCar:
            self.columnCounterShoppingCar = 0
            self.rowCounterShoppingCar +=1

        self.refreshTotal()

    def refreshTotal(self):
        total = 0
        
        for article in self.listArticleShopping:
            print(article.getTotal())
            total = total + article.getTotal()
        self.lcd_number_total.display(total)
    
    def keyPressEvent(self, event:QKeyEvent) -> None:
        key = event.key()

        match key:
            case Qt.Key_Escape:
                self.label_mode_system.setText(strings.mode_system_shopping_car)
            case Qt.Key_F1:
                self.label_mode_system.setText(strings.mode_system_pay_efective)
        

        return super().keyPressEvent(event)
    
    ######################
    ##  MAIN AUX SIGNAL ##
    ######################
    def deleteShoppingCar(self,shoppingCarEntity:CardShoppingCarWidget):
        msg_result = QMessageBox.warning(self,strings.msg_delete,strings.msg_delete_ask,QMessageBox.Yes|QMessageBox.No)
        if msg_result == QMessageBox.Yes:
            self.listArticleShopping.remove(shoppingCarEntity)
            shoppingCarEntity.close()
            self.refreshTotal()