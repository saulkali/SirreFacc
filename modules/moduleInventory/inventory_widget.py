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
        
        self.setupButtons()
        self.setupEditlines()
        self.setupListener()
        self.setupQwidgets()

        self.getAllArticles()

       
    
    def setupEditlines(self):
        self.input_code_bar.textChanged.connect(self.codeBarTextChanged)
        self.input_code_bar.returnPressed.connect(self.filterArticleList)

    def filterArticleList(self):
        codeBar = self.input_code_bar.text().lower()
        listFilterArticles = []
        for cardArticle in self.listArticles:
            if codeBar in cardArticle.article.name.lower() or codeBar in cardArticle.article.id:
                newCardArticle = CardArticle(cardArticle.listener,cardArticle.article,self)
                listFilterArticles.append(newCardArticle)
        self.setListCardArticles(listFilterArticles)

    def codeBarTextChanged(self,codeBar):
        if codeBar.__len__() == 0:
            self.getAllArticles()

    def setupListener(self):
        self.listener.reloadInventory.connect(self.getAllArticles)
        
    def setupQwidgets(self):
        self.widgetRoot = QWidget(self)
        self.recycleBox = QGridLayout(self)
        self.recycleBox.setContentsMargins(6,6,6,6)
        self.widgetRoot.setLayout(self.recycleBox)
        self.scroll_area_articles.setWidget(self.widgetRoot)

    def getAllArticles(self):
        self.listArticles.clear()
        listArticle:list = articles.getAllArticles()
        for article in listArticle:
            cardArticle = CardArticle(self.listener,article,self)
            self.listArticles.append(cardArticle)
        self.setListCardArticles(self.listArticles)

    def setListCardArticles(self,listCardArticle:list):
        self.setupQwidgets()
        row = 0
        column = 0
        sizeColumn = 3
        for CardArticle in listCardArticle:
            self.recycleBox.addWidget(CardArticle,row,column)
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

