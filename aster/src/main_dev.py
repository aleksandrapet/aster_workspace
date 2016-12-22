import json
import logging
import sys
import time

import psycopg2
import self as self
import serial
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#import JSONserial
import JSONserial_dev
from aster_gui import mainwindow_auto


# global var for stopping the worker threads when the GUI exits

app_running = True
pres = 0
flo = 0
t_plate = 0
c_1 = 0
t_1 = 0
c_2 = 0
t_2 = 0
t_3 = 0
c_3 = 0
t_4 = 0
c_4 = 0
t_5 = 0
c_5 = 0
t_6 = 0
c_6 = 0
t_7 = 0
c_7 = 0
t_8 = 0
c_8 = 0

class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):

    def btnstate(self):
        if self.wheel_button.isChecked():
            self.wheel_button.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button.setText("Extract")
            print("Closing wheel")


    def btnstate_2(self):
        if self.wheel_button_2.isChecked():
            self.wheel_button_2.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_2.setText("Extract")
            print("Closing wheel")

    def btnstate_3(self):
        if self.wheel_button_3.isChecked():
            self.wheel_button_3.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_3.setText("Extract")
            print("Closing wheel")

    def btnstate_4(self):
        if self.wheel_button_4.isChecked():
            self.wheel_button_4.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_4.setText("Extract")
            print("Closing wheel")

    def btnstate_5(self):
        if self.wheel_button_5.isChecked():
            self.wheel_button_5.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_5.setText("Extract")
            print("Closing wheel")

    def btnstate_6(self):
        if self.wheel_button_6.isChecked():
            self.wheel_button_6.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_6.setText("Extract")
            print("Closing wheel")

    def btnstate_7(self):
        if self.wheel_button_7.isChecked():
            self.wheel_button_7.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_7.setText("Extract")
            print("Closing wheel")

    def btnstate_8(self):
        if self.wheel_button_8.isChecked():
            self.wheel_button_8.setText("Retract")
            print("Opening wheel")
        else:
            self.wheel_button_8.setText("Extract")
            print("Closing wheel")

    def tabSelected(self, arg=None):
        print '\n\t tabSelected() current Tab index =', arg


    def whatTab(self):
        currentIndex=self.tabWidget.currentIndex()
        currentWidget=self.tabWidget.currentWidget()
        print '\n\t Query: current Tab index =', currentIndex




    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget.connect(self.tabWidget, SIGNAL("currentChanged(int)"), self.tabSelected)


        #buttons

        self.wheel_button.setCheckable(True)
        self.wheel_button.clicked.connect(lambda: self.btnstate())

        self.wheel_button_2.setCheckable(True)
        self.wheel_button_2.clicked.connect(lambda: self.btnstate_2())

        self.wheel_button_3.setCheckable(True)
        self.wheel_button_3.clicked.connect(lambda: self.btnstate_3())

        self.wheel_button_4.setCheckable(True)
        self.wheel_button_4.clicked.connect(lambda: self.btnstate_4())

        self.wheel_button_5.setCheckable(True)
        self.wheel_button_5.clicked.connect(lambda: self.btnstate_5())

        self.wheel_button_6.setCheckable(True)
        self.wheel_button_6.clicked.connect(lambda: self.btnstate_6())

        self.wheel_button_7.setCheckable(True)
        self.wheel_button_7.clicked.connect(lambda: self.btnstate_7())

        self.wheel_button_8.setCheckable(True)
        self.wheel_button_8.clicked.connect(lambda: self.btnstate_8())


        #grafici

        #Timer
        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.update_label)
        #vrati
        #self._update_timer.timeout.connect(self.set_tab)
        self._update_timer.timeout.connect(self.insert_data)
        self._update_timer.start(1000) # milliseconds
    
    def insert_data(self):
        con = psycopg2.connect("dbname='pi' user='pi' host='localhost' password='raspberry'")
        cur=con.cursor()
        #T_time=time.time()
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        #t=t+1
        print t
        query = "INSERT INTO Data(T_plate, T_1, C_1, T_2, C_2, T_3, C_3, T_4, C_4, T_5, C_5, T_6, C_6, T_7, C_7, T_8, C_8, TIME) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8,t))
        logging.info('Inserting into base sucessfull')
        logging.warning('BAZA')
        con.commit()
        cur.close()
        con.close()


    def update_label(self):
        logging.info('update_label')
        #print socket.gethostbyname(socket.gethostname())
        self.label_27.setText(str(pres))
        self.label_29.setText(str(flo))
        self.label_43.setText(str(pres))
        self.label_68.setText(str(flo))
        self.label_105.setText(str(pres))
        self.label_107.setText(str(flo))
        self.label_111.setText(str(pres))
        self.label_113.setText(str(flo))
        self.label_117.setText(str(pres))
        self.label_119.setText(str(flo))
        self.label_123.setText(str(pres))
        self.label_125.setText(str(flo))
        self.label_129.setText(str(pres))
        self.label_131.setText(str(flo))
        self.label_135.setText(str(pres))
        self.label_137.setText(str(flo))
        self.label_25.setText(str(t_plate))
        self.label_31.setText(str(t_plate))
        self.label_109.setText(str(t_plate))
        self.label_115.setText(str(t_plate))
        self.label_121.setText(str(t_plate))
        self.label_127.setText(str(t_plate))
        self.label_133.setText(str(t_plate))
        self.label_139.setText(str(t_plate))
        self.label_11.setText(str(t_1))
        self.label_12.setText(str(c_1))
        self.label_79.setText(str(t_2))
        self.label_82.setText(str(c_2))
        self.label_20.setText(str(t_3))
        self.label_142.setText(str(c_3))
        self.label_35.setText(str(t_4))
        self.label_144.setText(str(c_4))
        self.label_50.setText(str(t_5))
        self.label_146.setText(str(c_5))
        self.label_61.setText(str(t_6))
        self.label_148.setText(str(c_6))
        self.label_87.setText(str(t_7))
        self.label_150.setText(str(c_7))
        self.label_98.setText(str(t_8))
        self.label_152.setText(str(c_8))
        #self.label_154.setText(str(IP))




# therefore does not provide signals and slots.
class Runnable(QtCore.QRunnable):


    def run(self):
        #global IP
        global pres
        pres = 0
        global flo
        flo = 0
        global t_plate
        t_plate = 0
        global t_1
        t_1 = 0
        global c_1
        c_1 = 0
        global t_2
        t_2 = 0
        global c_2
        c_2=0
        global t_3
        t_3 = 0
        global c_3
        c_3 = 0
        global t_4
        t_4 = 0
        global c_4
        c_4 = 0
        global t_5
        t_5 = 0
        global c_5
        c_5 = 0
        global t_6
        t_6 = 0
        global c_6
        c_6 = 0
        global t_7
        t_7 = 0
        global c_7
        c_7 = 0
        global t_8
        t_8 = 0
        global c_8
        c_8 = 0

        while app_running:
            #pres,flo=pfqt.onetime()
            t_plate,t_1,c_1,t_2,c_2,t_3,c_3,t_4,c_4,t_5,c_5,c_6,t_6,c_7,t_7,c_8,t_8=JSONserial_dev.ser_read()
            #IP = ip.ip_read()
            pres = pres+1 #citaj od seriska
            flo = flo+1  #citaj od seriska
   
def main():
    app = QApplication(sys.argv)
    form = MainWindow()

    
    #label_153.show()
    #form.setWindowFlags(Qt.FramelessWindowHint)
    #form.showFullScreen()
    form.show()
    
    runnable = Runnable()
    QtCore.QThreadPool.globalInstance().start(runnable)
    
    exitval = app.exec_()
    # stop all workers
    # only in qt5 
    # QtCore.QThreadPool.globalInstance().cancel(runnable)
    global app_running
    app_running = False
    sys.exit(exitval)

if __name__=="__main__":
    main()

