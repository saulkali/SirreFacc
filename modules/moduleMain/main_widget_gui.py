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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(713, 589)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_root = QFrame(Form)
        self.frame_root.setObjectName(u"frame_root")
        self.frame_root.setFrameShape(QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_root)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_root)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(32, 32))
        self.label.setMaximumSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.label)

        self.input_code_bar = QLineEdit(self.frame_root)
        self.input_code_bar.setObjectName(u"input_code_bar")

        self.horizontalLayout.addWidget(self.input_code_bar)

        self.button_open_cash_drawing = QPushButton(self.frame_root)
        self.button_open_cash_drawing.setObjectName(u"button_open_cash_drawing")

        self.horizontalLayout.addWidget(self.button_open_cash_drawing)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame_controls = QFrame(self.frame_root)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_controls)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_controls)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.lcd_number_total = QLCDNumber(self.frame_controls)
        self.lcd_number_total.setObjectName(u"lcd_number_total")

        self.verticalLayout_8.addWidget(self.lcd_number_total)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_controls)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.lcd_number_change = QLCDNumber(self.frame_controls)
        self.lcd_number_change.setObjectName(u"lcd_number_change")

        self.verticalLayout_7.addWidget(self.lcd_number_change)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_controls)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lcd_number_payment = QLCDNumber(self.frame_controls)
        self.lcd_number_payment.setObjectName(u"lcd_number_payment")

        self.verticalLayout_6.addWidget(self.lcd_number_payment)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_controls)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_mode_system = QLabel(self.frame_controls)
        self.label_mode_system.setObjectName(u"label_mode_system")

        self.verticalLayout_5.addWidget(self.label_mode_system)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.calendar = QCalendarWidget(self.frame_controls)
        self.calendar.setObjectName(u"calendar")

        self.horizontalLayout_3.addWidget(self.calendar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.frame_controls)

        self.frame_shopping_car = QFrame(self.frame_root)
        self.frame_shopping_car.setObjectName(u"frame_shopping_car")
        self.frame_shopping_car.setMinimumSize(QSize(50, 50))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 657, 226))
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
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.button_open_cash_drawing.setText(QCoreApplication.translate("Form", u"open cash", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Mode System:", None))
        self.label_mode_system.setText(QCoreApplication.translate("Form", u"Shooping Card", None))
    # retranslateUi

