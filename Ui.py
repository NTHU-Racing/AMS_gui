# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1690, 860)
        MainWindow.setMinimumSize(QtCore.QSize(1690, 960))
        MainWindow.setMaximumSize(QtCore.QSize(1690, 960))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AMS_Status = QtWidgets.QLabel(self.centralwidget)
        self.AMS_Status.setGeometry(QtCore.QRect(1400, 10, 275, 331))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AMS_Status.setFont(font)
        self.AMS_Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AMS_Status.setObjectName("AMS_Status")
        radius = 5
        self.AMS_Status.setStyleSheet(
            """
            background:rgb(200, 200, 200);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.Voltage_hilo = QtWidgets.QLabel(self.centralwidget)
        self.Voltage_hilo.setGeometry(QtCore.QRect(1400, 350, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Voltage_hilo.setFont(font)
        self.Voltage_hilo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Voltage_hilo.setObjectName("Voltage_hilo")
        radius = 5
        self.Voltage_hilo.setStyleSheet(
            """
            background:rgb(200, 200, 200);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.temp_hilo = QtWidgets.QLabel(self.centralwidget)
        self.temp_hilo.setGeometry(QtCore.QRect(1400, 410, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.temp_hilo.setFont(font)
        self.temp_hilo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temp_hilo.setObjectName("temp_hilo")
        radius = 5
        self.temp_hilo.setStyleSheet(
            """
            background:rgb(200, 200, 200);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Connect.setGeometry(QtCore.QRect(1390, 850, 141, 51))
        self.Connect.setObjectName("Connect")
        self.Disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.Disconnect.setGeometry(QtCore.QRect(1540, 850, 141, 51))
        self.Disconnect.setObjectName("Disconnect")
        self.Setting = QtWidgets.QPushButton(self.centralwidget)
        self.Setting.setGeometry(QtCore.QRect(1540, 790, 141, 51))
        self.Setting.setObjectName("Setting")
        for i in range(0,6,1):
            for j in range(0,24,1):
                self.temp = QtWidgets.QProgressBar(self.centralwidget, textVisible=False)
                self.bias = 0
                if (j > 11):
                    self.bias = 50
                else:
                    self.bias = 0
                self.temp.setGeometry(QtCore.QRect(20 + 50 * j + self.bias, 30 + 155 * i, 31, 51))
                self.temp.setProperty("value", 0)
                self.temp.setOrientation(QtCore.Qt.Vertical)
                self.temp.setObjectName("progressBar" + str(i * 24 + j))
        for i in range(0,6,1):
            for j in range(0,24,1):
                self.temp = QtWidgets.QLabel(self.centralwidget)
                self.bias = 0
                if (j > 11):
                    self.bias = 50
                else:
                    self.bias = 0
                self.temp.setGeometry(QtCore.QRect(10 + 50 * j + self.bias, 80 + 155 * i, 51, 21))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.temp.setFont(font)
                self.temp.setAlignment(QtCore.Qt.AlignCenter)
                self.temp.setObjectName("v" + str(i * 24 + j))
                self.temp.setText('0.00V')
        for i in range(0,6,1):
            for j in range(0,32,1):
                self.temp = QtWidgets.QLabel(self.centralwidget)
                self.bias = 0
                if (j > 15):
                    self.bias = 50
                else:
                    self.bias = 0
                if((j > 7 and j < 16) or (j > 23)):
                    self.temp.setGeometry(QtCore.QRect(10 + 50 * (j - 8) + self.bias, 130 + 155 * i, 51, 21))
                else:
                    self.temp.setGeometry(QtCore.QRect(10 + 50 * j + self.bias, 105 + 155 * i, 51, 21))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.temp.setFont(font)
                self.temp.setAlignment(QtCore.Qt.AlignCenter)
                self.temp.setObjectName("temp" + str(i * 32 + j))
                self.temp.setText(' 0deg')
        for i in range(0,6,1):
            for j in range(0,24,1):
                self.temp = QtWidgets.QLabel(self.centralwidget)
                self.bias = 0
                if (j > 11):
                    self.bias = 50
                else:
                    self.bias = 0
                self.temp.setGeometry(QtCore.QRect(20 + 50 * j + self.bias, 10 + 155 * i, 31, 16))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.temp.setFont(font)
                self.temp.setStyleSheet("background-color: rgb(255, 0, 4);")
                self.temp.setAlignment(QtCore.Qt.AlignCenter)
                self.temp.setObjectName("dis" + str(i * 24 + j))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1690, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.Setting.setText(_translate("MainWindow", "Setting"))