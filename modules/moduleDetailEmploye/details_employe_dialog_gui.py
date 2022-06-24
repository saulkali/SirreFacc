# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'details_employe.ui'
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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(243, 552)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 150))
        self.label.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_2.addWidget(self.label)

        self.input_photo_url = QLineEdit(self.frame)
        self.input_photo_url.setObjectName(u"input_photo_url")

        self.verticalLayout_2.addWidget(self.input_photo_url)

        self.input_first_name = QLineEdit(self.frame)
        self.input_first_name.setObjectName(u"input_first_name")

        self.verticalLayout_2.addWidget(self.input_first_name)

        self.input_last_name = QLineEdit(self.frame)
        self.input_last_name.setObjectName(u"input_last_name")

        self.verticalLayout_2.addWidget(self.input_last_name)

        self.input_password = QLineEdit(self.frame)
        self.input_password.setObjectName(u"input_password")

        self.verticalLayout_2.addWidget(self.input_password)

        self.input_confirm_password = QLineEdit(self.frame)
        self.input_confirm_password.setObjectName(u"input_confirm_password")

        self.verticalLayout_2.addWidget(self.input_confirm_password)

        self.input_phone = QLineEdit(self.frame)
        self.input_phone.setObjectName(u"input_phone")

        self.verticalLayout_2.addWidget(self.input_phone)

        self.input_address = QLineEdit(self.frame)
        self.input_address.setObjectName(u"input_address")

        self.verticalLayout_2.addWidget(self.input_address)

        self.spin_box_cp = QSpinBox(self.frame)
        self.spin_box_cp.setObjectName(u"spin_box_cp")
        self.spin_box_cp.setMaximum(999999)

        self.verticalLayout_2.addWidget(self.spin_box_cp)

        self.input_email = QLineEdit(self.frame)
        self.input_email.setObjectName(u"input_email")

        self.verticalLayout_2.addWidget(self.input_email)

        self.input_rfc = QLineEdit(self.frame)
        self.input_rfc.setObjectName(u"input_rfc")

        self.verticalLayout_2.addWidget(self.input_rfc)

        self.combo_box_permissions = QComboBox(self.frame)
        self.combo_box_permissions.setObjectName(u"combo_box_permissions")

        self.verticalLayout_2.addWidget(self.combo_box_permissions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_cancel = QPushButton(self.frame)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_accept = QPushButton(self.frame)
        self.button_accept.setObjectName(u"button_accept")

        self.horizontalLayout.addWidget(self.button_accept)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.input_photo_url.setPlaceholderText(QCoreApplication.translate("Dialog", u"photo url", None))
        self.input_first_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.input_last_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Apellidos", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"constrase\u00f1a", None))
        self.input_confirm_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"confirma contrase\u00f1a", None))
        self.input_phone.setPlaceholderText(QCoreApplication.translate("Dialog", u"numero de telefono", None))
        self.input_address.setPlaceholderText(QCoreApplication.translate("Dialog", u"direccion", None))
        self.input_email.setPlaceholderText(QCoreApplication.translate("Dialog", u"Correo electronico", None))
        self.input_rfc.setPlaceholderText(QCoreApplication.translate("Dialog", u"rfc", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog", u"cancelar", None))
        self.button_accept.setText(QCoreApplication.translate("Dialog", u"aceptar", None))
    # retranslateUi

