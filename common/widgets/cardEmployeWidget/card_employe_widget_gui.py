# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_employe_widget.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(821, 279)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_root = QFrame(Form)
        self.frame_root.setObjectName(u"frame_root")
        self.frame_root.setFrameShape(QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_root)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_root)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setMaximumSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_name_employe = QLabel(self.frame_root)
        self.label_name_employe.setObjectName(u"label_name_employe")

        self.verticalLayout_2.addWidget(self.label_name_employe)

        self.label_rfc = QLabel(self.frame_root)
        self.label_rfc.setObjectName(u"label_rfc")

        self.verticalLayout_2.addWidget(self.label_rfc)

        self.label_phone = QLabel(self.frame_root)
        self.label_phone.setObjectName(u"label_phone")

        self.verticalLayout_2.addWidget(self.label_phone)

        self.label_email = QLabel(self.frame_root)
        self.label_email.setObjectName(u"label_email")

        self.verticalLayout_2.addWidget(self.label_email)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_delete = QPushButton(self.frame_root)
        self.button_delete.setObjectName(u"button_delete")

        self.horizontalLayout_2.addWidget(self.button_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.frame_pays_employe = QFrame(self.frame_root)
        self.frame_pays_employe.setObjectName(u"frame_pays_employe")
        self.frame_pays_employe.setMinimumSize(QSize(40, 0))
        self.frame_pays_employe.setFrameShape(QFrame.StyledPanel)
        self.frame_pays_employe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_pays_employe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.frame_pays_employe)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 245, 159))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.button_add_pay = QPushButton(self.frame_pays_employe)
        self.button_add_pay.setObjectName(u"button_add_pay")

        self.horizontalLayout_3.addWidget(self.button_add_pay)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.frame_pays_employe)


        self.verticalLayout.addWidget(self.frame_root)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"photo", None))
        self.label_name_employe.setText(QCoreApplication.translate("Form", u"Angel posada", None))
        self.label_rfc.setText(QCoreApplication.translate("Form", u"GKFKEL09090", None))
        self.label_phone.setText(QCoreApplication.translate("Form", u"676100000", None))
        self.label_email.setText(QCoreApplication.translate("Form", u"angelposada@example.com", None))
        self.button_delete.setText(QCoreApplication.translate("Form", u"delete", None))
        self.button_add_pay.setText(QCoreApplication.translate("Form", u"Nuevo Pago", None))
    # retranslateUi

