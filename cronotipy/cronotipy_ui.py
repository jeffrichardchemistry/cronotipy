# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cronotipy_mw(object):
    def setupUi(self, cronotipy_mw):
        cronotipy_mw.setObjectName("cronotipy_mw")
        cronotipy_mw.resize(782, 524)
        cronotipy_mw.setStyleSheet("background-color: rgba(84, 84, 84, 0.5);")
        self.centralwidget = QtWidgets.QWidget(cronotipy_mw)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_down = QtWidgets.QVBoxLayout()
        self.layout_down.setObjectName("layout_down")
        self.scrollA_bot = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollA_bot.setWidgetResizable(True)
        self.scrollA_bot.setObjectName("scrollA_bot")
        self.scrollAWD_bot = QtWidgets.QWidget()
        self.scrollAWD_bot.setGeometry(QtCore.QRect(0, 0, 696, 236))
        self.scrollAWD_bot.setObjectName("scrollAWD_bot")
        self.scrollA_bot.setWidget(self.scrollAWD_bot)
        self.layout_down.addWidget(self.scrollA_bot)
        self.gridLayout.addLayout(self.layout_down, 1, 0, 1, 1)
        self.layout_up = QtWidgets.QVBoxLayout()
        self.layout_up.setObjectName("layout_up")
        self.scrollA_top = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollA_top.setWidgetResizable(True)
        self.scrollA_top.setObjectName("scrollA_top")
        self.scrollAWD_top = QtWidgets.QWidget()
        self.scrollAWD_top.setGeometry(QtCore.QRect(0, 0, 696, 236))
        self.scrollAWD_top.setObjectName("scrollAWD_top")
        self.scrollA_top.setWidget(self.scrollAWD_top)
        self.layout_up.addWidget(self.scrollA_top)
        self.gridLayout.addLayout(self.layout_up, 0, 0, 1, 1)
        cronotipy_mw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cronotipy_mw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 20))
        self.menubar.setObjectName("menubar")
        self.menu_Menu = QtWidgets.QMenu(self.menubar)
        self.menu_Menu.setObjectName("menu_Menu")
        self.menu_Alert = QtWidgets.QMenu(self.menubar)
        self.menu_Alert.setObjectName("menu_Alert")
        cronotipy_mw.setMenuBar(self.menubar)
        self.dockwd = QtWidgets.QDockWidget(cronotipy_mw)
        self.dockwd.setMinimumSize(QtCore.QSize(58, 35))
        self.dockwd.setObjectName("dockwd")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.btn_create = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btn_create.setGeometry(QtCore.QRect(10, 0, 41, 23))
        self.btn_create.setMinimumSize(QtCore.QSize(41, 23))
        self.btn_create.setMaximumSize(QtCore.QSize(81, 45))
        self.btn_create.setObjectName("btn_create")
        self.btn_remove = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btn_remove.setGeometry(QtCore.QRect(10, 30, 41, 23))
        self.btn_remove.setMinimumSize(QtCore.QSize(41, 23))
        self.btn_remove.setMaximumSize(QtCore.QSize(81, 45))
        self.btn_remove.setObjectName("btn_remove")
        self.dockwd.setWidget(self.dockWidgetContents_2)
        cronotipy_mw.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockwd)
        self.menu_New = QtWidgets.QAction(cronotipy_mw)
        self.menu_New.setObjectName("menu_New")
        self.menu_Open = QtWidgets.QAction(cronotipy_mw)
        self.menu_Open.setObjectName("menu_Open")
        self.menu_Save = QtWidgets.QAction(cronotipy_mw)
        self.menu_Save.setObjectName("menu_Save")
        self.menu_Quit = QtWidgets.QAction(cronotipy_mw)
        self.menu_Quit.setObjectName("menu_Quit")
        self.menu_Notify_On_Off = QtWidgets.QAction(cronotipy_mw)
        self.menu_Notify_On_Off.setCheckable(True)
        self.menu_Notify_On_Off.setChecked(True)
        self.menu_Notify_On_Off.setObjectName("menu_Notify_On_Off")
        self.menu_Sound_On_Off = QtWidgets.QAction(cronotipy_mw)
        self.menu_Sound_On_Off.setCheckable(True)
        self.menu_Sound_On_Off.setChecked(True)
        self.menu_Sound_On_Off.setObjectName("menu_Sound_On_Off")
        self.menu_Loop_On_Off = QtWidgets.QAction(cronotipy_mw)
        self.menu_Loop_On_Off.setCheckable(True)
        self.menu_Loop_On_Off.setObjectName("menu_Loop_On_Off")
        self.menu_Menu.addAction(self.menu_Open)
        self.menu_Menu.addAction(self.menu_Save)
        self.menu_Menu.addSeparator()
        self.menu_Menu.addAction(self.menu_Quit)
        self.menu_Alert.addAction(self.menu_Notify_On_Off)
        self.menu_Alert.addAction(self.menu_Sound_On_Off)
        self.menu_Alert.addAction(self.menu_Loop_On_Off)
        self.menubar.addAction(self.menu_Menu.menuAction())
        self.menubar.addAction(self.menu_Alert.menuAction())

        self.retranslateUi(cronotipy_mw)
        QtCore.QMetaObject.connectSlotsByName(cronotipy_mw)

    def retranslateUi(self, cronotipy_mw):
        _translate = QtCore.QCoreApplication.translate
        cronotipy_mw.setWindowTitle(_translate("cronotipy_mw", "Cronotipy"))
        self.menu_Menu.setTitle(_translate("cronotipy_mw", "Menu"))
        self.menu_Alert.setTitle(_translate("cronotipy_mw", "Alert"))
        self.btn_create.setText(_translate("cronotipy_mw", "+"))
        self.btn_remove.setText(_translate("cronotipy_mw", "-"))
        self.menu_New.setText(_translate("cronotipy_mw", "New"))
        self.menu_Open.setText(_translate("cronotipy_mw", "Open"))
        self.menu_Save.setText(_translate("cronotipy_mw", "Save"))
        self.menu_Quit.setText(_translate("cronotipy_mw", "Quit"))
        self.menu_Notify_On_Off.setText(_translate("cronotipy_mw", "Notify On/Off"))
        self.menu_Sound_On_Off.setText(_translate("cronotipy_mw", "Sound ON/Off"))
        self.menu_Loop_On_Off.setText(_translate("cronotipy_mw", "Loop"))
