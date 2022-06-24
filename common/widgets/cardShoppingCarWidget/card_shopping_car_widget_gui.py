# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_shopping_car_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(295, 339)
        Form.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background: rgb(56, 57, 69);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_photo = QLabel(self.frame)
        self.label_photo.setObjectName(u"label_photo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_photo.sizePolicy().hasHeightForWidth())
        self.label_photo.setSizePolicy(sizePolicy)
        self.label_photo.setMinimumSize(QSize(0, 150))
        self.label_photo.setMaximumSize(QSize(300, 150))
        self.label_photo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_photo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_code_bar = QLabel(self.frame)
        self.label_code_bar.setObjectName(u"label_code_bar")
        self.label_code_bar.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_code_bar)

        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_3.addWidget(self.label_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_delete = QPushButton(self.frame)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.button_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_amount = QLabel(self.frame)
        self.label_amount.setObjectName(u"label_amount")

        self.horizontalLayout.addWidget(self.label_amount)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_price_unitary = QLabel(self.frame)
        self.label_price_unitary.setObjectName(u"label_price_unitary")

        self.horizontalLayout.addWidget(self.label_price_unitary)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_total_pay = QLabel(self.frame)
        self.label_total_pay.setObjectName(u"label_total_pay")

        self.horizontalLayout.addWidget(self.label_total_pay)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_photo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_code_bar.setText(QCoreApplication.translate("Form", u"1234", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"lubricante para cadenas", None))
        self.button_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_amount.setText(QCoreApplication.translate("Form", u"30.0 pz", None))
        self.label_price_unitary.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_total_pay.setText(QCoreApplication.translate("Form", u"$200", None))
    # retranslateUi

