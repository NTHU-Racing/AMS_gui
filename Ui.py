# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1040)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1040))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1040))
        
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QLabel {
                color: #ffffff;
                font-family: "Segoe UI", "Microsoft JhengHei";
            }
            QPushButton {
                background-color: #333;
                color: white;
                border-radius: 6px;
                font-size: 18px;
                font-weight: bold;
                border: 1px solid #444;
            }
            QPushButton:hover {
                background-color: #444;
            }
            QProgressBar {
                border: 1px solid #333;
                border-radius: 2px;
                background-color: #222;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #00FF00, stop:1 #008800);
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        panel_style = "background-color: #1e1e1e; border: 1px solid #333; border-radius: 8px; padding: 10px;"

        self.AMS_Status = QtWidgets.QLabel(self.centralwidget)
        self.AMS_Status.setGeometry(QtCore.QRect(1610, 20, 290, 330))
        self.AMS_Status.setStyleSheet(panel_style + "color: #50fa7b; font-size: 20px; font-weight: bold;")
        self.AMS_Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AMS_Status.setObjectName("AMS_Status")

        self.Voltage_hilo = QtWidgets.QLabel(self.centralwidget)
        self.Voltage_hilo.setGeometry(QtCore.QRect(1610, 360, 290, 60))
        self.Voltage_hilo.setStyleSheet(panel_style + "color: #8be9fd; font-size: 22px;")
        self.Voltage_hilo.setObjectName("Voltage_hilo")

        self.temp_hilo = QtWidgets.QLabel(self.centralwidget)
        self.temp_hilo.setGeometry(QtCore.QRect(1610, 430, 290, 100))
        self.temp_hilo.setStyleSheet(panel_style + "color: #ffb86c; font-size: 22px;")
        self.temp_hilo.setObjectName("temp_hilo")

        self.Setting = QtWidgets.QPushButton(self.centralwidget)
        self.Setting.setGeometry(QtCore.QRect(1610, 840, 130, 50))
        self.Setting.setObjectName("Setting")

        self.Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Connect.setGeometry(QtCore.QRect(1610, 900, 130, 50))
        self.Connect.setStyleSheet("background-color: #28a745; color: white;")
        self.Connect.setObjectName("Connect")

        self.Disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.Disconnect.setGeometry(QtCore.QRect(1750, 900, 150, 50))
        self.Disconnect.setStyleSheet("background-color: #dc3545; color: white;")
        self.Disconnect.setObjectName("Disconnect")

        X_START = 30
        Y_START = 40
        X_STEP = 62  
        Y_STEP = 165
        GROUP_BIAS = 65 

        for i in range(0, 6):
            for j in range(0, 24):
                bias = GROUP_BIAS if j > 11 else 0
                pb = QtWidgets.QProgressBar(self.centralwidget, textVisible=False)
                pb.setGeometry(QtCore.QRect(X_START + X_STEP * j + bias, Y_START + Y_STEP * i, 38, 55))
                pb.setOrientation(QtCore.Qt.Vertical)
                pb.setObjectName("progressBar" + str(i * 24 + j))

        for i in range(0, 6):
            for j in range(0, 24):
                bias = GROUP_BIAS if j > 11 else 0
                v_lbl = QtWidgets.QLabel(self.centralwidget)
                v_lbl.setGeometry(QtCore.QRect(X_START + X_STEP * j + bias - 13, Y_START + 58 + Y_STEP * i, 65, 30))
                font = QtGui.QFont()
                font.setPointSize(11) 
                font.setBold(True)
                v_lbl.setFont(font)
                v_lbl.setAlignment(QtCore.Qt.AlignCenter)
                v_lbl.setText('0.00v')
                v_lbl.setObjectName("v" + str(i * 24 + j))

        for i in range(0, 6):
            for j in range(0, 32):
                bias = GROUP_BIAS if j > 15 else 0
                t_lbl = QtWidgets.QLabel(self.centralwidget)
                
                if((j > 7 and j < 16) or (j > 23)):
                    x_pos = X_START + X_STEP * (j - 8) + bias
                    y_pos = Y_START + 112 + Y_STEP * i
                else:
                    x_pos = X_START + X_STEP * j + bias
                    y_pos = Y_START + 92 + Y_STEP * i
                
                t_lbl.setGeometry(QtCore.QRect(x_pos - 13, y_pos, 65, 22))
                font = QtGui.QFont()
                font.setPointSize(10) 
                t_lbl.setFont(font)
                t_lbl.setStyleSheet("color: #bd93f9;") 
                t_lbl.setAlignment(QtCore.Qt.AlignCenter)
                t_lbl.setText('0.0°C')
                t_lbl.setObjectName("temp" + str(i * 32 + j))

        for i in range(0, 6):
            for j in range(0, 24):
                bias = GROUP_BIAS if j > 11 else 0
                dis = QtWidgets.QLabel(self.centralwidget)
                dis.setGeometry(QtCore.QRect(X_START + X_STEP * j + bias + 2, Y_START - 22 + Y_STEP * i, 34, 15))
                dis.setStyleSheet("background-color: #444; border-radius: 2px;")
                dis.setObjectName("dis" + str(i * 24 + j))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMS Monitoring System Pro"))
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.Setting.setText(_translate("MainWindow", "Setting"))