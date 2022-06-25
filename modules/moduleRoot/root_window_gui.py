# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'root_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actioncerrar = QAction(MainWindow)
        self.actioncerrar.setObjectName(u"actioncerrar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.dock_widget_control = QDockWidget(MainWindow)
        self.dock_widget_control.setObjectName(u"dock_widget_control")
        self.dock_widget_control.setFloating(False)
        self.dock_widget_control.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidgetContents.setMinimumSize(QSize(100, 0))
        self.dockWidgetContents.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_photo_employe = QLabel(self.dockWidgetContents)
        self.label_photo_employe.setObjectName(u"label_photo_employe")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_photo_employe.sizePolicy().hasHeightForWidth())
        self.label_photo_employe.setSizePolicy(sizePolicy)
        self.label_photo_employe.setMinimumSize(QSize(100, 100))
        self.label_photo_employe.setMaximumSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.label_photo_employe)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_name_employe = QLabel(self.dockWidgetContents)
        self.label_name_employe.setObjectName(u"label_name_employe")

        self.verticalLayout.addWidget(self.label_name_employe)

        self.button_open_shopping_card = QPushButton(self.dockWidgetContents)
        self.button_open_shopping_card.setObjectName(u"button_open_shopping_card")

        self.verticalLayout.addWidget(self.button_open_shopping_card)

        self.button_open_inventory = QPushButton(self.dockWidgetContents)
        self.button_open_inventory.setObjectName(u"button_open_inventory")

        self.verticalLayout.addWidget(self.button_open_inventory)

        self.button_open_employes = QPushButton(self.dockWidgetContents)
        self.button_open_employes.setObjectName(u"button_open_employes")

        self.verticalLayout.addWidget(self.button_open_employes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_settings = QPushButton(self.dockWidgetContents)
        self.button_settings.setObjectName(u"button_settings")

        self.verticalLayout.addWidget(self.button_settings)

        self.button_logout = QPushButton(self.dockWidgetContents)
        self.button_logout.setObjectName(u"button_logout")

        self.verticalLayout.addWidget(self.button_logout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dock_widget_control.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget_control)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actioncerrar.setText(QCoreApplication.translate("MainWindow", u"cerrar", None))
        self.label_photo_employe.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_name_employe.setText(QCoreApplication.translate("MainWindow", u"Saul burciaga Hernandez", None))
        self.button_open_shopping_card.setText(QCoreApplication.translate("MainWindow", u"Shopping Card", None))
        self.button_open_inventory.setText(QCoreApplication.translate("MainWindow", u"inventory", None))
        self.button_open_employes.setText(QCoreApplication.translate("MainWindow", u"Employe", None))
        self.button_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.button_logout.setText(QCoreApplication.translate("MainWindow", u"logout", None))
    # retranslateUi

