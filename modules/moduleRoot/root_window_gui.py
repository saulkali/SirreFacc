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
from PySide6.QtWidgets import (QApplication, QDockWidget, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuarchivos = QMenu(self.menubar)
        self.menuarchivos.setObjectName(u"menuarchivos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_widget_control = QDockWidget(MainWindow)
        self.dock_widget_control.setObjectName(u"dock_widget_control")
        self.dock_widget_control.setFloating(False)
        self.dock_widget_control.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
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


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dock_widget_control.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget_control)

        self.menubar.addAction(self.menuarchivos.menuAction())
        self.menuarchivos.addAction(self.actioncerrar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actioncerrar.setText(QCoreApplication.translate("MainWindow", u"cerrar", None))
        self.menuarchivos.setTitle(QCoreApplication.translate("MainWindow", u"archivos", None))
        self.button_open_shopping_card.setText(QCoreApplication.translate("MainWindow", u"Shopping Card", None))
        self.button_open_inventory.setText(QCoreApplication.translate("MainWindow", u"inventory", None))
        self.button_open_employes.setText(QCoreApplication.translate("MainWindow", u"Employe", None))
    # retranslateUi

