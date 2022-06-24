# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'details_article.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(212, 634)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.photo = QLabel(Dialog)
        self.photo.setObjectName(u"photo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo.sizePolicy().hasHeightForWidth())
        self.photo.setSizePolicy(sizePolicy)
        self.photo.setMinimumSize(QSize(0, 150))
        self.photo.setMaximumSize(QSize(16777215, 150))
        self.photo.setScaledContents(True)

        self.verticalLayout.addWidget(self.photo)

        self.input_photo_url = QLineEdit(Dialog)
        self.input_photo_url.setObjectName(u"input_photo_url")

        self.verticalLayout.addWidget(self.input_photo_url)

        self.input_code_bar = QLineEdit(Dialog)
        self.input_code_bar.setObjectName(u"input_code_bar")

        self.verticalLayout.addWidget(self.input_code_bar)

        self.input_code_bar_confirm = QLineEdit(Dialog)
        self.input_code_bar_confirm.setObjectName(u"input_code_bar_confirm")

        self.verticalLayout.addWidget(self.input_code_bar_confirm)

        self.input_name = QLineEdit(Dialog)
        self.input_name.setObjectName(u"input_name")

        self.verticalLayout.addWidget(self.input_name)

        self.input_description = QPlainTextEdit(Dialog)
        self.input_description.setObjectName(u"input_description")

        self.verticalLayout.addWidget(self.input_description)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)

        self.combox_box_method_shopping = QComboBox(Dialog)
        self.combox_box_method_shopping.setObjectName(u"combox_box_method_shopping")

        self.gridLayout.addWidget(self.combox_box_method_shopping, 3, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.input_shelf = QLineEdit(Dialog)
        self.input_shelf.setObjectName(u"input_shelf")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_shelf.sizePolicy().hasHeightForWidth())
        self.input_shelf.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.input_shelf, 5, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.combox_box_category = QComboBox(Dialog)
        self.combox_box_category.setObjectName(u"combox_box_category")

        self.gridLayout.addWidget(self.combox_box_category, 5, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.spin_amount = QDoubleSpinBox(Dialog)
        self.spin_amount.setObjectName(u"spin_amount")

        self.gridLayout.addWidget(self.spin_amount, 1, 0, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)

        self.spin_off_sale = QDoubleSpinBox(Dialog)
        self.spin_off_sale.setObjectName(u"spin_off_sale")

        self.gridLayout.addWidget(self.spin_off_sale, 3, 0, 1, 1)

        self.spin_price = QDoubleSpinBox(Dialog)
        self.spin_price.setObjectName(u"spin_price")

        self.gridLayout.addWidget(self.spin_price, 1, 1, 1, 1)

        self.input_horizontal = QLineEdit(Dialog)
        self.input_horizontal.setObjectName(u"input_horizontal")
        sizePolicy1.setHeightForWidth(self.input_horizontal.sizePolicy().hasHeightForWidth())
        self.input_horizontal.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.input_horizontal, 7, 0, 1, 1)

        self.input_vertical = QLineEdit(Dialog)
        self.input_vertical.setObjectName(u"input_vertical")
        sizePolicy1.setHeightForWidth(self.input_vertical.sizePolicy().hasHeightForWidth())
        self.input_vertical.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.input_vertical, 7, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_cancel = QPushButton(Dialog)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_success = QPushButton(Dialog)
        self.button_success.setObjectName(u"button_success")

        self.horizontalLayout.addWidget(self.button_success)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.photo.setText(QCoreApplication.translate("Dialog", u"photo", None))
        self.input_photo_url.setPlaceholderText(QCoreApplication.translate("Dialog", u"photo url", None))
        self.input_code_bar.setPlaceholderText(QCoreApplication.translate("Dialog", u"codigo de barra", None))
        self.input_code_bar_confirm.setPlaceholderText(QCoreApplication.translate("Dialog", u"confirmar codigo de barra", None))
        self.input_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"nombre", None))
        self.input_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Descripcion", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Estante", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Modo De Venta", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Descuento %", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Categoria", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Horizontal", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Precio Unitario", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Vertical", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.button_success.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
    # retranslateUi

