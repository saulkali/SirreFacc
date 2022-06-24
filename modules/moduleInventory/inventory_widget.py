#pyside6
from PySide6.QtWidgets import QWidget,QGridLayout

#helper
from helper import singleton

#modules
from modules.moduleDetailArticle.details_article_dialog import DetailsArticleDialog

#common
from common.widgets.cardArticleWidget.card_article_widget import CardArticle

#firebase
from common.database.firebase import articles

#gui
from .inventory_widget_gui import Ui_Form

from .signals.inventory_aux_widget import InventoryAuxWidget

@singleton
class InventoryWidget(QWidget,Ui_Form):
    
    listener:InventoryAuxWidget = InventoryAuxWidget()

    widgetRoot:QWidget
    recycleBox:QGridLayout
    listArticles:list = []

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setupQwidgets()
        self.setupButtons()
        self.setupListener()
    
    def setupListener(self):
        self.listener.reloadInventory.connect(self.setupQwidgets)
        
    def setupQwidgets(self):
        self.widgetRoot = QWidget(self)
        self.recycleBox = QGridLayout(self)
        self.recycleBox.setContentsMargins(6,6,6,6)

        self.widgetRoot.setLayout(self.recycleBox)
        self.scroll_area_articles.setWidget(self.widgetRoot)

        self.setListArticles()

    def setListArticles(self):
        row = 0
        column = 0
        sizeColumn = 3
        for article in articles.getAllArticles():
            cardArticle = CardArticle(self.listener,article,self)
            self.recycleBox.addWidget(cardArticle,row,column)
            self.listArticles.append(cardArticle)
            column += 1
            if column == sizeColumn:
                row += 1
                column = 0

    def setupButtons(self):
        self.button_open_add_article.clicked.connect(self.openAddArticleMenu)

    def openAddArticleMenu(self):
        add_article = DetailsArticleDialog(self.listener,self)
        add_article.exec()

    def getArticles(self):
        self.listArticles = articles.getAllArticles()