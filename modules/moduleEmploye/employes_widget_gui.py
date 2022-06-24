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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(768, 484)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.input_code_employee = QLineEdit(self.frame)
        self.input_code_employee.setObjectName(u"input_code_employee")

        self.horizontalLayout_2.addWidget(self.input_code_employee)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.table_widget_employes = QTableWidget(self.frame)
        if (self.table_widget_employes.columnCount() < 4):
            self.table_widget_employes.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_employes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_employes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_employes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget_employes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_widget_employes.setObjectName(u"table_widget_employes")

        self.verticalLayout_4.addWidget(self.table_widget_employes)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_add_employe = QPushButton(self.frame_2)
        self.button_add_employe.setObjectName(u"button_add_employe")

        self.horizontalLayout_5.addWidget(self.button_add_employe)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.button_see_more = QPushButton(self.frame)
        self.button_see_more.setObjectName(u"button_see_more")

        self.verticalLayout_3.addWidget(self.button_see_more)

        self.table_widget_pay = QTableWidget(self.frame)
        if (self.table_widget_pay.columnCount() < 3):
            self.table_widget_pay.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget_pay.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_widget_pay.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_widget_pay.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.table_widget_pay.setObjectName(u"table_widget_pay")

        self.verticalLayout_3.addWidget(self.table_widget_pay)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.button_add_pay = QPushButton(self.frame)
        self.button_add_pay.setObjectName(u"button_add_pay")

        self.horizontalLayout_3.addWidget(self.button_add_pay)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        ___qtablewidgetitem = self.table_widget_employes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.table_widget_employes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.table_widget_employes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Apellidos", None));
        ___qtablewidgetitem3 = self.table_widget_employes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"permisos", None));
        self.button_add_employe.setText(QCoreApplication.translate("Form", u"Nuevo Empleado", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"id", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"rfc", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"nombre", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"apellido", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"telefono", None))
        self.button_see_more.setText(QCoreApplication.translate("Form", u"ver mas...", None))
        ___qtablewidgetitem4 = self.table_widget_pay.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem5 = self.table_widget_pay.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"cantidad", None));
        ___qtablewidgetitem6 = self.table_widget_pay.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"fecha", None));
        self.button_add_pay.setText(QCoreApplication.translate("Form", u"nuevo pago", None))
    # retranslateUi

