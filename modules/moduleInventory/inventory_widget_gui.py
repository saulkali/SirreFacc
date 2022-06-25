# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_widget.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 757)
        Form.setMinimumSize(QSize(500, 500))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_search = QFrame(self.frame)
        self.frame_search.setObjectName(u"frame_search")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setMinimumSize(QSize(0, 40))
        self.frame_search.setMaximumSize(QSize(16777215, 70))
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_search)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_search)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(32, 32))
        self.label.setMaximumSize(QSize(32, 32))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.input_code_bar = QLineEdit(self.frame_search)
        self.input_code_bar.setObjectName(u"input_code_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_code_bar.sizePolicy().hasHeightForWidth())
        self.input_code_bar.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.input_code_bar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.frame_search)

        self.frame_recycle_article = QFrame(self.frame)
        self.frame_recycle_article.setObjectName(u"frame_recycle_article")
        sizePolicy1.setHeightForWidth(self.frame_recycle_article.sizePolicy().hasHeightForWidth())
        self.frame_recycle_article.setSizePolicy(sizePolicy1)
        self.frame_recycle_article.setMinimumSize(QSize(0, 0))
        self.frame_recycle_article.setFrameShape(QFrame.StyledPanel)
        self.frame_recycle_article.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_recycle_article)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scroll_area_articles = QScrollArea(self.frame_recycle_article)
        self.scroll_area_articles.setObjectName(u"scroll_area_articles")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scroll_area_articles.sizePolicy().hasHeightForWidth())
        self.scroll_area_articles.setSizePolicy(sizePolicy3)
        self.scroll_area_articles.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 733, 517))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scroll_area_articles.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scroll_area_articles)


        self.verticalLayout_2.addWidget(self.frame_recycle_article)

        self.frame_controls_inventory = QFrame(self.frame)
        self.frame_controls_inventory.setObjectName(u"frame_controls_inventory")
        self.frame_controls_inventory.setFrameShape(QFrame.StyledPanel)
        self.frame_controls_inventory.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_controls_inventory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_open_add_article = QPushButton(self.frame_controls_inventory)
        self.button_open_add_article.setObjectName(u"button_open_add_article")

        self.horizontalLayout_2.addWidget(self.button_open_add_article)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame_controls_inventory)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.button_open_add_article.setText(QCoreApplication.translate("Form", u"add article", None))
    # retranslateUi

