# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from common.utils import resources_qt_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(808, 722)
        Form.setStyleSheet(u"background-color: rgb(33, 40, 63);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_root = QFrame(Form)
        self.frame_root.setObjectName(u"frame_root")
        self.frame_root.setStyleSheet(u"background-color: rgb(40, 49, 78);")
        self.frame_root.setFrameShape(QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_root)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_search = QFrame(self.frame_root)
        self.frame_search.setObjectName(u"frame_search")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setMinimumSize(QSize(0, 40))
        self.frame_search.setStyleSheet(u"background-color: rgb(23, 28, 43);")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_search)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_search)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(32, 32))
        self.label.setMaximumSize(QSize(32, 32))
        self.label.setPixmap(QPixmap(u":/main_widget/src/search_ico.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.input_code_bar = QLineEdit(self.frame_search)
        self.input_code_bar.setObjectName(u"input_code_bar")
        font = QFont()
        font.setFamilies([u"Ausion Personal Use Extra"])
        font.setPointSize(14)
        self.input_code_bar.setFont(font)
        self.input_code_bar.setStyleSheet(u"border: 2px solid gray;\n"
" border-radius: 10px;\n"
"border-color: rgb(0, 254, 187);\n"
"background-color: rgb(31, 38, 59);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(70, 254, 227);")

        self.horizontalLayout.addWidget(self.input_code_bar)

        self.button_search_article = QPushButton(self.frame_search)
        self.button_search_article.setObjectName(u"button_search_article")
        font1 = QFont()
        font1.setFamilies([u"Ausion Personal Use"])
        font1.setPointSize(10)
        self.button_search_article.setFont(font1)
        self.button_search_article.setStyleSheet(u"color: rgb(175, 255, 234);")
        icon = QIcon()
        icon.addFile(u":/main_widget/src/btn_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_search_article.setIcon(icon)
        self.button_search_article.setIconSize(QSize(32, 32))
        self.button_search_article.setFlat(True)

        self.horizontalLayout.addWidget(self.button_search_article)

        self.button_open_cash_drawing = QPushButton(self.frame_search)
        self.button_open_cash_drawing.setObjectName(u"button_open_cash_drawing")
        self.button_open_cash_drawing.setFont(font1)
        self.button_open_cash_drawing.setStyleSheet(u"color: rgb(175, 255, 234);")
        icon1 = QIcon()
        icon1.addFile(u":/main_widget/src/btn_cash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_open_cash_drawing.setIcon(icon1)
        self.button_open_cash_drawing.setIconSize(QSize(32, 32))
        self.button_open_cash_drawing.setFlat(True)

        self.horizontalLayout.addWidget(self.button_open_cash_drawing)


        self.verticalLayout_9.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame_search)

        self.frame_controls = QFrame(self.frame_root)
        self.frame_controls.setObjectName(u"frame_controls")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy2)
        self.frame_controls.setStyleSheet(u"background-color: rgb(51, 62, 99);")
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_controls)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_controls)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(20, 10))
        self.label_4.setMaximumSize(QSize(100, 20))
        self.label_4.setPixmap(QPixmap(u":/main_widget/src/header_total.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setMargin(-2)
        self.label_4.setIndent(90)

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_7 = QLabel(self.frame_controls)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_7)

        self.lcd_number_total = QLCDNumber(self.frame_controls)
        self.lcd_number_total.setObjectName(u"lcd_number_total")
        self.lcd_number_total.setStyleSheet(u"background-color: rgb(16, 20, 31);\n"
"color: rgb(0, 254, 187);")

        self.verticalLayout_8.addWidget(self.lcd_number_total)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.button_reset_shopping_car = QPushButton(self.frame_controls)
        self.button_reset_shopping_car.setObjectName(u"button_reset_shopping_car")
        icon2 = QIcon()
        icon2.addFile(u":/main_widget/src/restore_btn1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_reset_shopping_car.setIcon(icon2)
        self.button_reset_shopping_car.setIconSize(QSize(35, 30))
        self.button_reset_shopping_car.setFlat(True)

        self.verticalLayout_8.addWidget(self.button_reset_shopping_car)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame_controls)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(20, 10))
        self.label_5.setMaximumSize(QSize(100, 20))
        self.label_5.setPixmap(QPixmap(u":/main_widget/src/header_mone.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setMargin(-2)
        self.label_5.setIndent(90)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_controls)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_6)

        self.lcd_number_change = QLCDNumber(self.frame_controls)
        self.lcd_number_change.setObjectName(u"lcd_number_change")
        self.lcd_number_change.setStyleSheet(u"background-color: rgb(16, 20, 31);\n"
"color: rgb(0, 254, 187);")

        self.verticalLayout_7.addWidget(self.lcd_number_change)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_controls)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(20, 10))
        self.label_8.setMaximumSize(QSize(100, 20))
        self.label_8.setPixmap(QPixmap(u":/main_widget/src/header_money_client.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setMargin(-2)
        self.label_8.setIndent(90)

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_3 = QLabel(self.frame_controls)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lcd_number_payment = QLCDNumber(self.frame_controls)
        self.lcd_number_payment.setObjectName(u"lcd_number_payment")
        self.lcd_number_payment.setStyleSheet(u"background-color: rgb(16, 20, 31);\n"
"color: rgb(0, 254, 187);")

        self.verticalLayout_6.addWidget(self.lcd_number_payment)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.frame_controls)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(20, 10))
        self.label_9.setMaximumSize(QSize(100, 20))
        self.label_9.setPixmap(QPixmap(u":/main_widget/src/mode_system.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setMargin(-2)
        self.label_9.setIndent(90)

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_2 = QLabel(self.frame_controls)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.label_mode_system = QLabel(self.frame_controls)
        self.label_mode_system.setObjectName(u"label_mode_system")
        self.label_mode_system.setFont(font1)
        self.label_mode_system.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_mode_system)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.lcd_number_efective_pay = QLCDNumber(self.frame_controls)
        self.lcd_number_efective_pay.setObjectName(u"lcd_number_efective_pay")
        self.lcd_number_efective_pay.setStyleSheet(u"background-color: rgb(16, 20, 31);\n"
"color: rgb(0, 254, 187);")

        self.verticalLayout_5.addWidget(self.lcd_number_efective_pay)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.calendar = QCalendarWidget(self.frame_controls)
        self.calendar.setObjectName(u"calendar")
        font2 = QFont()
        font2.setFamilies([u"Ausion Personal Use"])
        font2.setPointSize(11)
        self.calendar.setFont(font2)
        self.calendar.setFocusPolicy(Qt.NoFocus)
        self.calendar.setStyleSheet(u"background-color: rgb(40, 49, 78);\n"
"alternate-background-color: rgb(23, 28, 43);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(54, 67, 106);\n"
"selection-color: rgb(183, 243, 255);")

        self.horizontalLayout_3.addWidget(self.calendar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.frame_controls)

        self.frame_shopping_car = QFrame(self.frame_root)
        self.frame_shopping_car.setObjectName(u"frame_shopping_car")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_shopping_car.sizePolicy().hasHeightForWidth())
        self.frame_shopping_car.setSizePolicy(sizePolicy4)
        self.frame_shopping_car.setMinimumSize(QSize(50, 50))
        self.frame_shopping_car.setStyleSheet(u"background-color: rgb(23, 28, 43);")
        self.frame_shopping_car.setFrameShape(QFrame.StyledPanel)
        self.frame_shopping_car.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_shopping_car)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_shopping_car = QScrollArea(self.frame_shopping_car)
        self.scroll_area_shopping_car.setObjectName(u"scroll_area_shopping_car")
        self.scroll_area_shopping_car.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 764, 351))
        self.scroll_area_shopping_car.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scroll_area_shopping_car)


        self.verticalLayout_2.addWidget(self.frame_shopping_car)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame_root)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.button_search_article.setText(QCoreApplication.translate("Form", u"search", None))
        self.button_open_cash_drawing.setText(QCoreApplication.translate("Form", u"open cash", None))
        self.label_4.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.button_reset_shopping_car.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Mode System:", None))
        self.label_mode_system.setText(QCoreApplication.translate("Form", u"Shooping Card", None))
    # retranslateUi

