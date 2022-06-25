# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 481)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_root = QFrame(Dialog)
        self.frame_root.setObjectName(u"frame_root")
        self.frame_root.setFrameShape(QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_root)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_root)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 300))
        self.label.setMaximumSize(QSize(300, 300))

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.combo_box_email = QComboBox(self.frame_root)
        self.combo_box_email.setObjectName(u"combo_box_email")

        self.verticalLayout_2.addWidget(self.combo_box_email)

        self.input_password = QLineEdit(self.frame_root)
        self.input_password.setObjectName(u"input_password")

        self.verticalLayout_2.addWidget(self.input_password)

        self.button_login = QPushButton(self.frame_root)
        self.button_login.setObjectName(u"button_login")

        self.verticalLayout_2.addWidget(self.button_login)

        self.button_exit = QPushButton(self.frame_root)
        self.button_exit.setObjectName(u"button_exit")

        self.verticalLayout_2.addWidget(self.button_exit)


        self.verticalLayout.addWidget(self.frame_root)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"password", None))
        self.button_login.setText(QCoreApplication.translate("Dialog", u"login", None))
        self.button_exit.setText(QCoreApplication.translate("Dialog", u"exit", None))
    # retranslateUi

