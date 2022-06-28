# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_article_widget.ui'
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
from common.utils import resources_qt_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(315, 339)
        Form.setCursor(QCursor(Qt.PointingHandCursor))
        Form.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_root = QFrame(Form)
        self.frame_root.setObjectName(u"frame_root")
        self.frame_root.setStyleSheet(u"QFrame[objectName^=\"frame_root\"]{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(16, 20, 31);\n"
"\n"
"}\n"
"\n"
"QFrame[objectName^=\"frame_root\"]:hover{\n"
"\n"
"	\n"
"	background-color: rgb(29, 36, 57);\n"
"\n"
"}")
        self.frame_root.setFrameShape(QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_root)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_photo = QLabel(self.frame_root)
        self.label_photo.setObjectName(u"label_photo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_photo.sizePolicy().hasHeightForWidth())
        self.label_photo.setSizePolicy(sizePolicy)
        self.label_photo.setMinimumSize(QSize(0, 150))
        self.label_photo.setMaximumSize(QSize(300, 150))
        font = QFont()
        font.setFamilies([u"Ausion Personal Use"])
        font.setPointSize(10)
        self.label_photo.setFont(font)
        self.label_photo.setStyleSheet(u"QFrame#frame_root{\n"
"	background:red;\n"
"}")
        self.label_photo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_photo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_code_bar = QLabel(self.frame_root)
        self.label_code_bar.setObjectName(u"label_code_bar")
        font1 = QFont()
        font1.setFamilies([u"Ausion Personal Use"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_code_bar.setFont(font1)
        self.label_code_bar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_code_bar.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.label_code_bar)

        self.label_name = QLabel(self.frame_root)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_delete = QPushButton(self.frame_root)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/main_widget/src/trash_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_delete.setIcon(icon)
        self.button_delete.setIconSize(QSize(80, 50))
        self.button_delete.setFlat(True)

        self.horizontalLayout.addWidget(self.button_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_root)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 35))
        self.label.setPixmap(QPixmap(u":/card_article_widget/src/pieces_.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-2)

        self.horizontalLayout.addWidget(self.label)

        self.label_amount = QLabel(self.frame_root)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setFont(font)
        self.label_amount.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_amount)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.frame_root)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 23))
        self.label_2.setPixmap(QPixmap(u":/main_widget/src/money.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(-5)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_price = QLabel(self.frame_root)
        self.label_price.setObjectName(u"label_price")
        font2 = QFont()
        font2.setFamilies([u"Ausion Personal Use Extra"])
        font2.setPointSize(14)
        self.label_price.setFont(font2)
        self.label_price.setStyleSheet(u"color: rgb(0, 254, 187);")

        self.horizontalLayout.addWidget(self.label_price)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.frame_root)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_photo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_code_bar.setText(QCoreApplication.translate("Form", u"1234", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"lubricante para cadenas", None))
        self.button_delete.setText("")
        self.label.setText("")
        self.label_amount.setText(QCoreApplication.translate("Form", u"30.0 pz", None))
        self.label_2.setText("")
        self.label_price.setText(QCoreApplication.translate("Form", u"$200", None))
    # retranslateUi

