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

#printer
from common.utils.printer import PrinterEscPos as Printer

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
        self.lcd_number_efective_pay.setDigitCount(8)
        self.setupScrollArea()
        self.setupButtons()
        self.setupEditLine()
        self.setupMainAuxSignal()
        self.setupModeSystem()

    def setupButtons(self):
        self.button_reset_shopping_car.setEnabled(False)
        self.button_reset_shopping_car.clicked.connect(self.clearShoppingCar)
        self.button_open_cash_drawing.clicked.connect(lambda: Printer().openCashDrawing())

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

    def searchArticle(self,codeBar:str):
        if codeBar.__len__() == 0:
            QMessageBox.warning(self,strings.msg_error,strings.msg_code_bar_search_is_empty)
        else:
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
        
        if total > 0:
            self.button_reset_shopping_car.setEnabled(True)
        else:
            self.button_reset_shopping_car.setEnabled(False)

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
        if self.totalPayDigit.__len__() > 0:
            if self.totalPayDigit[-1] == ".":
                if digit == "0":
                    return
        if self.totalPayDigit.__len__() < integers.size_lcb_numer_pay_total:
            self.totalPayDigit += digit
            if self.totalPayDigit.__len__() == 0:
                self.lcd_number_efective_pay.display(0)
            else:
                self.totalPayDigit.lstrip("0")
                self.lcd_number_efective_pay.display(float(self.totalPayDigit.format()))
    
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
        sale = SaleEntity(
            listArticle = listShoppingCard,
            payClient = self.lcd_number_change.value(),
            changeClient = self.lcd_number_change.value()
        )
        sales.saveSale(sale)
        resultPrintTicket = QMessageBox.warning(self,strings.msg_await,strings.msg_ask_print_ticket_sale,QMessageBox.Yes|QMessageBox.No)
        if resultPrintTicket == QMessageBox.Yes:
            Printer().printSale(sale)

    def resetValueShoppingCard(self):
        self.totalPayDigit = ""
        self.columnCounterShoppingCar = 0
        self.rowCounterShoppingCar = 0
        self.lcd_number_efective_pay.display(0)
    
    def clearShoppingCar(self):
        msg = QMessageBox().warning(self,strings.msg_await,strings.msg_ask_clear_shopping_car,QMessageBox.Yes|QMessageBox.No)
        if msg == QMessageBox.Yes:
            for article in self.listArticleShopping:
                article.close()
            self.listArticleShopping.clear()
            self.resetValueShoppingCard()
            self.refreshTotal()
            self.setModeSystem(strings.mode_system_shopping_car)

    def setDisplayLcdSale(self):
        self.lcd_number_payment.display(float(self.totalPayDigit))
        change = self.lcd_number_payment.value() - self.lcd_number_total.value()
        self.lcd_number_change.display(change)

    def verifyPay(self):
        if float(self.totalPayDigit) < self.lcd_number_total.value():
            QMessageBox.warning(self,"monto menor","el monto es menor que el total de venta")
        else:
            self.closeShoppingCard()
    
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

    def keyPressEvent(self, event:QKeyEvent) -> None:
        key = event.key()
        match key:
            case Qt.Key_Escape:
                self.setModeSystem(strings.mode_system_shopping_car)
            case Qt.Key_F1:
                if self.listArticleShopping.__len__() == 0:
                    QMessageBox.warning(self,strings.msg_error,strings.msg_shopping_car_is_empty)
                else:
                    self.setModeSystem(strings.mode_system_pay_efective)
            case _:
                if self.modeSystem == strings.mode_system_pay_efective:
                    match key:
                        case Qt.Key_Space:
                            self.verifyPay()
                        case Qt.Key_Period:
                            if "." not in self.totalPayDigit:
                                self.setDigitTotalPay(".")
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
            