#pyside6
from PySide6.QtWidgets import QWidget,QMessageBox,QGridLayout
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

#helper
from helper import singleton

#entities
from common.entities.article_entity import ArticleEntity
from common.entities.shopping_car_entity import ShoppingCardEntity
from common.entities.sale_entity import SaleEntity

#gui
from .main_widget_gui import Ui_Form

#firebase database
from common.database.firebase import articles
from common.database.firebase import sales

#values
from common.values import strings
from common.values import integers

#widgets
from common.widgets.cardShoppingCarWidget.card_shopping_car_widget import CardShoppingCarWidget

#signals
from .signals.main_aux_signal import MainAuxSignal

@singleton
class MainWidget(QWidget,Ui_Form):
    
    listener:MainAuxSignal = MainAuxSignal()
    modeSystem:str = strings.mode_system_shopping_car # mode system shopping card operations

    listArticleShopping:list = [] #cardShoppingcar
    recycleBoxShoppingCar: QGridLayout

    totalPayDigit:str = ""
    
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
        self.listener.refreshTotal.connect(self.refreshTotal)
    

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
            amountArticle = 1.0,
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

        self.lcd_number_change.display(0)
        self.lcd_number_payment.display(0)
        self.refreshTotal()
    

    def refreshTotal(self):
        total = 0
        for article in self.listArticleShopping:
            print(article.getTotal())
            total = total + article.getTotal()
        self.lcd_number_total.display(total)
    

    def setModeSystem(self,mode:str):
        if mode.__eq__(strings.mode_system_pay_efective):
            self.modeSystem = strings.mode_system_pay_efective
            self.label_mode_system.setText(strings.mode_system_pay_efective)
            self.input_code_bar.setEnabled(False)
        elif mode.__eq__(strings.mode_system_shopping_car):
            self.modeSystem = strings.mode_system_shopping_car
            self.label_mode_system.setText(strings.mode_system_shopping_car)
            self.input_code_bar.setEnabled(True)
            self.input_code_bar.setFocus()
        else:
            QMessageBox.warning(self,strings.msg_error,strings.msg_mode_system_not_found)

    def setDigitTotalPay(self,digit:str):
        if self.totalPayDigit.__len__() < integers.size_lcb_numer_pay_total:
            self.totalPayDigit += digit
            if self.totalPayDigit.__len__() == 0:
                self.lcd_number_efective_pay.display(0)
            else:
                self.lcd_number_efective_pay.display(float(self.totalPayDigit))
    
    def deleteDigit(self):
        self.totalPayDigit = self.totalPayDigit[0:self.totalPayDigit.__len__()-1]
        if self.totalPayDigit.__len__() == 0:
            self.lcd_number_efective_pay.display(0)
        else:
            self.lcd_number_efective_pay.display(float(self.totalPayDigit))
    

    def closeShoppingCard(self):
        listShoppingCard = []

        for item in self.listArticleShopping:
            articles.deleteAmountArticle(item.shoppingCarEntity.idArticle,item.shoppingCarEntity.amountArticle)
            self.recycleBoxShoppingCar.removeWidget(item)
            listShoppingCard.append(item.shoppingCarEntity)
            item.close()
        self.listArticleShopping.clear()
        self.saveSale(listShoppingCard)
        self.setDisplayLcdSale()

        self.resetValueShoppingCard()
        self.reloadShoppingCardItems()
        self.setModeSystem(strings.mode_system_shopping_car)
    
    def saveSale(self,listShoppingCard:list):
        sale = SaleEntity(listArticle = listShoppingCard)
        sales.saveSale(sale)

    def resetValueShoppingCard(self):
        self.totalPayDigit = ""
        self.columnCounterShoppingCar = 0
        self.rowCounterShoppingCar = 0
        self.lcd_number_efective_pay.display(0)
        

    def setDisplayLcdSale(self):
        self.lcd_number_payment.display(float(self.totalPayDigit))
        change = self.lcd_number_payment.value() - self.lcd_number_total.value()
        self.lcd_number_change.display(change)

    def verifyPay(self):
        if float(self.totalPayDigit) < self.lcd_number_total.value():
            QMessageBox.warning(self,"monto menor","el monto es menor que el total de venta")
        else:
            self.closeShoppingCard()

    def keyPressEvent(self, event:QKeyEvent) -> None:
        key = event.key()
        match key:
            case Qt.Key_Escape:
                self.setModeSystem(strings.mode_system_shopping_car)
            case Qt.Key_F1:
                self.setModeSystem(strings.mode_system_pay_efective)
            case _:
                if self.modeSystem == strings.mode_system_pay_efective:
                    match key:
                        case Qt.Key_Space:
                            self.verifyPay()
                        case Qt.Key_0:
                            self.setDigitTotalPay("0")
                        case Qt.Key_1:
                            self.setDigitTotalPay("1")
                        case Qt.Key_2:
                            self.setDigitTotalPay("2")
                        case Qt.Key_3:
                            self.setDigitTotalPay("3")
                        case Qt.Key_4:
                            self.setDigitTotalPay("4")
                        case Qt.Key_5:
                            self.setDigitTotalPay("5")
                        case Qt.Key_6:
                            self.setDigitTotalPay("6")
                        case Qt.Key_7:
                            self.setDigitTotalPay("7")
                        case Qt.Key_8:
                            self.setDigitTotalPay("8")
                        case Qt.Key_9:
                            self.setDigitTotalPay("9")
                        case Qt.Key_Delete:
                            self.deleteDigit()
                        case Qt.Key_Backspace:
                            self.deleteDigit()
                        case Qt.Key_cent:
                            print(".")
        return super().keyPressEvent(event)
    
    def reloadShoppingCardItems(self):
        row = 0
        column = 0
        for widget in self.listArticleShopping:
            if column == self.columnSizeShoppingCar:
                column = 0
                row +=1
            column += 1
            self.recycleBoxShoppingCar.addWidget(widget,row,column)
        self.refreshTotal()

    ######################
    ##  MAIN AUX SIGNAL ##
    ######################
    def deleteShoppingCar(self,shoppingCarEntity:CardShoppingCarWidget):
        msg_result = QMessageBox.warning(self,strings.msg_delete,strings.msg_delete_ask,QMessageBox.Yes|QMessageBox.No)
        if msg_result == QMessageBox.Yes:
            self.listArticleShopping.remove(shoppingCarEntity)
            self.recycleBoxShoppingCar.removeWidget(shoppingCarEntity)
            shoppingCarEntity.close()
            self.resetValueShoppingCard()
            self.reloadShoppingCardItems()
            