import serial
import os
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal,QTimer
from Ui import Ui_MainWindow
from setting import Ui_Setting_window

COM_port = 'COM6'
BAUD_RATES = 115200

total_ic = 12
cell_v = np.zeros(total_ic * 12)
cell_temp = np.zeros(total_ic * 16)
read_setting = False




class ThreadTask(QThread):
    return_AMS_status = pyqtSignal(str)
    return_v = pyqtSignal(str)
    return_dis = pyqtSignal(str)
    return_temp = pyqtSignal(str)

    def serial_read(self):
        global total_ic 
        global COM_port
        global BAUD_RATES
        global read_setting
        sec = 0 
        '''0:init,1:total,2:v,3:temp,4:dis'''
        s = ''
        Cycle = ''
        AMS_status = ''
        v_str = ''
        temp_str = ''
        dis_str = ''
        is_send = True
        line = 0
        try:
            ser = serial.Serial(COM_port, BAUD_RATES)
            if(read_setting):
                ser.write(b'd\n')
            else:
                ser.write(b's\n')
                
            is_send = True
            while is_send :
                while ser.in_waiting: 
                    is_read = True
                    data_raw = ser.readline()
                    s = s + data_raw.decode()
                    if(line <= 2):
                        AMS_status = AMS_status + data_raw.decode()
                        print('total')
                        sec = 1
                    elif(line <= 2 +(total_ic + 2)):
                        print('Voltage')
                        sec = 2
                        v_str = v_str + data_raw.decode()
                    elif(line <= 2 + 2 * (total_ic + 2) - 1):
                        temp_str = temp_str + data_raw.decode()
                        print('Temp')
                        sec = 3
                    else:
                        print('Dis')
                        dis_str = dis_str + data_raw.decode()
                        sec = 4
                    print(str(line) + ' '+ data_raw.decode())
                    line = line + 1
                    if(data_raw == b'\r\r\r\r\r\r\r\r\r\r\n'):
                        
                        if(read_setting):
                            self.return_AMS_status.emit(AMS_status)
                            self.return_v.emit(v_str)
                            self.return_dis.emit(dis_str)
                            self.return_temp.emit(temp_str)
                        else:
                            read_setting = True
                            total_ic = int(s[0:2])
                            print(total_ic)
                        s = ''
                        v_str = ''
                        temp_str = ''
                        AMS_status = ''
                        dis_str = ''
                        line = 0
                        is_send = False
            ser.close()     
        except Exception  as e:
            AMS_status = 'Can_not_connect_to_' + COM_port
            self.return_AMS_status.emit(AMS_status)


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.MainWindow = Ui_MainWindow()
        self.MainWindow.setupUi(self)
        self.setup_control()
        self.setting_win = Setting_window()
        self.MainWindow.Setting.clicked.connect(self.setting_func)

    def setting_func(self):
        self.setting_win.show()

    def setup_control(self):
        self.MainWindow.Connect.clicked.connect(self.Start_read)
        self.MainWindow.Disconnect.clicked.connect(self.Stop_read)
        self.timer=QTimer()
        self.timer.timeout.connect(self.start_read_thread)
    def Start_read(self):
        self.timer.start(1000)
    def Stop_read(self):
        self.timer.stop()
    def start_read_thread(self):
        self.qthread = ThreadTask()
        self.qthread.return_AMS_status.connect(self.set_text)
        self.qthread.return_v.connect(self.update_voltage)
        self.qthread.return_dis.connect(self.update_dis)
        self.qthread.return_temp.connect(self.update_temp)
        self.qthread.serial_read()
    def set_text(self,text):
        temp = text.replace(' ','\n')
        temp = temp.replace('_',' ')
        self.MainWindow.AMS_Status.setText(temp)
    def update_voltage(self,text):
        max = 0
        min = 0    
        for i in range(0,total_ic,1):
            for j in range(0,12,1):
                cell_v[i * 12 + j] = (float(text[86 * i + 7 * j:86 * i + 7 * j + 7]))
                if(cell_v[i * 12 + j] > cell_v[max]):
                    max = i * 12 + j
                if(cell_v[i * 12 + j] < cell_v[min]):
                    min = i * 12 + j
        print(cell_v)
        for i in range(0,total_ic,1):
            for j in range(0,12,1):
                temp = self.findChild(QtWidgets.QProgressBar,'progressBar' + str(i * 12 + j))
                if(i * 12 + j == max):
                    temp.setStyleSheet("QProgressBar::chunk{background: rgb(255, 0, 0);}")
                elif(i * 12 + j == min):
                    temp.setStyleSheet("QProgressBar::chunk{background: rgb(0, 0, 255);}")
                else:
                    temp.setStyleSheet("QProgressBar::chunk{background: rgb(0, 255, 0);}")
                if(cell_v[i * 12 + j] < 4.20 and cell_v[i * 12 + j] > 2.50):
                    temp.setValue(int((cell_v[i * 12 + j] - 2.5)/1.7  * 100))
                else:
                    temp.setValue(0)
                tem_s = ''
                tem_s = str(cell_v[i * 12 + j])
                temp = self.findChild(QtWidgets.QLabel,'v' + str(i * 12 + j))
                temp.setText(tem_s[0:4] + 'v')
        self.MainWindow.Voltage_hilo.setText('voltage hi: ' + text[total_ic* 86:total_ic* 86 + 4] + 'v lo:' + text[total_ic* 86 + 7:total_ic* 86 + 11])
    def update_dis(self,text):
        for i in range(0,total_ic,1):
            for j in range(0,12,1):
                temp = self.findChild(QtWidgets.QLabel,'dis' + str(i * 12 + j))
                if(text[i * 14 + j] == '#'):
                    if(text[total_ic * i] == 1):
                        temp.setStyleSheet("background-color: rgb(0, 200, 0);")
                    else:
                        temp.setStyleSheet("background-color: rgb(0, 200, 255);")
                else:
                    temp.setStyleSheet("background-color: rgb(200, 200, 200);")
                    
    def update_temp(self,text):
        for i in range(0,total_ic,1):
            for j in range(0,16,1):
                temp = self.findChild(QtWidgets.QLabel,'temp' + str(i * 16 + j))
                temp.setText(text[114 * i + 7 * j:114 * i + 7 * j + 2] + 'deg')
        self.MainWindow.temp_hilo.setText('temp hi: ' + text[total_ic* 114:total_ic* 114 + 4] + 'deg')
                
class Setting_window(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(Setting_window, self).__init__()
        self.ui = Ui_Setting_window()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.enter_com)
        for i in range(1,32,1):
            self.ui.COM.addItem("COM" + str(i))
    def enter_com(self):
        global COM_port 
        COM_port = str(self.ui.COM.currentText())
        print(COM_port)

                

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
