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

from common.utils import resources_qt_rc

class Ui_main_root(object):
    def setupUi(self, main_root):
        if not main_root.objectName():
            main_root.setObjectName(u"main_root")
        main_root.resize(790, 633)
        main_root.setStyleSheet(u"background-color: rgb(23, 28, 43);\n"
"\n"
"")
        self.actioncerrar = QAction(main_root)
        self.actioncerrar.setObjectName(u"actioncerrar")
        self.centralwidget = QWidget(main_root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        main_root.setCentralWidget(self.centralwidget)
        self.dock_widget_control = QDockWidget(main_root)
        self.dock_widget_control.setObjectName(u"dock_widget_control")
        self.dock_widget_control.setMinimumSize(QSize(100, 633))
        self.dock_widget_control.setMaximumSize(QSize(100, 524287))
        font = QFont()
        font.setFamilies([u"Ausion Personal Use"])
        font.setPointSize(9)
        self.dock_widget_control.setFont(font)
        icon = QIcon()
        icon.addFile(u":/root_window/src/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dock_widget_control.setWindowIcon(icon)
        self.dock_widget_control.setStyleSheet(u"QDockWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.dock_widget_control.setFloating(False)
        self.dock_widget_control.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_widget_control.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidgetContents.setMinimumSize(QSize(100, 0))
        self.dockWidgetContents.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
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
        self.label_photo_employe.setMinimumSize(QSize(50, 70))
        self.label_photo_employe.setMaximumSize(QSize(50, 70))
        self.label_photo_employe.setFont(font)

        self.horizontalLayout.addWidget(self.label_photo_employe)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 10))
        self.label.setPixmap(QPixmap(u":/root_window/src/user.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-1)
        self.label.setIndent(90)

        self.verticalLayout.addWidget(self.label)

        self.label_name_employe = QLabel(self.dockWidgetContents)
        self.label_name_employe.setObjectName(u"label_name_employe")
        font1 = QFont()
        font1.setFamilies([u"Ausion Personal Use Extra"])
        font1.setPointSize(9)
        self.label_name_employe.setFont(font1)
        self.label_name_employe.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_name_employe)

        self.button_open_shopping_card = QPushButton(self.dockWidgetContents)
        self.button_open_shopping_card.setObjectName(u"button_open_shopping_card")
        self.button_open_shopping_card.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_shopping_card.setFocusPolicy(Qt.NoFocus)
        self.button_open_shopping_card.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/root_window/src/shopping_card.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_open_shopping_card.setIcon(icon1)
        self.button_open_shopping_card.setIconSize(QSize(50, 50))
        self.button_open_shopping_card.setCheckable(False)
        self.button_open_shopping_card.setChecked(False)
        self.button_open_shopping_card.setFlat(True)

        self.verticalLayout.addWidget(self.button_open_shopping_card)

        self.button_open_inventory = QPushButton(self.dockWidgetContents)
        self.button_open_inventory.setObjectName(u"button_open_inventory")
        self.button_open_inventory.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_inventory.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/root_window/src/inventory.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_open_inventory.setIcon(icon2)
        self.button_open_inventory.setIconSize(QSize(50, 50))
        self.button_open_inventory.setCheckable(False)
        self.button_open_inventory.setFlat(True)

        self.verticalLayout.addWidget(self.button_open_inventory)

        self.button_open_employes = QPushButton(self.dockWidgetContents)
        self.button_open_employes.setObjectName(u"button_open_employes")
        self.button_open_employes.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_employes.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/root_window/src/employe.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_open_employes.setIcon(icon3)
        self.button_open_employes.setIconSize(QSize(50, 50))
        self.button_open_employes.setFlat(True)

        self.verticalLayout.addWidget(self.button_open_employes)

        self.button_clients = QPushButton(self.dockWidgetContents)
        self.button_clients.setObjectName(u"button_clients")
        self.button_clients.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_clients.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.button_clients)

        self.button_issue = QPushButton(self.dockWidgetContents)
        self.button_issue.setObjectName(u"button_issue")
        self.button_issue.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_issue.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.button_issue)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_settings = QPushButton(self.dockWidgetContents)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/root_window/src/setting_butt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon4)
        self.button_settings.setIconSize(QSize(40, 40))
        self.button_settings.setFlat(True)

        self.verticalLayout.addWidget(self.button_settings)

        self.button_logout = QPushButton(self.dockWidgetContents)
        self.button_logout.setObjectName(u"button_logout")
        self.button_logout.setFocusPolicy(Qt.NoFocus)
        icon5 = QIcon()
        icon5.addFile(u":/root_window/src/close_session.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_logout.setIcon(icon5)
        self.button_logout.setIconSize(QSize(40, 40))
        self.button_logout.setFlat(True)

        self.verticalLayout.addWidget(self.button_logout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dock_widget_control.setWidget(self.dockWidgetContents)
        main_root.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget_control)

        self.retranslateUi(main_root)

        QMetaObject.connectSlotsByName(main_root)
    # setupUi

    def retranslateUi(self, main_root):
        main_root.setWindowTitle(QCoreApplication.translate("main_root", u"MainWindow", None))
        self.actioncerrar.setText(QCoreApplication.translate("main_root", u"cerrar", None))
        self.dock_widget_control.setWindowTitle(QCoreApplication.translate("main_root", u"Controles", None))
        self.label_photo_employe.setText(QCoreApplication.translate("main_root", u"TextLabel", None))
        self.label.setText("")
        self.label_name_employe.setText(QCoreApplication.translate("main_root", u"Saul burciaga Hernandez", None))
        self.button_open_shopping_card.setText("")
        self.button_open_inventory.setText("")
        self.button_open_employes.setText("")
        self.button_clients.setText(QCoreApplication.translate("main_root", u"clients", None))
        self.button_issue.setText(QCoreApplication.translate("main_root", u"issue", None))
        self.button_settings.setText("")
        self.button_logout.setText("")
    # retranslateUi

