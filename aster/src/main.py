import datetime
import logging
import sys
import time
from PyQt4 import QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


from PyQt4.QtCore import *
from PyQt4.QtGui import *

import HWWarmService
import MockWarmService
from DBService import DBService
import mainwindow_auto

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# global var for stopping the worker threads when the GUI exits
warm_service = ""
app_running = True


class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # main data structure
    def btnstate(self):
        if self.wheel_button.isChecked():
            self.wheel_button.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button.setText("Extract")
            warm_service.closeContact()

    def btnstate_2(self):
        if self.wheel_button_2.isChecked():
            self.wheel_button_2.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_2.setText("Extract")
            print("Closing wheel")

    def btnstate_3(self):
        if self.wheel_button_3.isChecked():
            self.wheel_button_3.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_3.setText("Extract")
            warm_service.closeContact()

    def btnstate_4(self):
        if self.wheel_button_4.isChecked():
            self.wheel_button_4.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_4.setText("Extract")
            warm_service.closeContact()

    def btnstate_5(self):
        if self.wheel_button_5.isChecked():
            self.wheel_button_5.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_5.setText("Extract")
            warm_service.closeContact()

    def btnstate_6(self):
        if self.wheel_button_6.isChecked():
            self.wheel_button_6.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_6.setText("Extract")
            warm_service.closeContact()

    def btnstate_7(self):
        if self.wheel_button_7.isChecked():
            self.wheel_button_7.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_7.setText("Extract")
            warm_service.closeContact()

    def btnstate_8(self):
        if self.wheel_button_8.isChecked():
            self.wheel_button_8.setText("Retract")
            warm_service.openContact()
        else:
            self.wheel_button_8.setText("Extract")
            warm_service.closeContact()

    def tabSelected(self, arg=None):
        print '\n\t tabSelected() current Tab index =', arg

    def whatTab(self):
        currentIndex = self.tabWidget.currentIndex()
        currentWidget = self.tabWidget.currentWidget()

        print '\n\t Query: current Tab index =', currentIndex

    def un_click(self):
        if self.btn_close.isChecked():
            self.graphicsView_1_t.move(420, 40)
            self.graphicsView_1_t.resize(331, 91)
            self.graphicsView_1_t.show()
            self.btn_close.hide()
            print "ZOOM out"

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget.connect(self.tabWidget, SIGNAL("currentChanged(int)"), self.tabSelected)
        self.dbService = DBService()

        self.btn_close = QtGui.QPushButton("X", self)
        self.btn_close.move(0, 0)
        self.btn_close.setFixedSize(20, 20)
        self.btn_close.hide()

        #self.hbox = QtGui.QVBoxLayout()
        #self.hbox.addWidget(self.graphicsView_1)
        #self.hbox.addWidget(self.btn_close)

        self.xData = []
        self.yData = []

        #self.graphicsView_1 = pg.PlotWidget(self)
        self.graphicsView_1_t.mouseReleaseEvent= self.click
        #self.graphicsView_1.mousePressEvent= self.un_click


        pg.setConfigOptions(antialias=True)
        # self.graphicsView_1.setYRange(1, 5, 0.1)
        self.graphicsView_1_t.setMouseTracking(True)
        self.graphicsView_1_t.setBackground(None)
        self.graphicsView_1_t.setMouseEnabled(x=True, y=False)
        #self.graphicsView_1_t.setLabel('left', 'CO2')
        #self.graphicsView_1_t.setLabel('bottom', 'h')
        self.graphicsView_1_t.plotItem.showGrid(True, True, 0.7)

        self.graphicsView_1_c.setMouseTracking(True)
        self.graphicsView_1_c.setBackground(None)
        self.graphicsView_1_c.setMouseEnabled(x=True, y=False)
        # self.graphicsView_1_t.setLabel('left', 'CO2')
        # self.graphicsView_1_t.setLabel('bottom', 'h')
        self.graphicsView_1_c.plotItem.showGrid(True, True, 0.7)

        # GPIO adding event

        # GPIO.add_event_detect(12, GPIO.FALLING)
        # GPIO.add_event_detect(16, GPIO.FALLING)
        # GPIO.add_event_detect(20, GPIO.FALLING)
        # GPIO.add_event_detect(21, GPIO.FALLING)
        # GPIO.add_event_detect(18, GPIO.FALLING)
        # GPIO.add_event_detect(23, GPIO.FALLING)
        # GPIO.add_event_detect(24, GPIO.FALLING)
        # GPIO.add_event_detect(25, GPIO.FALLING)

        # buttons\

        #self.connect(self.graphicsView_1, SIGNAL('clicked()'), self.click)

        #self.graphicsView_1.setMouseTracking(True)

        self.btn_close.setCheckable(True)
        self.btn_close.clicked.connect(lambda: self.un_click())

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

        # grafici sliki
        # label_153= QLabel()
        pixmap = QPixmap('/home/aleksandra/workspace/aster/aster_gui/splash.png')
        self.label_153.setPixmap(pixmap)


        # Timer
        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.update_label)
        self._update_timer.timeout.connect(self.plot)
        # vrati
        # self._update_timer.timeout.connect(self.set_tab)
        # self._update_timer.timeout.connect(self.insert_data)
        self._update_timer.start(1000)  # millisec

    def click(self,event):
        print "IN"
        self.graphicsView_1_t.move(00, 00)
        self.graphicsView_1_t.resize(800, 400)
        self.btn_close.move(780, 20)
        self.btn_close.show()
        self.btn_close.setStyleSheet("background-color: red")
        #self.graphicsView_1().show()
        print "zoom in"



    def plot(self):


        #self.y = []
        #y = self.dbService.read_latest_box_data(1)[1]
        #x = np.arange(0.0, 50.0, 0.5)

        #self.cnt = 0
        #pg.mkQApp()
        #self.graphicsView_1 = pg.PlotWidget()
        #self.graphicsView_1.show()

        #self.graphicsView_1.p1 = self.graphicsView_1.plotItem
        #self.graphicsView_1.p2 = pg.ViewBox()
        #self.graphicsView_1.p1.showAxis('right')
        #self.graphicsView_1.p1.scene().addItem(self.graphicsView_1.p2)
        #self.graphicsView_1.p2.setGeometry(self.graphicsView_1.p1.vb.sceneBoundingRect())
        #self.graphicsView_1.p1.getAxis('right').linkToView(self.graphicsView_1.p2)
        #self.graphicsView_1.p2.setXLink(self.graphicsView_1.p1)

        #self.graphicsView_1.p1.plot(x)
        # time.sleep(1)
        #self.graphicsView_1.p2.addItem(self.graphicsView_1.p1.plot(y, pen='b'))
        # time.sleep(1)


        #self.plot = self.graphicsView_1.plot(title='Timed data')
        #self.curve = self.plot.plot()


        #numb = self.dbService.read_latest_box_data(1)[1]
        #self.xValues.append(x)
        #self.yValues.append(numb)

        numPoints = 50
        X = np.arange(numPoints)
        X = np.arange(0.0,50.0, 0.5)
        #Y= np.zeros(len(X), float)
        Y = np.sin(3.14159 * X * 10 / numPoints)

        # x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # y = self.dbService.read_latest_box_data(1)[1]


        C = pg.hsvColor(time.time() / 5 % 1, alpha=.5)
        pen = pg.mkPen(color=C, width=2)
        #Y=np.roll(Y,1)
        #self.data = deque()
        #self.plot = self.graphicsView_1.addPlot(title='Timed data')
        #self.curve = self.plot.plot()

        #self.data.append({'x':x, 'y': y})
        #self.xData.append(x)  # self.xData should be a list or deque
        #self.yData.append(y)  # self.yData should be a list or deque

        # Drawing the plot is now only performed once per update

        #self.graphicsView_1.setData(x=x, y=y)
        self.graphicsView_1_t.setInteractive(True)
        self.graphicsView_1_c.setInteractive(True)

        gr = self.graphicsView_1_t.plot(X, Y, pen=pen, clickable='True', clear='True')
        gr = self.graphicsView_1_c.plot(X, Y, pen=pen, clickable='True', clear='True')

        print "*******"
        print self.dbService.read_latest_box_data(1)[1]

 #------------------------------------------------------------------------------
        # def set_tab(self):
        # if GPIO.event_detected(23) and GPIO.input(23) == 0:
        # self.tabWidget.setCurrentIndex(0)
        # elif GPIO.event_detected(18) and GPIO.input(18) == 0:
        # self.tabWidget.setCurrentIndex(1)
        # elif GPIO.event_detected(21) and GPIO.input(21) == 0:
        # self.tabWidget.setCurrentIndex(2)
        # elif GPIO.event_detected(20) and GPIO.input(20) == 0:
        # self.tabWidget.setCurrentIndex(3)
        # elif GPIO.event_detected(16) and GPIO.input(16) == 0:
        # self.tabWidget.setCurrentIndex(4)
        # elif GPIO.event_detected(12) and GPIO.input(12) == 0:
        # self.tabWidget.setCurrentIndex(5)
        # elif GPIO.event_detected(25) and GPIO.input(25) == 0:
        # self.tabWidget.setCurrentIndex(6)
        # elif GPIO.event_detected(24) and GPIO.input(24) == 0:
        # self.tabWidget.setCurrentIndex(7)


    def update_label(self):
        logging.info('update_label')
        box_data_1 = self.dbService.read_latest_box_data(1)
        box_data_2 = self.dbService.read_latest_box_data(2)
        box_data_3 = self.dbService.read_latest_box_data(3)
        box_data_4 = self.dbService.read_latest_box_data(4)
        box_data_5 = self.dbService.read_latest_box_data(5)
        box_data_6 = self.dbService.read_latest_box_data(6)
        box_data_7 = self.dbService.read_latest_box_data(7)
        box_data_8 = self.dbService.read_latest_box_data(8)
        plate_data = self.dbService.read_latest_plate_data()

        # print socket.gethostbyname(socket.gethostname())

        self.label_27.setText(str(plate_data[1]))
        self.label_29.setText(str(plate_data[2]))
        self.label_43.setText(str(plate_data[1]))
        self.label_68.setText(str(plate_data[2]))
        self.label_105.setText(str(plate_data[1]))
        self.label_107.setText(str(plate_data[2]))
        self.label_111.setText(str(plate_data[1]))
        self.label_113.setText(str(plate_data[2]))
        self.label_117.setText(str(plate_data[1]))
        self.label_119.setText(str(plate_data[2]))
        self.label_123.setText(str(plate_data[1]))
        self.label_125.setText(str(plate_data[2]))
        self.label_129.setText(str(plate_data[1]))
        self.label_131.setText(str(plate_data[2]))
        self.label_135.setText(str(plate_data[1]))
        self.label_137.setText(str(plate_data[2]))
        self.label_25.setText(str(plate_data[3]))
        self.label_31.setText(str(plate_data[3]))
        self.label_109.setText(str(plate_data[3]))
        self.label_115.setText(str(plate_data[3]))
        self.label_121.setText(str(plate_data[3]))
        self.label_127.setText(str(plate_data[3]))
        self.label_133.setText(str(plate_data[3]))
        self.label_139.setText(str(plate_data[3]))
        # self.label_11.setText(str(t_1))
        self.label_11.setText(str(box_data_1[1]))
        self.label_12.setText(str(box_data_1[2]))
        self.label_79.setText(str(box_data_2[1]))
        self.label_82.setText(str(box_data_2[2]))
        self.label_20.setText(str(box_data_3[1]))
        self.label_142.setText(str(box_data_3[2]))
        self.label_35.setText(str(box_data_4[1]))
        self.label_144.setText(str(box_data_4[2]))
        self.label_50.setText(str(box_data_5[1]))
        self.label_146.setText(str(box_data_5[2]))
        self.label_61.setText(str(box_data_6[1]))
        self.label_148.setText(str(box_data_6[2]))
        self.label_87.setText(str(box_data_7[1]))
        self.label_150.setText(str(box_data_7[2]))
        self.label_98.setText(str(box_data_8[1]))
        self.label_152.setText(str(box_data_8[2]))
        # self.label_154.setText(str(IP))


# therefore does not provide signals and slots.
class WarmServiceRunnable(QtCore.QRunnable):
    def __init__(self, db_service, warmService):
        super(self.__class__, self).__init__()
        self.dbService = db_service
        self.warm_service = warmService

    def run(self):
        while app_running:
            # Read data from serial port using WarmsService
            t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8 = self.warm_service.ser_read()
            pres, flow = self.warm_service.analog_read()
            self.dbService.insert_box_data(datetime.datetime.now(), 1, t_1, c_1)
            self.dbService.insert_box_data(datetime.datetime.now(), 2, t_2, c_2)
            self.dbService.insert_box_data(datetime.datetime.now(), 3, t_3, c_3)
            self.dbService.insert_box_data(datetime.datetime.now(), 4, t_4, c_4)
            self.dbService.insert_box_data(datetime.datetime.now(), 5, t_5, c_5)
            self.dbService.insert_box_data(datetime.datetime.now(), 6, t_6, c_6)
            self.dbService.insert_box_data(datetime.datetime.now(), 7, t_7, c_7)
            self.dbService.insert_box_data(datetime.datetime.now(), 8, t_8, c_8)

            self.dbService.insert_plate_data(datetime.datetime.now(), t_plate, pres, flow)
            time.sleep(1)


def main():
    app = QApplication(sys.argv)
    form = MainWindow()

    # label_153.show()
    # form.setWindowFlags(Qt.FramelessWindowHint)
    # form.showFullScreen()
    form.show()
    app.processEvents()
    global warm_service
    user_input = "Dev"  # raw_input("Dev or Test:")
    if user_input == "Dev":
        warm_service = MockWarmService.MockWarmService()
    elif user_input == "Test":
        warm_service = HWWarmService.HWWarmService()

    runnable = WarmServiceRunnable(form.dbService, warm_service)
    QtCore.QThreadPool.globalInstance().start(runnable)

    exitval = app.exec_()
    # stop all workers
    # only in qt5 
    # QtCore.QThreadPool.globalInstance().cancel(runnable)
    global app_running
    app_running = False
    sys.exit(exitval)


if __name__ == "__main__":
    main()
