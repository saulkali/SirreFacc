#pyside6
from PySide6.QtWidgets import QWidget,QMessageBox

#entities
from common.entities.article_entity import ArticleEntity

#module
from modules.moduleDetailArticle.details_article_dialog import DetailsArticleDialog
from modules.moduleInventory.signals.inventory_aux_widget import InventoryAuxWidget

#gui
from .card_article_widget_gui import Ui_Form

from helper import loadImage

from common.database.firebase import articles

from common.values import strings



class CardArticle (QWidget,Ui_Form):
    listener:InventoryAuxWidget
    def __init__(self,listener:InventoryAuxWidget,article:ArticleEntity, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.article = article
        self.listener = listener
        self.setInfoArticle()
        self.setupButtons()

    def setupButtons(self):
        self.button_delete.clicked.connect(self.deleteArticle)

    def deleteArticle(self):
        result = QMessageBox.warning(self,strings.msg_error,strings.msg_delete_ask,QMessageBox.Yes|QMessageBox.No)
        if result == QMessageBox.Yes:
            articles.deleteArticle(self.article)
            self.listener.reloadInventory.emit()
            self.close()

    def setInfoArticle(self):
        loadImage(self.label_photo,self.article.photoUrl)

        self.label_name.setText(self.article.name)
        self.label_code_bar.setText(self.article.id)
        self.label_price.setText(f"${self.article.price}")
        self.label_amount.setText(f"{self.article.amount}")
    
    def openDetailsArticle(self):
        detailsArticle = DetailsArticleDialog(self.listener,self,self.article)
        detailsArticle.exec()
    
    def mousePressEvent(self,event) -> None:
        self.openDetailsArticle()
        return super().mousePressEvent(event)
