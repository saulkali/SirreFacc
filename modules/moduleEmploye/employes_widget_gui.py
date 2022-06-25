# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employes_widget.ui'
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
        Form.resize(768, 484)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_root = QFrame(Form)
        self.frame_root.setObjectName(u"frame_root")
        self.frame_root.setFrameShape(QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_root)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_search = QFrame(self.frame_root)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 40))
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_search)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_search)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.input_code_employee = QLineEdit(self.frame_search)
        self.input_code_employee.setObjectName(u"input_code_employee")

        self.horizontalLayout_2.addWidget(self.input_code_employee)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.frame_search)

        self.frame_recycle = QFrame(self.frame_root)
        self.frame_recycle.setObjectName(u"frame_recycle")
        self.frame_recycle.setFrameShape(QFrame.StyledPanel)
        self.frame_recycle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_recycle)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scroll_area_employes = QScrollArea(self.frame_recycle)
        self.scroll_area_employes.setObjectName(u"scroll_area_employes")
        self.scroll_area_employes.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 712, 289))
        self.scroll_area_employes.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scroll_area_employes)


        self.verticalLayout_4.addWidget(self.frame_recycle)

        self.frame_controls = QFrame(self.frame_root)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_controls)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_add_employe = QPushButton(self.frame_controls)
        self.button_add_employe.setObjectName(u"button_add_employe")

        self.horizontalLayout_5.addWidget(self.button_add_employe)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.frame_controls)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frame_root)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.button_add_employe.setText(QCoreApplication.translate("Form", u"Nuevo Empleado", None))
    # retranslateUi

