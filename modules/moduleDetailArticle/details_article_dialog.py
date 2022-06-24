#pyside6
from PySide6.QtWidgets import QDialog,QMessageBox

#pydantic
from pydantic import ValidationError

#gui
from .details_article_dialog_gui import Ui_Dialog

#entities
from common.entities.article_entity import ArticleEntity

#firebase database
from common.database.firebase import articles

#string
from common.values import strings

from helper import loadImage

from modules.moduleInventory.signals.inventory_aux_widget import InventoryAuxWidget


class DetailsArticleDialog(QDialog,Ui_Dialog):
    isEdit:bool = False
    article:ArticleEntity = None
    listener:InventoryAuxWidget

    def __init__(self, listener:InventoryAuxWidget,parent = None,article:ArticleEntity = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(strings.title_create_article)
        self.listener = listener
        self.article = article

        self.setupButtons()
        self.setupEditLine()

        if self.article is not None:
            self.isEdit = True
            self.setWindowTitle(strings.title_edit_article)
            self.setArticleData()

    def setupEditLine(self):
        self.input_photo_url.textChanged.connect(self.setImageUrl)

    def setImageUrl(self,url):
        loadImage(self.photo,url)

    def setArticleData(self):
        self.input_code_bar.setText(self.article.id)
        self.input_code_bar.setEnabled(False)
        self.input_code_bar_confirm.setText(self.article.id)
        self.input_code_bar_confirm.setEnabled(False)
        self.input_name.setText(self.article.name)
        self.input_description.setPlainText(self.article.description)
        self.input_photo_url.setText(self.article.photoUrl)
        loadImage(self.photo,self.article.photoUrl)
        self.spin_price.setValue(self.article.price)
        self.spin_amount.setValue(self.article.amount)
        self.spin_off_sale.setValue(self.article.offSale)
        self.input_shelf.setText(self.article.shelf)
        self.input_vertical.setText(self.article.vertical)
        self.input_horizontal.setText(self.article.horizontal)
        self.combox_box_category.setCurrentText(self.article.category)

    def setupButtons(self):
        self.button_success.clicked.connect(self.validateArticle)
        self.button_cancel.clicked.connect(self.close)


    def validateArticle(self):
        try:
            articleEntity = ArticleEntity(
                id = self.input_code_bar.text(),
                name = self.input_name.text(),
                description = self.input_description.toPlainText(),
                photoUrl = self.input_photo_url.text(),
                price = self.spin_price.value(),
                amount = self.spin_amount.value(),
                offSale = self.spin_off_sale.value(),
                shelf = self.input_shelf.text(),
                vertical = self.input_vertical.text(),
                horizontal = self.input_horizontal.text(),
                category = self.combox_box_category.currentText()
            )
            if self.isEdit:
                articles.updateArticle(articleEntity)
                self.listener.reloadInventory.emit()
                self.close()
            else:
                if articles.existsArticle(articleEntity.id):
                    QMessageBox.warning(self,strings.msg_error,strings.msg_article_exists)
                else:
                    articles.saveArticle(articleEntity)
                    self.listener.reloadInventory.emit()

            self.clearFields()
        except ValidationError as error:
            QMessageBox().warning(self,strings.msg_error,error.errors.__str__())
    
    def clearFields(self):
        self.input_code_bar.setText("")
        self.input_code_bar_confirm.setText("")
        self.input_name.setText("")
        self.input_description.setPlainText("")
        self.input_photo_url.setText("")
        self.spin_price.setValue(0.0)
        self.spin_amount.setValue(0.0)
        self.spin_off_sale.setValue(0.0)
        self.input_shelf.setText("")
        self.input_vertical.setText("")
        self.input_horizontal.setText("")
        self.combox_box_category.setCurrentIndex(0)
            
    

    