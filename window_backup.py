# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from qtpy import QtGui
import time
import cv2 as cv

import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import qdarkstyle

from yolo import YOLO


class Ui_MainWindow(object):
    ########yolo########
    args = {'image': True, 'input': None, 'output': None}
    my_yolo = YOLO(**args)
    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()
    ########yolo########
    mode1_activate = False
    mode2_activate = False
    vpause = False
    save_flag = True
    cap = None
    output_name = "test.avi"
    output_path = "./Violation Record/" + output_name
    _translate = QtCore.QCoreApplication.translate
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode1.setAutoDefault(False)
        self.Mode1.setDefault(False)
        self.Mode1.setFlat(False)
        self.Mode1.setObjectName("Mode1")
        self.horizontalLayout_2.addWidget(self.Mode1)
        self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode2.setObjectName("Mode2")
        self.horizontalLayout_2.addWidget(self.Mode2)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.verticalLayout_2.addWidget(self.Open)
        spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setObjectName("Status")
        self.verticalLayout_2.addWidget(self.Status)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.AllPeople = QtWidgets.QLabel(self.centralwidget)
        self.AllPeople.setObjectName("AllPeople")
        self.verticalLayout_2.addWidget(self.AllPeople)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.WithHM = QtWidgets.QLabel(self.centralwidget)
        self.WithHM.setObjectName("WithHM")
        self.verticalLayout_2.addWidget(self.WithHM)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.aa = QtWidgets.QLabel(self.centralwidget)
        self.aa.setObjectName("aa")
        self.verticalLayout_2.addWidget(self.aa)
        self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
        self.WithoutHM.setObjectName("WithoutHM")
        self.verticalLayout_2.addWidget(self.WithoutHM)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("label10")
        self.verticalLayout_2.addWidget(self.label10)
        self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
        self.UnusedHM.setObjectName("UnusedHM")
        self.verticalLayout_2.addWidget(self.UnusedHM)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ######################################################################################
        self.lcdNumber.setNumDigits(8)
        self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
        self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
        self.timer = QTimer()  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 设置定时间隔为1000ms即1s，并启动定时器

        #########################################################################################
        self.timer_camera = QtCore.QTimer()  # 初始化定时器
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################

        self.retranslateUi(MainWindow)
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Pause.clicked.connect(self.pause)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "Mode1"))
        self.Mode2.setText(_translate("MainWindow", "Mode2"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Open.setText(_translate("MainWindow", "View Record"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.Status.setText(_translate("MainWindow", "Default"))
        self.label_3.setText(_translate("MainWindow", "Detected People:"))
        self.AllPeople.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
        self.WithHM.setText(_translate("MainWindow", "0"))
        self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
        self.WithoutHM.setText(_translate("MainWindow", "0"))
        self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
        self.UnusedHM.setText(_translate("MainWindow", "0"))




###########################################
    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))


    def show_camera(self):
        # self.prev_time = time.time()

        ret, self.image = self.cap.read()

        ######yolo#########
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        result = np.asarray(self.image)
        self.curr_time = timer()
        self.exec_time = self.curr_time - self.prev_time
        self.prev_time = self.curr_time
        self.accum_time = self.accum_time + self.exec_time
        self.curr_fps = self.curr_fps + 1
        if self. accum_time > 1:
            self.accum_time = self.accum_time - 1
            self.fps = "FPS: " + str(self.curr_fps)
            self.curr_fps = 0

        # self.curr_time = time.time()
        # self.curr_fps = 1/(self.curr_time-self.prev_time)
        # self.fps = "FPS: " + str(curr_fps)

        cv.putText(result, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        # ######yolo#########

        #######Video Saver########
        if(self.save_flag == True):
            self.out.write(result)
        #######Video Saver########

        #print(self.image)
        #print(type(self.image))
        height, width, bytesPerComponent = result.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(result, cv.COLOR_BGR2RGB, result)
        img = QImage(result.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(img))




    def pause(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.vpause == False):
                self.timer_camera.stop()
                self.vpause = True
            elif (self.vpause == True):
                self.timer_camera.start(1)
                self.vpause = False
        pass

    def stop(self):
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False

        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        self.Status.setText(self._translate("MainWindow", "Default"))
        self.AllPeople.setText(self._translate("MainWindow", "0"))
        self.WithHM.setText(self._translate("MainWindow", "0"))
        self.WithoutHM.setText(self._translate("MainWindow", "0"))
        self.UnusedHM.setText(self._translate("MainWindow", "0"))
        ############################# reset label
        white = cv.imread("label1.jpg")
        height, width, bytesPerComponent = white.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(white, cv.COLOR_BGR2RGB, white)
        image = QImage(white.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setScaledContents(True)
        self.label.setPixmap(QPixmap.fromImage(image))
        ############################### release cap
        if (self.cap != None):
            self.cap.release()
        ########################################################
        ############close yolo##########
        #if(self.my_yolo != None):
        #    self.my_yolo.close_session()
        ############close yolo##########
        pass

    def exec_mode1(self):
        #if(self.mode1_activate == False and self.mode2_activate == False):
        #    main.fun2(self, 1)
        if (self.mode1_activate == False and self.mode2_activate == False):
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == False and self.mode2_activate == False):
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)

            self.mode2_activate = True
        pass


    def openfolder(self):
        foldername = "./Violation Record"
        os.system('xdg-open "%s"' % foldername)
        pass

    def videosaver(self):
        #Video Saver
        fps = self.cap.get(cv.CAP_PROP_FPS)
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)

###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui.setupUi(MainWindow)
    MainWindow.show()

    """init label"""
    white = cv.imread("label1.jpg")
    height, width, bytesPerComponent = white.shape
    bytesPerLine = bytesPerComponent * width
    cv.cvtColor(white, cv.COLOR_BGR2RGB, white)
    image = QImage(white.data, width, height, bytesPerLine, QImage.Format_RGB888)
    ui.label.setScaledContents(True)
    ui.label.setPixmap(QPixmap.fromImage(image))
    """"init label"""
    #ui.timer()

    sys.exit(app.exec_())













    ###############################################################################################################################################
    # -*- coding: utf-8 -*-

    # Form implementation generated from reading ui file 'mainwindow.ui'
    #
    # Created by: PyQt5 UI code generator 5.10.1
    #
    # WARNING! All changes made in this file will be lost!
    import os
    from timeit import default_timer as timer

    import numpy as np
    from PIL import Image, ImageFont, ImageDraw
    from PyQt5 import QtCore, QtWidgets
    from PyQt5.QtGui import QPixmap, QImage
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5.QtCore import QPoint
    from PyQt5.QtCore import QTimer
    from qtpy import QtGui
    import time
    import cv2 as cv

    import sys

    from PyQt5.QtGui import QImage, QPixmap
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
    import qdarkstyle

    from yolo import YOLO


    class Ui_MainWindow(object):

        def __init__(self, parent=None):
            super(Ui_MainWindow, self).__init__(parent)
            # self.cap = cv2.VideoCapture("test.mp4")
            self.timer_camera = QtCore.QTimer()  # 初始化定时器
            # self.cap = cv2.VideoCapture("test.mp4")  # 初始化摄像头
            self.CAM_NUM = 0
            self.set_ui()
            self.slot_init()
            self.__flag_work = 0
            self.x = 0
            self.count = 0

        ########yolo########
        img = None
        args = {'image': True, 'input': None, 'output': None}
        my_yolo = YOLO(**args)
        accum_time = 0
        curr_fps = 0
        fps = "FPS: ??"
        prev_time = timer()
        ########yolo########
        mode1_activate = False
        mode2_activate = False
        vpause = False
        save_flag = True
        cap = None
        output_name = "test.avi"
        output_path = "./Violation Record/" + output_name
        _translate = QtCore.QCoreApplication.translate

        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1008, 858)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout()
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.horizontalLayout_4.addItem(spacerItem)
            self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
            self.lcdNumber.setObjectName("lcdNumber")
            self.horizontalLayout_4.addWidget(self.lcdNumber)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.horizontalLayout_4.addItem(spacerItem1)
            self.horizontalLayout_4.setStretch(0, 10)
            self.horizontalLayout_4.setStretch(1, 1)
            self.horizontalLayout_4.setStretch(2, 10)
            self.verticalLayout_3.addLayout(self.horizontalLayout_4)
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setAutoFillBackground(False)
            self.label.setFrameShadow(QtWidgets.QFrame.Plain)
            self.label.setText("")
            self.label.setIndent(-1)
            self.label.setTextInteractionFlags(
                QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
            self.label.setObjectName("label")
            self.verticalLayout.addWidget(self.label)
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
            self.Mode1.setAutoDefault(False)
            self.Mode1.setDefault(False)
            self.Mode1.setFlat(False)
            self.Mode1.setObjectName("Mode1")
            self.horizontalLayout_2.addWidget(self.Mode1)
            self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
            self.Mode2.setObjectName("Mode2")
            self.horizontalLayout_2.addWidget(self.Mode2)
            self.Pause = QtWidgets.QPushButton(self.centralwidget)
            self.Pause.setObjectName("Pause")
            self.horizontalLayout_2.addWidget(self.Pause)
            self.Close = QtWidgets.QPushButton(self.centralwidget)
            self.Close.setObjectName("Close")
            self.horizontalLayout_2.addWidget(self.Close)
            self.verticalLayout.addLayout(self.horizontalLayout_2)
            self.verticalLayout.setStretch(0, 10)
            self.verticalLayout.setStretch(1, 1)
            self.horizontalLayout_3.addLayout(self.verticalLayout)
            self.verticalLayout_2 = QtWidgets.QVBoxLayout()
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.Open = QtWidgets.QPushButton(self.centralwidget)
            self.Open.setObjectName("Open")
            self.verticalLayout_2.addWidget(self.Open)
            spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem2)
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_2.addWidget(self.label_2)
            self.Status = QtWidgets.QLabel(self.centralwidget)
            self.Status.setObjectName("Status")
            self.verticalLayout_2.addWidget(self.Status)
            spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem3)
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setObjectName("label_3")
            self.verticalLayout_2.addWidget(self.label_3)
            self.AllPeople = QtWidgets.QLabel(self.centralwidget)
            self.AllPeople.setObjectName("AllPeople")
            self.verticalLayout_2.addWidget(self.AllPeople)
            spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem4)
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setObjectName("label_4")
            self.verticalLayout_2.addWidget(self.label_4)
            self.WithHM = QtWidgets.QLabel(self.centralwidget)
            self.WithHM.setObjectName("WithHM")
            self.verticalLayout_2.addWidget(self.WithHM)
            spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem5)
            self.aa = QtWidgets.QLabel(self.centralwidget)
            self.aa.setObjectName("aa")
            self.verticalLayout_2.addWidget(self.aa)
            self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
            self.WithoutHM.setObjectName("WithoutHM")
            self.verticalLayout_2.addWidget(self.WithoutHM)
            spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem6)
            self.label10 = QtWidgets.QLabel(self.centralwidget)
            self.label10.setObjectName("label10")
            self.verticalLayout_2.addWidget(self.label10)
            self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
            self.UnusedHM.setObjectName("UnusedHM")
            self.verticalLayout_2.addWidget(self.UnusedHM)
            spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem7)
            spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem8)
            self.horizontalLayout_3.addLayout(self.verticalLayout_2)
            self.horizontalLayout_3.setStretch(0, 10)
            self.horizontalLayout_3.setStretch(1, 2)
            self.verticalLayout_3.addLayout(self.horizontalLayout_3)
            spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_3.addItem(spacerItem9)
            self.verticalLayout_3.setStretch(0, 1)
            self.verticalLayout_3.setStretch(1, 30)
            self.verticalLayout_3.setStretch(2, 1)
            self.horizontalLayout.addLayout(self.verticalLayout_3)
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            ######################################################################################
            self.lcdNumber.setNumDigits(24)
            self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
            self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
            self.timer = QTimer()  # 新建一个定时器
            # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)  # 设置定时间隔为1000ms即1s，并启动定时器

            #########################################################################################
            self.timer_camera = QtCore.QTimer()  # 初始化定时器
            self.timer_camera.timeout.connect(self.show_camera)
            ########################################################################################

            self.retranslateUi(MainWindow)
            self.Mode1.clicked.connect(self.exec_mode1)
            self.Mode2.clicked.connect(self.exec_mode2)
            self.Pause.clicked.connect(self.pause)
            self.Close.clicked.connect(self.stop)
            self.Open.clicked.connect(self.openfolder)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
            self.Mode1.setText(_translate("MainWindow", "Mode1"))
            self.Mode2.setText(_translate("MainWindow", "Mode2"))
            self.Pause.setText(_translate("MainWindow", "Pause"))
            self.Close.setText(_translate("MainWindow", "Close"))
            self.Open.setText(_translate("MainWindow", "View Record"))
            self.label_2.setText(_translate("MainWindow", "Status:"))
            self.Status.setText(_translate("MainWindow", "Default"))
            self.label_3.setText(_translate("MainWindow", "Detected People:"))
            self.AllPeople.setText(_translate("MainWindow", "0"))
            self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
            self.WithHM.setText(_translate("MainWindow", "0"))
            self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
            self.WithoutHM.setText(_translate("MainWindow", "0"))
            self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
            self.UnusedHM.setText(_translate("MainWindow", "0"))

        ###########################################
        def update_time(self):
            self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
            # self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))

        def show_camera(self):
            ret, self.image = self.cap.read()

            ######yolo#########
            self.image = Image.fromarray(self.image)
            self.image = self.my_yolo.detect_image(self.image)
            self.img = np.asarray(self.image)
            self.curr_time = timer()
            self.exec_time = self.curr_time - self.prev_time
            self.prev_time = self.curr_time
            self.accum_time = self.accum_time + self.exec_time
            self.curr_fps = self.curr_fps + 1
            if self.accum_time > 1:
                self.accum_time = self.accum_time - 1
                self.fps = "FPS: " + str(self.curr_fps)
                self.curr_fps = 0

            cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                       fontScale=0.50, color=(255, 0, 0), thickness=2)
            # ######yolo#########

            #######Video Saver########
            if (self.save_flag == True):
                self.out.write(self.img)
            #######Video Saver########

            self.label_show()

        def pause(self):
            if (self.mode1_activate == True or self.mode2_activate == True):
                if (self.vpause == False):
                    self.timer_camera.stop()
                    self.vpause = True
                elif (self.vpause == True):
                    self.timer_camera.start(1)
                    self.vpause = False
            pass

        def stop(self):
            self.mode1_activate = False
            self.mode2_activate = False
            self.vpause = False

            self.timer_camera.stop()
            ####################### Exit #######################
            # if(type(out) == "cv2.VideoWriter"):
            #    out.release()
            self.Status.setText(self._translate("MainWindow", "Default"))
            self.AllPeople.setText(self._translate("MainWindow", "0"))
            self.WithHM.setText(self._translate("MainWindow", "0"))
            self.WithoutHM.setText(self._translate("MainWindow", "0"))
            self.UnusedHM.setText(self._translate("MainWindow", "0"))
            ########### reset label ########
            self.img = cv.imread("label1.jpg")
            self.label_show()
            ########### reset label ########
            ########### release cap ##############
            if (self.cap != None):
                self.cap.release()
            ########### release cap ##############
            ############close yolo##########
            # if(self.my_yolo != None):
            #    self.my_yolo.close_session()
            ############close yolo##########
            pass

        def exec_mode1(self):
            # if(self.mode1_activate == False and self.mode2_activate == False):
            #    main.fun2(self, 1)
            if (self.mode1_activate == False and self.mode2_activate == False):
                self.cap = cv.VideoCapture(0)
                self.videosaver()
                self.timer_camera.start(1)

                self.mode1_activate = True
            pass

        def exec_mode2(self):
            if (self.mode1_activate == False and self.mode2_activate == False):
                openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4)')  # return QString
                if (len(openfile_name[0]) != 0):
                    self.cap = cv.VideoCapture(openfile_name[0])
                    self.videosaver()
                    self.timer_camera.start(1)

                self.mode2_activate = True
            pass

        def openfolder(self):
            foldername = "./Violation Record"
            os.system('xdg-open "%s"' % foldername)
            pass

        def videosaver(self):
            fps = self.cap.get(cv.CAP_PROP_FPS)
            size = (int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
            fourcc = cv.VideoWriter_fourcc(*'XVID')
            # out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
            self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)

        def label_show(self):
            height, width, bytesPerComponent = self.img.shape
            bytesPerLine = bytesPerComponent * width
            cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
            image = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setScaledContents(True)  ##??????
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))


    ###################################### video #########################################
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        ui.setupUi(MainWindow)
        MainWindow.show()

        """init label"""
        white = cv.imread("label1.jpg")
        height, width, bytesPerComponent = white.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(white, cv.COLOR_BGR2RGB, white)
        image = QImage(white.data, width, height, bytesPerLine, QImage.Format_RGB888)
        ui.label.setScaledContents(True)
        ui.label.setPixmap(QPixmap.fromImage(image))
        """"init label"""
        # ui.timer()

        sys.exit(app.exec_())

##########################################################################################################################
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from qtpy import QtGui
import time
import cv2 as cv

import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import qdarkstyle

from yolo import YOLO


class Ui_MainWindow(object):

    def __init__(self, object):
        object.setObjectName("MainWindow")
        object.resize(1008, 858)
        self.centralwidget = QtWidgets.QWidget(object)
        self.setupUi()
        ######################################################################################
        self.lcdNumber.setNumDigits(24)
        self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
        self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
        self.timer = QTimer()  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 设置定时间隔为1000ms即1s，并启动定时器
        #########################################################################################
        self.timer_camera = QtCore.QTimer()  # 初始化定时器
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################
        ########yolo########
        self.img = None
        args = {'image': True, 'input': None, 'output': None}
        self.my_yolo = YOLO(**args)
        self.accum_time = 0
        self.curr_fps = 0
        self.fps = "FPS: ??"
        self.prev_time = timer()
        ########yolo########
        self.mode1_activate = False
        self.mode2_activate = False
        self. vpause = False
        self.save_flag = True
        self.cap = None
        self.output_name = "test.avi"
        self.output_path = "./Violation Record/" + self.output_name
        self._translate = QtCore.QCoreApplication.translate
        self.init_label()
        self.interrupt_flag = False



    def setupUi(self):
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode1.setAutoDefault(False)
        self.Mode1.setDefault(False)
        self.Mode1.setFlat(False)
        self.Mode1.setObjectName("Mode1")
        self.horizontalLayout_2.addWidget(self.Mode1)
        self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode2.setObjectName("Mode2")
        self.horizontalLayout_2.addWidget(self.Mode2)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.verticalLayout_2.addWidget(self.Open)
        spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setObjectName("Status")
        self.verticalLayout_2.addWidget(self.Status)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.AllPeople = QtWidgets.QLabel(self.centralwidget)
        self.AllPeople.setObjectName("AllPeople")
        self.verticalLayout_2.addWidget(self.AllPeople)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.WithHM = QtWidgets.QLabel(self.centralwidget)
        self.WithHM.setObjectName("WithHM")
        self.verticalLayout_2.addWidget(self.WithHM)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.aa = QtWidgets.QLabel(self.centralwidget)
        self.aa.setObjectName("aa")
        self.verticalLayout_2.addWidget(self.aa)
        self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
        self.WithoutHM.setObjectName("WithoutHM")
        self.verticalLayout_2.addWidget(self.WithoutHM)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("label10")
        self.verticalLayout_2.addWidget(self.label10)
        self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
        self.UnusedHM.setObjectName("UnusedHM")
        self.verticalLayout_2.addWidget(self.UnusedHM)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Pause.clicked.connect(self.pause)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "Mode1"))
        self.Mode2.setText(_translate("MainWindow", "Mode2"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Open.setText(_translate("MainWindow", "View Record"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.Status.setText(_translate("MainWindow", "Default"))
        self.label_3.setText(_translate("MainWindow", "Detected People:"))
        self.AllPeople.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
        self.WithHM.setText(_translate("MainWindow", "0"))
        self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
        self.WithoutHM.setText(_translate("MainWindow", "0"))
        self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
        self.UnusedHM.setText(_translate("MainWindow", "0"))


###########################################
    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
        #self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))


    def show_camera(self):
        ret, self.image = self.cap.read()

        ######yolo#########
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.img = np.asarray(self.image)
        self.curr_time = timer()
        self.exec_time = self.curr_time - self.prev_time
        self.prev_time = self.curr_time
        self.accum_time = self.accum_time + self.exec_time
        self.curr_fps = self.curr_fps + 1
        if self. accum_time > 1:
            self.accum_time = self.accum_time - 1
            self.fps = "FPS: " + str(self.curr_fps)
            self.curr_fps = 0

        cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        # ######yolo#########

        #######Video Saver########
        if(self.save_flag == True):
            self.out.write(self.img)
        #######Video Saver########

        self.label_show()




    def pause(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.vpause == False):
                self.timer_camera.stop()
                self.vpause = True
            elif (self.vpause == True):
                self.timer_camera.start(1)
                self.vpause = False
        pass

    def stop(self):
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False

        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        self.Status.setText(self._translate("MainWindow", "Default"))
        self.AllPeople.setText(self._translate("MainWindow", "0"))
        self.WithHM.setText(self._translate("MainWindow", "0"))
        self.WithoutHM.setText(self._translate("MainWindow", "0"))
        self.UnusedHM.setText(self._translate("MainWindow", "0"))
        ########### reset label ########
        self.init_label()
        ########### reset label ########
        ########### release cap ##############
        if (self.cap != None):
            self.cap.release()
        ########### release cap ##############
        ############close yolo##########
        #if(self.my_yolo != None):
        #    self.my_yolo.close_session()
        ############close yolo##########
        pass

    def exec_mode1(self):
        #if(self.mode1_activate == False and self.mode2_activate == False):
        #    main.fun2(self, 1)
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)

            self.mode2_activate = True
        pass


    def openfolder(self):
        foldername = "./Violation Record"
        os.system('xdg-open "%s"' % foldername)
        pass


    def videosaver(self):
        fps = self.cap.get(cv.CAP_PROP_FPS)
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)


    def label_show(self):
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
        image = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setScaledContents(True)##??????
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def init_label(self):
        self.img = cv.imread("label1.jpg")
        self.label_show()

    def interrupt(self):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'终止', u'将终止当前模式！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            pass
        else:
            self.stop()
            self.mode1_activate = False
            self.mode2_activate = False
            #event.accept()
            pass

###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())





















    # -*- coding: utf-8 -*-

    # Form implementation generated from reading ui file 'mainwindow.ui'
    #
    # Created by: PyQt5 UI code generator 5.10.1
    #
    # WARNING! All changes made in this file will be lost!
    import os
    from timeit import default_timer as timer

    import numpy as np
    from PIL import Image, ImageFont, ImageDraw
    from PyQt5 import QtCore, QtWidgets
    from PyQt5.QtGui import QPixmap, QImage
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5.QtCore import QPoint
    from PyQt5.QtCore import QTimer
    from qtpy import QtGui
    import time
    import cv2 as cv

    import sys

    from PyQt5.QtGui import QImage, QPixmap
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
    import qdarkstyle

    from yolo import YOLO


    class Ui_MainWindow(object):

        def __init__(self, object):
            object.setObjectName("MainWindow")
            object.resize(1008, 858)
            self.centralwidget = QtWidgets.QWidget(object)
            self.setupUi()
            ######################################################################################
            self.lcdNumber.setNumDigits(24)
            self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
            self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
            self.timer = QTimer()  # 新建一个定时器
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)
            #########################################################################################
            self.timer_camera = QtCore.QTimer()
            self.timer_camera.timeout.connect(self.show_camera)
            ########################################################################################
            ########yolo########
            self.img = None
            args = {'image': True, 'input': None, 'output': None}
            self.my_yolo = YOLO(**args)
            self.accum_time = 0
            self.curr_fps = 0
            self.fps = "FPS: ??"
            self.prev_time = timer()
            ########yolo########
            self.mode1_activate = False
            self.mode2_activate = False
            self.vpause = False
            self.save_flag = True
            self.cap = None
            self.output_name = "test.avi"  # 输出文件名
            self.output_path = "./Violation Record/" + self.output_name  # 输出路径
            self._translate = QtCore.QCoreApplication.translate  # 文本
            self.init_label()
            self.interrupt_flag = False  # 中断标志
            self.foldername = "./Violation Record"  # 录像文件夹

        def setupUi(self):
            self.centralwidget.setObjectName("centralwidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout()
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.horizontalLayout_4.addItem(spacerItem)
            self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
            self.lcdNumber.setObjectName("lcdNumber")
            self.horizontalLayout_4.addWidget(self.lcdNumber)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.horizontalLayout_4.addItem(spacerItem1)
            self.horizontalLayout_4.setStretch(0, 10)
            self.horizontalLayout_4.setStretch(1, 1)
            self.horizontalLayout_4.setStretch(2, 10)
            self.verticalLayout_3.addLayout(self.horizontalLayout_4)
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setAutoFillBackground(False)
            self.label.setFrameShadow(QtWidgets.QFrame.Plain)
            self.label.setText("")
            self.label.setIndent(-1)
            self.label.setTextInteractionFlags(
                QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
            self.label.setObjectName("label")
            self.verticalLayout.addWidget(self.label)
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
            self.Mode1.setAutoDefault(False)
            self.Mode1.setDefault(False)
            self.Mode1.setFlat(False)
            self.Mode1.setObjectName("Mode1")
            self.horizontalLayout_2.addWidget(self.Mode1)
            self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
            self.Mode2.setObjectName("Mode2")
            self.horizontalLayout_2.addWidget(self.Mode2)
            self.Pause = QtWidgets.QPushButton(self.centralwidget)
            self.Pause.setObjectName("Pause")
            self.horizontalLayout_2.addWidget(self.Pause)
            self.Close = QtWidgets.QPushButton(self.centralwidget)
            self.Close.setObjectName("Close")
            self.horizontalLayout_2.addWidget(self.Close)
            self.verticalLayout.addLayout(self.horizontalLayout_2)
            self.verticalLayout.setStretch(0, 10)
            self.verticalLayout.setStretch(1, 1)
            self.horizontalLayout_3.addLayout(self.verticalLayout)
            self.verticalLayout_2 = QtWidgets.QVBoxLayout()
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.Open = QtWidgets.QPushButton(self.centralwidget)
            self.Open.setObjectName("Open")
            self.verticalLayout_2.addWidget(self.Open)
            spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem2)
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_2.addWidget(self.label_2)
            self.Status = QtWidgets.QLabel(self.centralwidget)
            self.Status.setObjectName("Status")
            self.verticalLayout_2.addWidget(self.Status)
            spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem3)
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setObjectName("label_3")
            self.verticalLayout_2.addWidget(self.label_3)
            self.AllPeople = QtWidgets.QLabel(self.centralwidget)
            self.AllPeople.setObjectName("AllPeople")
            self.verticalLayout_2.addWidget(self.AllPeople)
            spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem4)
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setObjectName("label_4")
            self.verticalLayout_2.addWidget(self.label_4)
            self.WithHM = QtWidgets.QLabel(self.centralwidget)
            self.WithHM.setObjectName("WithHM")
            self.verticalLayout_2.addWidget(self.WithHM)
            spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem5)
            self.aa = QtWidgets.QLabel(self.centralwidget)
            self.aa.setObjectName("aa")
            self.verticalLayout_2.addWidget(self.aa)
            self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
            self.WithoutHM.setObjectName("WithoutHM")
            self.verticalLayout_2.addWidget(self.WithoutHM)
            spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem6)
            self.label10 = QtWidgets.QLabel(self.centralwidget)
            self.label10.setObjectName("label10")
            self.verticalLayout_2.addWidget(self.label10)
            self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
            self.UnusedHM.setObjectName("UnusedHM")
            self.verticalLayout_2.addWidget(self.UnusedHM)
            spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem7)
            spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_2.addItem(spacerItem8)
            self.horizontalLayout_3.addLayout(self.verticalLayout_2)
            self.horizontalLayout_3.setStretch(0, 10)
            self.horizontalLayout_3.setStretch(1, 2)
            self.verticalLayout_3.addLayout(self.horizontalLayout_3)
            spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_3.addItem(spacerItem9)
            self.verticalLayout_3.setStretch(0, 1)
            self.verticalLayout_3.setStretch(1, 30)
            self.verticalLayout_3.setStretch(2, 1)
            self.horizontalLayout.addLayout(self.verticalLayout_3)
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            self.Mode1.clicked.connect(self.exec_mode1)
            self.Mode2.clicked.connect(self.exec_mode2)
            self.Pause.clicked.connect(self.pause)
            self.Close.clicked.connect(self.stop)
            self.Open.clicked.connect(self.openfolder)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
            self.Mode1.setText(_translate("MainWindow", "Mode1"))
            self.Mode2.setText(_translate("MainWindow", "Mode2"))
            self.Pause.setText(_translate("MainWindow", "Pause"))
            self.Close.setText(_translate("MainWindow", "Close"))
            self.Open.setText(_translate("MainWindow", "View Record"))
            self.label_2.setText(_translate("MainWindow", "Status:"))
            self.Status.setText(_translate("MainWindow", "Default"))
            self.label_3.setText(_translate("MainWindow", "Detected People:"))
            self.AllPeople.setText(_translate("MainWindow", "0"))
            self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
            self.WithHM.setText(_translate("MainWindow", "0"))
            self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
            self.WithoutHM.setText(_translate("MainWindow", "0"))
            self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
            self.UnusedHM.setText(_translate("MainWindow", "0"))

        ###########################################
        def update_time(self):
            self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
            # self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))

        def show_camera(self):
            ret, self.image = self.cap.read()
            ######yolo detect########
            self.image = Image.fromarray(self.image)
            self.image = self.my_yolo.detect_image(self.image)
            self.img = np.asarray(self.image)
            self.curr_time = timer()
            self.exec_time = self.curr_time - self.prev_time
            self.prev_time = self.curr_time
            self.accum_time = self.accum_time + self.exec_time
            self.curr_fps = self.curr_fps + 1
            if self.accum_time > 1:
                self.accum_time = self.accum_time - 1
                self.fps = "FPS: " + str(self.curr_fps)
                self.curr_fps = 0
            cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                       fontScale=0.50, color=(255, 0, 0), thickness=2)
            ######yolo detect########

            #######Video Saver########
            if (self.save_flag == True):
                self.out.write(self.img)
            #######Video Saver########

            #######show label#########
            self.label_show()
            #######show label#########

        def pause(self):
            if (self.mode1_activate == True or self.mode2_activate == True):
                if (self.vpause == False):
                    self.timer_camera.stop()
                    self.vpause = True
                elif (self.vpause == True):
                    self.timer_camera.start(1)
                    self.vpause = False
            pass

        def stop(self):
            self.mode1_activate = False
            self.mode2_activate = False
            self.vpause = False

            self.timer_camera.stop()
            ####################### Exit #######################
            # if(type(out) == "cv2.VideoWriter"):
            #    out.release()
            self.Status.setText(self._translate("MainWindow", "Default"))
            self.AllPeople.setText(self._translate("MainWindow", "0"))
            self.WithHM.setText(self._translate("MainWindow", "0"))
            self.WithoutHM.setText(self._translate("MainWindow", "0"))
            self.UnusedHM.setText(self._translate("MainWindow", "0"))
            ########### reset label ########
            self.init_label()
            ########### reset label ########
            ########### release cap ##############
            if (self.cap != None):
                self.cap.release()
            ########### release cap ##############
            ############close yolo##########
            # if(self.my_yolo != None):
            #    self.my_yolo.close_session()
            ############close yolo##########
            pass

        def exec_mode1(self):
            # if(self.mode1_activate == False and self.mode2_activate == False):
            #    main.fun2(self, 1)
            if (self.mode1_activate == True or self.mode2_activate == True):
                self.interrupt()
            if (self.mode1_activate == False and self.mode2_activate == False):
                self.cap = cv.VideoCapture(0)
                self.videosaver()
                self.timer_camera.start(1)

                self.mode1_activate = True
            pass

        def exec_mode2(self):
            if (self.mode1_activate == True or self.mode2_activate == True):
                self.interrupt()
            if (self.mode1_activate == False and self.mode2_activate == False):
                openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4)')  # return QString
                if (len(openfile_name[0]) != 0):
                    self.cap = cv.VideoCapture(openfile_name[0])
                    self.videosaver()
                    self.timer_camera.start(1)

                self.mode2_activate = True
            pass

        def openfolder(self):
            os.system('xdg-open "%s"' % self.foldername)
            pass

        def videosaver(self):
            fps = self.cap.get(cv.CAP_PROP_FPS)
            size = (int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
            fourcc = cv.VideoWriter_fourcc(*'XVID')
            # out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
            self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)

        def label_show(self):
            height, width, bytesPerComponent = self.img.shape
            bytesPerLine = bytesPerComponent * width
            cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
            image = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setScaledContents(True)  ##??????
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

        def init_label(self):
            self.img = cv.imread("label1.jpg")
            self.label_show()

        def interrupt(self):
            ok = QtWidgets.QPushButton()
            cancel = QtWidgets.QPushButton()
            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'终止', u'将终止当前模式！')
            msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
            msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
            ok.setText(u'确定')
            cancel.setText(u'取消')
            if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
                pass
            else:
                self.stop()
                self.mode1_activate = False
                self.mode2_activate = False
                # event.accept()
                pass


    ###################################### video #########################################
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow(MainWindow)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow.show()
        sys.exit(app.exec_())

























































































# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from qtpy import QtGui
import time
import cv2 as cv

import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import qdarkstyle

from yolo import YOLO


class Ui_MainWindow(object):

    def __init__(self, object):
        self.setupUi(object)
        ######################################################################################
        self.lcdNumber.setNumDigits(24)
        self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
        self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
        self.timer = QTimer()  # 新建一个定时器
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        #########################################################################################
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################
        ########yolo########
        self.img = None
        args = {'image': True, 'input': None, 'output': None}
        self.my_yolo = YOLO(**args)
        self.accum_time = 0
        self.curr_fps = 0
        self.fps = "FPS: ??"
        self.prev_time = timer()
        ########yolo########
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False
        self.save_flag = True
        self.cap = None
        self.output_name = "test.avi"                                  #输出文件名
        self.output_path = "./Violation Record/" + self.output_name    #输出路径
        self._translate = QtCore.QCoreApplication.translate       #文本
        self.init_label()
        self.interrupt_flag = False            #中断标志
        self.foldername = "./Violation Record" #录像文件夹

    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 858)
        self.centralwidget = QtWidgets.QWidget(object)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode1.setAutoDefault(False)
        self.Mode1.setDefault(False)
        self.Mode1.setFlat(False)
        self.Mode1.setObjectName("Mode1")
        self.horizontalLayout_2.addWidget(self.Mode1)
        self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode2.setObjectName("Mode2")
        self.horizontalLayout_2.addWidget(self.Mode2)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.verticalLayout_2.addWidget(self.Open)
        spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setObjectName("Status")
        self.verticalLayout_2.addWidget(self.Status)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.AllPeople = QtWidgets.QLabel(self.centralwidget)
        self.AllPeople.setObjectName("AllPeople")
        self.verticalLayout_2.addWidget(self.AllPeople)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.WithHM = QtWidgets.QLabel(self.centralwidget)
        self.WithHM.setObjectName("WithHM")
        self.verticalLayout_2.addWidget(self.WithHM)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.aa = QtWidgets.QLabel(self.centralwidget)
        self.aa.setObjectName("aa")
        self.verticalLayout_2.addWidget(self.aa)
        self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
        self.WithoutHM.setObjectName("WithoutHM")
        self.verticalLayout_2.addWidget(self.WithoutHM)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("label10")
        self.verticalLayout_2.addWidget(self.label10)
        self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
        self.UnusedHM.setObjectName("UnusedHM")
        self.verticalLayout_2.addWidget(self.UnusedHM)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Pause.clicked.connect(self.pause)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "Mode1"))
        self.Mode2.setText(_translate("MainWindow", "Mode2"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Open.setText(_translate("MainWindow", "View Record"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.Status.setText(_translate("MainWindow", "Default"))
        self.label_3.setText(_translate("MainWindow", "Detected People:"))
        self.AllPeople.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
        self.WithHM.setText(_translate("MainWindow", "0"))
        self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
        self.WithoutHM.setText(_translate("MainWindow", "0"))
        self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
        self.UnusedHM.setText(_translate("MainWindow", "0"))


###########################################
    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
        #self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))


    def show_camera(self):
        ret, self.image = self.cap.read()
        ######yolo detect########
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.img = np.asarray(self.image)
        self.curr_time = timer()
        self.exec_time = self.curr_time - self.prev_time
        self.prev_time = self.curr_time
        self.accum_time = self.accum_time + self.exec_time
        self.curr_fps = self.curr_fps + 1
        if self. accum_time > 1:
            self.accum_time = self.accum_time - 1
            self.fps = "FPS: " + str(self.curr_fps)
            self.curr_fps = 0
        cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        ######yolo detect########

        #######Video Saver########
        if(self.save_flag == True):
            self.out.write(self.img)
        #######Video Saver########

        #######show label#########
        self.label_show()
        #######show label#########




    def pause(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.vpause == False):
                self.timer_camera.stop()
                self.vpause = True
            elif (self.vpause == True):
                self.timer_camera.start(1)
                self.vpause = False
        pass

    def stop(self):
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False

        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        self.Status.setText(self._translate("MainWindow", "Default"))
        self.AllPeople.setText(self._translate("MainWindow", "0"))
        self.WithHM.setText(self._translate("MainWindow", "0"))
        self.WithoutHM.setText(self._translate("MainWindow", "0"))
        self.UnusedHM.setText(self._translate("MainWindow", "0"))
        ########### reset label ########
        self.init_label()
        ########### reset label ########
        ########### release cap ##############
        if (self.cap != None):
            self.cap.release()
        ########### release cap ##############
        ############close yolo##########
        #if(self.my_yolo != None):
        #    self.my_yolo.close_session()
        ############close yolo##########
        pass

    def exec_mode1(self):
        #if(self.mode1_activate == False and self.mode2_activate == False):
        #    main.fun2(self, 1)
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)

            self.mode2_activate = True
        pass


    def openfolder(self):
        os.system('xdg-open "%s"' % self.foldername)
        pass


    def videosaver(self):
        fps = self.cap.get(cv.CAP_PROP_FPS)
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)


    def label_show(self):
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
        image = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setScaledContents(True)##??????
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def init_label(self):
        self.img = cv.imread("label1.jpg")
        self.label_show()

    def interrupt(self):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'终止', u'将终止当前模式！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            pass
        else:
            self.stop()
            self.mode1_activate = False
            self.mode2_activate = False
            #event.accept()
            pass

###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())












import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from qtpy import QtGui
import time
import cv2 as cv

import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import qdarkstyle

from yolo import YOLO

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self, object):
        self.setupUi(object)
        ######################################################################################
        self.lcdNumber.setNumDigits(24)
        self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
        self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
        self.timer = QTimer()  # 新建一个定时器
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        #########################################################################################
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################
        ########yolo########
        self.img = None
        args = {'image': True, 'input': None, 'output': None}
        self.my_yolo = YOLO(**args)
        self.accum_time = 0
        self.curr_fps = 0
        self.fps = "FPS: ??"
        self.prev_time = timer()
        ########yolo########
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False
        self.save_flag = True
        self.cap = None
        self.output_name = "test.avi"                                  #输出文件名
        self.output_path = "./Violation Record/" + self.output_name    #输出路径
        self._translate = QtCore.QCoreApplication.translate       #文本
        self.init_label()
        self.interrupt_flag = False            #中断标志
        self.foldername = "./Violation Record" #录像文件夹
        #######inint model#######
        self.save_flag = False
        self.cap = cv.VideoCapture(0)
        ret, self.image = self.cap.read()
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.stop()
        self.save_flag = True
        #######inint model#######

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode1.setAutoDefault(False)
        self.Mode1.setDefault(False)
        self.Mode1.setFlat(False)
        self.Mode1.setObjectName("Mode1")
        self.horizontalLayout_2.addWidget(self.Mode1)
        self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode2.setObjectName("Mode2")
        self.horizontalLayout_2.addWidget(self.Mode2)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.verticalLayout_2.addWidget(self.Open)
        spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setObjectName("Status")
        self.verticalLayout_2.addWidget(self.Status)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.AllPeople = QtWidgets.QLabel(self.centralwidget)
        self.AllPeople.setObjectName("AllPeople")
        self.verticalLayout_2.addWidget(self.AllPeople)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.WithHM = QtWidgets.QLabel(self.centralwidget)
        self.WithHM.setObjectName("WithHM")
        self.verticalLayout_2.addWidget(self.WithHM)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.aa = QtWidgets.QLabel(self.centralwidget)
        self.aa.setObjectName("aa")
        self.verticalLayout_2.addWidget(self.aa)
        self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
        self.WithoutHM.setObjectName("WithoutHM")
        self.verticalLayout_2.addWidget(self.WithoutHM)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("label10")
        self.verticalLayout_2.addWidget(self.label10)
        self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
        self.UnusedHM.setObjectName("UnusedHM")
        self.verticalLayout_2.addWidget(self.UnusedHM)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 30)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Pause.clicked.connect(self.pause)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "Mode1"))
        self.Mode2.setText(_translate("MainWindow", "Mode2"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Open.setText(_translate("MainWindow", "View Record"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.Status.setText(_translate("MainWindow", "Default"))
        self.label_3.setText(_translate("MainWindow", "Detected People:"))
        self.AllPeople.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
        self.WithHM.setText(_translate("MainWindow", "0"))
        self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
        self.WithoutHM.setText(_translate("MainWindow", "0"))
        self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
        self.UnusedHM.setText(_translate("MainWindow", "0"))

###########################################
    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
        #self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))

    def show_camera(self):
        ret, self.image = self.cap.read()
        ret, self.image = self.cap.read()
        ######yolo detect########
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.img = np.asarray(self.image)
        self.curr_time = timer()
        self.exec_time = self.curr_time - self.prev_time
        self.prev_time = self.curr_time
        self.accum_time = self.accum_time + self.exec_time
        self.curr_fps = self.curr_fps + 1
        if self. accum_time > 1:
            self.accum_time = self.accum_time - 1
            self.fps = "FPS: " + str(self.curr_fps)
            self.fps = "FPS: " + str(self.curr_fps + 10)   #fake
            self.curr_fps = 0
        cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        ######yolo detect########

        #######Video Saver########
        if(self.save_flag == True):
            self.out.write(self.img)
        #######Video Saver########

        #######show label#########
        self.label_show()
        #######show label#########




    def pause(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.vpause == False):
                self.timer_camera.stop()
                self.vpause = True
            elif (self.vpause == True):
                self.timer_camera.start(1)
                self.vpause = False
        pass

    def stop(self):
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False

        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        self.Status.setText(self._translate("MainWindow", "Default"))
        self.AllPeople.setText(self._translate("MainWindow", "0"))
        self.WithHM.setText(self._translate("MainWindow", "0"))
        self.WithoutHM.setText(self._translate("MainWindow", "0"))
        self.UnusedHM.setText(self._translate("MainWindow", "0"))
        ########### reset label ########
        self.init_label()
        ########### reset label ########
        ########### release cap ##############
        if (self.cap != None):
            self.cap.release()
        ########### release cap ##############
        ############close yolo##########
        #if(self.my_yolo != None):
        #    self.my_yolo.close_session()
        ############close yolo##########
        pass

    def exec_mode1(self):
        #if(self.mode1_activate == False and self.mode2_activate == False):
        #    main.fun2(self, 1)
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4);;All Files (*)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)
                self.mode2_activate = True
            else:
                self.stop()
        pass


    def openfolder(self):
        os.system('xdg-open "%s"' % self.foldername)
        pass


    def videosaver(self):
        fps = self.cap.get(cv.CAP_PROP_FPS)
        fps = fps/2
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)


    def label_show(self):
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
        image = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setScaledContents(True)##??????
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def init_label(self):
        self.img = cv.imread("label1.jpg")
        self.label_show()

    def interrupt(self):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'终止', u'将终止当前模式！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            pass
        else:
            self.stop()
            self.mode1_activate = False
            self.mode2_activate = False
            #event.accept()
            pass

###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())





























import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from qtpy import QtGui
import time
import cv2 as cv

import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import qdarkstyle

from yolo import YOLO

from PyQt5 import QtCore, QtGui, QtWidgets

import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGridLayout, QWidget, QVBoxLayout, \
    QLabel

class Ui_MainWindow(object):
    def __init__(self, object):
        self.setupUi(object)
        self.test_count = 0
        self.qt_img = None
        ######################################################################################
        self.lcdNumber.setNumDigits(24)
        self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
        self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
        self.timer = QTimer()  # 新建一个定时器
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        #########################################################################################
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################
        ########yolo########
        self.img = None
        args = {'image': True, 'input': None, 'output': None}
        self.my_yolo = YOLO(**args)
        self.accum_time = 0
        self.curr_fps = 0
        self.fps = "FPS: ??"
        self.prev_time = timer()
        ########yolo########
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False
        self.save_flag = True
        self.cap = None
        self.output_name = "test.avi"                                  #输出文件名
        self.output_path = "./Violation Record/" + self.output_name    #输出路径
        self._translate = QtCore.QCoreApplication.translate       #文本
        self.init_label()
        self.interrupt_flag = False            #中断标志
        self.foldername = "./Violation Record" #录像文件夹
        #######inint model#######
        self.save_flag = False
        self.cap = cv.VideoCapture(0)
        ret, self.image = self.cap.read()
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.stop()
        self.save_flag = True
        #######inint model#######
        ######init image viewer######
        self.displayed_image_size = 300
        self.col = 0
        self.row = 0

        self.initial_path = None

        self.width = 960
        self.height = 500

        self.gridLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        # self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        ######init image viewer######

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode1.setAutoDefault(False)
        self.Mode1.setDefault(False)
        self.Mode1.setFlat(False)
        self.Mode1.setObjectName("Mode1")
        self.horizontalLayout_2.addWidget(self.Mode1)
        self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode2.setObjectName("Mode2")
        self.horizontalLayout_2.addWidget(self.Mode2)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.verticalLayout_2.addWidget(self.Open)
        spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setObjectName("Status")
        self.verticalLayout_2.addWidget(self.Status)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.AllPeople = QtWidgets.QLabel(self.centralwidget)
        self.AllPeople.setObjectName("AllPeople")
        self.verticalLayout_2.addWidget(self.AllPeople)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.WithHM = QtWidgets.QLabel(self.centralwidget)
        self.WithHM.setObjectName("WithHM")
        self.verticalLayout_2.addWidget(self.WithHM)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.aa = QtWidgets.QLabel(self.centralwidget)
        self.aa.setObjectName("aa")
        self.verticalLayout_2.addWidget(self.aa)
        self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
        self.WithoutHM.setObjectName("WithoutHM")
        self.verticalLayout_2.addWidget(self.WithoutHM)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("label10")
        self.verticalLayout_2.addWidget(self.label10)
        self.UnusedHM = QtWidgets.QLabel(self.centralwidget)
        self.UnusedHM.setObjectName("UnusedHM")
        self.verticalLayout_2.addWidget(self.UnusedHM)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(558, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 194, 782))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Pause.clicked.connect(self.pause)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "Mode1"))
        self.Mode2.setText(_translate("MainWindow", "Mode2"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Open.setText(_translate("MainWindow", "View Record"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.Status.setText(_translate("MainWindow", "Default"))
        self.label_3.setText(_translate("MainWindow", "Detected People:"))
        self.AllPeople.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "People With Helmet:"))
        self.WithHM.setText(_translate("MainWindow", "0"))
        self.aa.setText(_translate("MainWindow", "People Without Helmet:"))
        self.WithoutHM.setText(_translate("MainWindow", "0"))
        self.label10.setText(_translate("MainWindow", "Unused Helmet:"))
        self.UnusedHM.setText(_translate("MainWindow", "0"))

    ###########################################
    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
        #self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))

    def show_camera(self):
        ret, self.image = self.cap.read()
        ret, self.image = self.cap.read()
        ######yolo detect########
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.img = np.asarray(self.image)
        self.curr_time = timer()
        self.exec_time = self.curr_time - self.prev_time
        self.prev_time = self.curr_time
        self.accum_time = self.accum_time + self.exec_time
        self.curr_fps = self.curr_fps + 1
        if self. accum_time > 1:
            self.accum_time = self.accum_time - 1
            self.fps = "FPS: " + str(self.curr_fps)
            self.fps = "FPS: " + str(self.curr_fps + 10)   #fake
            self.curr_fps = 0
        cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        ######yolo detect########

        #######Video Saver########
        if(self.save_flag == True):
            self.out.write(self.img)
        #######Video Saver########

        #######show label#########
        self.label_show()
        #######show label#########

        #######img viewer########
        if(self.test_count % 100 == 0):
            image_id = "./Violation Record/"+str(self.test_count)+".jpg"
            cv.imwrite(image_id, self.img)
            print(image_id)
            pixmap = QPixmap(image_id)
            self.addImage(pixmap, image_id)
            print(pixmap)
            QApplication.processEvents()
        #######img viewer########
        self.test_count += 1






    def pause(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.vpause == False):
                self.timer_camera.stop()
                self.vpause = True
            elif (self.vpause == True):
                self.timer_camera.start(1)
                self.vpause = False
        pass

    def stop(self):
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False

        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        self.Status.setText(self._translate("MainWindow", "Default"))
        self.AllPeople.setText(self._translate("MainWindow", "0"))
        self.WithHM.setText(self._translate("MainWindow", "0"))
        self.WithoutHM.setText(self._translate("MainWindow", "0"))
        self.UnusedHM.setText(self._translate("MainWindow", "0"))
        ########### reset label ########
        self.init_label()
        ########### reset label ########
        ########### release cap ##############
        if (self.cap != None):
            self.cap.release()
        ########### release cap ##############
        ############close yolo##########
        #if(self.my_yolo != None):
        #    self.my_yolo.close_session()
        ############close yolo##########
        pass

    def exec_mode1(self):
        #if(self.mode1_activate == False and self.mode2_activate == False):
        #    main.fun2(self, 1)
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4);;All Files (*)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)
                self.mode2_activate = True
            else:
                self.stop()
        pass


    def openfolder(self):
        os.system('xdg-open "%s"' % self.foldername)
        pass


    def videosaver(self):
        fps = self.cap.get(cv.CAP_PROP_FPS)
        fps = fps/2
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)


    def label_show(self):
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
        self.qt_img = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setScaledContents(True)##??????
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.qt_img))

    def init_label(self):
        self.img = cv.imread("label1.jpg")
        self.label_show()

    def interrupt(self):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'终止', u'将终止当前模式！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            pass
        else:
            self.stop()
            self.mode1_activate = False
            self.mode2_activate = False
            #event.accept()
            pass

    ####### image viewer #############
    def open(self):
        file_path = QFileDialog.getExistingDirectory(None, '选择文文件夹', '/')
        if file_path == None:
            QMessageBox.information(None, '提示', '文件为空，请重新操作')
        else:
            self.initial_path = file_path
            print(file_path)

    def start_img_viewer(self):
        if self.initial_path:
            file_path = self.initial_path
            print('file_path为{}'.format(file_path))
            print(file_path)
            img_type = 'jpg'
            # if file_path and img_type:
            if file_path and img_type:
                png_list = list(i for i in os.listdir(file_path) if str(i).endswith('.{}'.format(img_type)))
                print(png_list)
                num = len(png_list)
                if num != 0:
                    for i in range(num):
                        image_id = str(file_path + '/' + png_list[i])
                        print(image_id)
                        pixmap = QPixmap(image_id)
                        self.addImage(pixmap, image_id)
                        print(pixmap)
                        QApplication.processEvents()
                else:
                    QMessageBox.warning(self, '错误', '生成图片文件为空')
                    self.event(exit())
            else:
                QMessageBox.warning(self, '错误', '文件为空，请稍后')
        else:
            QMessageBox.warning(self, '错误', '文件为空，请稍后')

    def loc_fil(self, stre):
        print('存放地址为{}'.format(stre))
        self.initial_path = stre

    def geng_path(self, loc):
        print('路径为，，，，，，{}'.format(loc))

    def gen_type(self, type):
        print('图片类型为：，，，，{}'.format(type))

    def addImage(self, pixmap, image_id):
        # 图像法列数
        nr_of_columns = self.get_nr_of_image_columns()
        # 这个布局内的数量
        nr_of_widgets = self.gridLayout.count()
        self.max_columns = nr_of_columns
        if self.col < self.max_columns:
            self.col = self.col + 1
        else:
            self.col = 0
            self.row += 1

        print('行数为{}'.format(self.row))
        print('此时布局内不含有的元素数为{}'.format(nr_of_widgets))

        print('列数为{}'.format(self.col))
        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, pixmap, image_id)
        clickable_image.clicked.connect(self.on_left_clicked)
        clickable_image.rightClicked.connect(self.on_right_clicked)
        # self.gridLayout.addWidget(clickable_image, self.row, self.col)

        self.gridLayout.addWidget(clickable_image, self.row)

    def on_left_clicked(self, image_id):
        print('left clicked - image id = ' + image_id)

    def on_right_clicked(self, image_id):
        print('right clicked - image id = ' + image_id)

    def get_nr_of_image_columns(self):
        # 展示图片的区域
        scroll_area_images_width = self.width
        if scroll_area_images_width > self.displayed_image_size:

            pic_of_columns = scroll_area_images_width // self.displayed_image_size  # 计算出一行几列；
        else:
            pic_of_columns = 1
        return pic_of_columns

    def setDisplayedImageSize(self, image_size):
        self.displayed_image_size = image_size

class QClickableImage(QWidget):
    image_id = ''

    def __init__(self, width=0, height=0, pixmap=None, image_id=''):
        QWidget.__init__(self)

        self.layout = QVBoxLayout(self)
        self.label1 = QLabel()
        self.label1.setObjectName('label1')
        self.lable2 = QLabel()
        self.lable2.setObjectName('label2')
        self.width = width
        self.height = height
        self.pixmap = pixmap

        if self.width and self.height:
            self.resize(self.width, self.height)
        if self.pixmap:
            pixmap = self.pixmap.scaled(QSize(self.width, self.height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label1.setPixmap(pixmap)
            self.label1.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.label1)
        if image_id:
            self.image_id = image_id
            self.lable2.setText(image_id)
            self.lable2.setAlignment(Qt.AlignCenter)
            ###让文字自适应大小
            self.lable2.adjustSize()
            self.layout.addWidget(self.lable2)
        self.setLayout(self.layout)

    clicked = pyqtSignal(object)
    rightClicked = pyqtSignal(object)

    def mouseressevent(self, ev):
        print('55555555555555555')
        if ev.button() == Qt.RightButton:
            print('dasdasd')
            # 鼠标右击
            self.rightClicked.emit(self.image_id)
        else:
            self.clicked.emit(self.image_id)

    def imageId(self):
        return self.image_id



###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())


    # showMinimized() - 最小化;
    # showMaximized() - 最大化;
    # showFullscreen() - 窗口全屏显示，不带标题栏和边框。
    # showNormal() - 回到窗口的原始尺寸。
    # activateWindow()
    # 将窗口变为活动窗口。如果窗口是最小化状态，将会恢复到窗口的原始尺寸。
    # setwindowState()
    # 根据Flags值，设置窗口的状态。Flags值可为下列值的组合，这些值来自QtCore.Qt。
    # windowNoState - 正常状态
    # windowMinimized - 最小化
    # windowMaximized - 最大化
    # windowFullScreen - 全屏显示
    # windowActive - 活动窗口
    # 可用下列函数来获得窗口的状态：
    #
    # isMinimized() - 如果窗口最小化，返回值为True;
    # 否则，为False;
    # isMaximized() - 如果窗口最大化，返回值为True;
    # 否则，为False;
    # isFullScreen() - 如果窗口全屏显示，返回值为True;
    # 否则，为False;
    # isActiveWindow() - 如果是活动窗口，返回值为True;
    # 否则，为False;;
    # windowstate() - 返回窗口状态的组合值.















































import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from qtpy import QtGui
import time
import cv2 as cv

import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import qdarkstyle

from yolo import YOLO

from PyQt5 import QtCore, QtGui, QtWidgets

import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGridLayout, QWidget, QVBoxLayout, \
    QLabel

class Ui_MainWindow(object):
    def __init__(self, object):
        self.setupUi(object)
        self.test_count = 0
        self.qt_img = None
        ######init image viewer######
        self.displayed_image_size = 300
        self.col = 0
        self.row = 0

        self.initial_path = None

        self.width = 960
        self.height = 500

        self.gridLayout_scroll = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        # self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        ######init image viewer######
        ######################################################################################
        self.lcdNumber.setNumDigits(24)
        self.ShowColon = True  # 是否显示时间如[12:07]中的冒号，用于冒号的闪烁
        self.dragPosition = QPoint(0, 0)  # 用于保存鼠标相对于电子时钟左上角的偏移值
        self.timer = QTimer()  # 新建一个定时器
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        #########################################################################################
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################
        ########yolo########
        self.img = None
        args = {'image': True, 'input': None, 'output': None}
        self.my_yolo = YOLO(**args)
        self.accum_time = 0
        self.curr_fps = 0
        self.fps = "FPS: ??"
        self.prev_time = timer()
        ########yolo########
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False
        self.save_flag = True
        self.cap = None
        self.output_name = "test.avi"                                  #输出文件名
        self.output_path = "./Violation Record/" + self.output_name    #输出路径
        self._translate = QtCore.QCoreApplication.translate       #文本
        self.init_label()
        self.interrupt_flag = False            #中断标志
        self.foldername = "./Violation Record" #录像文件夹
        #######inint model#######
        self.save_flag = False
        self.cap = cv.VideoCapture(0)
        ret, self.image = self.cap.read()
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.stop()
        self.save_flag = True
        #######inint model#######

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.Mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode1.setAutoDefault(False)
        self.Mode1.setDefault(False)
        self.Mode1.setFlat(False)
        self.Mode1.setObjectName("Mode1")
        self.horizontalLayout_3.addWidget(self.Mode1)
        self.Mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode2.setObjectName("Mode2")
        self.horizontalLayout_3.addWidget(self.Mode2)
        self.fullscreen = QtWidgets.QPushButton(self.centralwidget)
        self.fullscreen.setObjectName("fullscreen")
        self.horizontalLayout_3.addWidget(self.fullscreen)
        self.path_setting = QtWidgets.QPushButton(self.centralwidget)
        self.path_setting.setObjectName("path_setting")
        self.horizontalLayout_3.addWidget(self.path_setting)
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setObjectName("record")
        self.horizontalLayout_3.addWidget(self.record)
        self.language = QtWidgets.QPushButton(self.centralwidget)
        self.language.setObjectName("language")
        self.horizontalLayout_3.addWidget(self.language)
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setObjectName("help")
        self.horizontalLayout_3.addWidget(self.help)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setObjectName("Status")
        self.gridLayout.addWidget(self.Status, 0, 0, 1, 1)
        self.illegal = QtWidgets.QLabel(self.centralwidget)
        self.illegal.setObjectName("illegal")
        self.gridLayout.addWidget(self.illegal, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.AllPeople = QtWidgets.QLabel(self.centralwidget)
        self.AllPeople.setObjectName("AllPeople")
        self.gridLayout.addWidget(self.AllPeople, 1, 0, 1, 1)
        self.WithoutHM = QtWidgets.QLabel(self.centralwidget)
        self.WithoutHM.setObjectName("WithoutHM")
        self.gridLayout.addWidget(self.WithoutHM, 1, 1, 1, 1)
        self.WithHM = QtWidgets.QLabel(self.centralwidget)
        self.WithHM.setObjectName("WithHM")
        self.gridLayout.addWidget(self.WithHM, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 207, 597))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.horizontalLayout.addWidget(self.Open)
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 8)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Pause.clicked.connect(self.pause)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        self.Clear.clicked.connect(self.clear_img)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "Mode1"))
        self.Mode2.setText(_translate("MainWindow", "Mode2"))
        self.fullscreen.setText(_translate("MainWindow", "full screen"))
        self.path_setting.setText(_translate("MainWindow", "path setting"))
        self.record.setText(_translate("MainWindow", "recording"))
        self.language.setText(_translate("MainWindow", "language"))
        self.help.setText(_translate("MainWindow", "help"))
        self.Status.setText(_translate("MainWindow", "Status: Default"))
        self.illegal.setText(_translate("MainWindow", "illegal: 0"))
        self.label_2.setText(_translate("MainWindow", "output: True"))
        self.AllPeople.setText(_translate("MainWindow", "all person: 0"))
        self.WithoutHM.setText(_translate("MainWindow", "person: 0"))
        self.WithHM.setText(_translate("MainWindow", "hat: 0"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.Open.setText(_translate("MainWindow", "View "))
        self.Clear.setText(_translate("MainWindow", "Clear"))

    ###########################################
    def clear_img(self):
        for i in range(self.gridLayout_scroll.count()):
            self.gridLayout_scroll.itemAt(i).widget().deleteLater()
        pass

    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
        #self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))

    def show_camera(self):
        ret, self.image = self.cap.read()
        ret, self.image = self.cap.read()
        ######yolo detect########
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.img = np.asarray(self.image)
        self.curr_time = timer()
        self.exec_time = self.curr_time - self.prev_time
        self.prev_time = self.curr_time
        self.accum_time = self.accum_time + self.exec_time
        self.curr_fps = self.curr_fps + 1
        if self. accum_time > 1:
            self.accum_time = self.accum_time - 1
            self.fps = "FPS: " + str(self.curr_fps)
            self.fps = "FPS: " + str(self.curr_fps + 10)   #fake
            self.curr_fps = 0
        cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.50, color=(255, 0, 0), thickness=2)
        ######yolo detect########

        #######Video Saver########
        if(self.save_flag == True):
            self.out.write(self.img)
        #######Video Saver########

        #######show label#########
        self.label_show()
        #######show label#########

        #######img viewer########
        if(self.test_count % 100 == 0):
            self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
            image_id = "./Violation Record/"+str(self.test_count)+".jpg"
            cv.imwrite(image_id, self.img)
            print(image_id)
            pixmap = QPixmap(image_id)
            self.addImage(pixmap, image_id)
            print(pixmap)
            QApplication.processEvents()
        #######img viewer########
        self.test_count += 1






    def pause(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.vpause == False):
                self.timer_camera.stop()
                self.vpause = True
            elif (self.vpause == True):
                self.timer_camera.start(1)
                self.vpause = False
        pass

    def stop(self):
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False

        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        self.Status.setText(self._translate("MainWindow", "Status: Default"))
        self.illegal.setText(self._translate("MainWindow", "illegal: 0"))
        self.label_2.setText(self._translate("MainWindow", "output: True"))
        self.AllPeople.setText(self._translate("MainWindow", "all person: 0"))
        self.WithoutHM.setText(self._translate("MainWindow", "person: 0"))
        self.WithHM.setText(self._translate("MainWindow", "hat: 0"))
        ########### reset label ########
        self.init_label()
        ########### reset label ########
        ########### release cap ##############
        if (self.cap != None):
            self.cap.release()
        ########### release cap ##############
        ############close yolo##########
        #if(self.my_yolo != None):
        #    self.my_yolo.close_session()
        ############close yolo##########

        pass

    def exec_mode1(self):
        #if(self.mode1_activate == False and self.mode2_activate == False):
        #    main.fun2(self, 1)
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4);;All Files (*)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)
                self.mode2_activate = True
            else:
                self.stop()
        pass


    def openfolder(self):
        os.system('xdg-open "%s"' % self.foldername)
        pass


    def videosaver(self):
        fps = self.cap.get(cv.CAP_PROP_FPS)
        fps = fps/2
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        self.out = cv.VideoWriter(self.output_path, fourcc, fps, size)


    def label_show(self):
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = bytesPerComponent * width
        cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
        self.qt_img = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label.setScaledContents(True)##??????
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.qt_img))

    def init_label(self):
        self.img = cv.imread("label1.jpg")
        self.label_show()

    def interrupt(self):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'终止', u'将终止当前模式！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            pass
        else:
            self.stop()
            self.mode1_activate = False
            self.mode2_activate = False
            #event.accept()
            pass

    ####### image viewer #############
    def open(self):
        file_path = QFileDialog.getExistingDirectory(None, '选择文文件夹', '/')
        if file_path == None:
            QMessageBox.information(None, '提示', '文件为空，请重新操作')
        else:
            self.initial_path = file_path
            print(file_path)

    def start_img_viewer(self):
        if self.initial_path:
            file_path = self.initial_path
            print('file_path为{}'.format(file_path))
            print(file_path)
            img_type = 'jpg'
            # if file_path and img_type:
            if file_path and img_type:
                png_list = list(i for i in os.listdir(file_path) if str(i).endswith('.{}'.format(img_type)))
                print(png_list)
                num = len(png_list)
                if num != 0:
                    for i in range(num):
                        image_id = str(file_path + '/' + png_list[i])
                        print(image_id)
                        pixmap = QPixmap(image_id)
                        self.addImage(pixmap, image_id)
                        print(pixmap)
                        QApplication.processEvents()
                else:
                    QMessageBox.warning(self, '错误', '生成图片文件为空')
                    self.event(exit())
            else:
                QMessageBox.warning(self, '错误', '文件为空，请稍后')
        else:
            QMessageBox.warning(self, '错误', '文件为空，请稍后')

    def loc_fil(self, stre):
        print('存放地址为{}'.format(stre))
        self.initial_path = stre

    def geng_path(self, loc):
        print('路径为，，，，，，{}'.format(loc))

    def gen_type(self, type):
        print('图片类型为：，，，，{}'.format(type))

    def addImage(self, pixmap, image_id):
        # 图像法列数
        nr_of_columns = self.get_nr_of_image_columns()
        # 这个布局内的数量
        nr_of_widgets = self.gridLayout_scroll.count()
        self.max_columns = nr_of_columns
        if self.col < self.max_columns:
            self.col = self.col + 1
        else:
            self.col = 0
            self.row += 1

        print('行数为{}'.format(self.row))
        print('此时布局内不含有的元素数为{}'.format(nr_of_widgets))

        print('列数为{}'.format(self.col))
        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, pixmap, image_id)
        clickable_image.clicked.connect(self.on_left_clicked)
        clickable_image.rightClicked.connect(self.on_right_clicked)
        # self.gridLayout.addWidget(clickable_image, self.row, self.col)

        self.gridLayout_scroll.addWidget(clickable_image, self.row)

    def on_left_clicked(self, image_id):
        print('left clicked - image id = ' + image_id)

    def on_right_clicked(self, image_id):
        print('right clicked - image id = ' + image_id)

    def get_nr_of_image_columns(self):
        # 展示图片的区域
        scroll_area_images_width = self.width
        if scroll_area_images_width > self.displayed_image_size:

            pic_of_columns = scroll_area_images_width // self.displayed_image_size  # 计算出一行几列；
        else:
            pic_of_columns = 1
        return pic_of_columns

    def setDisplayedImageSize(self, image_size):
        self.displayed_image_size = image_size

class QClickableImage(QWidget):
    image_id = ''

    def __init__(self, width=0, height=0, pixmap=None, image_id=''):
        QWidget.__init__(self)

        self.layout = QVBoxLayout(self)
        self.label1 = QLabel()
        self.label1.setObjectName('label1')
        self.lable2 = QLabel()
        self.lable2.setObjectName('label2')
        self.width = width
        self.height = height
        self.pixmap = pixmap

        if self.width and self.height:
            self.resize(self.width, self.height)
        if self.pixmap:
            pixmap = self.pixmap.scaled(QSize(self.width, self.height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label1.setPixmap(pixmap)
            self.label1.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.label1)
        if image_id:
            self.image_id = image_id
            self.lable2.setText(image_id)
            self.lable2.setAlignment(Qt.AlignCenter)
            ###让文字自适应大小
            self.lable2.adjustSize()
            self.layout.addWidget(self.lable2)
        self.setLayout(self.layout)

    clicked = pyqtSignal(object)
    rightClicked = pyqtSignal(object)

    def mouseressevent(self, ev):
        print('55555555555555555')
        if ev.button() == Qt.RightButton:
            print('dasdasd')
            # 鼠标右击
            self.rightClicked.emit(self.image_id)
        else:
            self.clicked.emit(self.image_id)

    def imageId(self):
        return self.image_id



###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())


    # showMinimized() - 最小化;
    # showMaximized() - 最大化;
    # showFullscreen() - 窗口全屏显示，不带标题栏和边框。
    # showNormal() - 回到窗口的原始尺寸。
    # activateWindow()
    # 将窗口变为活动窗口。如果窗口是最小化状态，将会恢复到窗口的原始尺寸。
    # setwindowState()
    # 根据Flags值，设置窗口的状态。Flags值可为下列值的组合，这些值来自QtCore.Qt。
    # windowNoState - 正常状态
    # windowMinimized - 最小化
    # windowMaximized - 最大化
    # windowFullScreen - 全屏显示
    # windowActive - 活动窗口
    # 可用下列函数来获得窗口的状态：
    #
    # isMinimized() - 如果窗口最小化，返回值为True;
    # 否则，为False;
    # isMaximized() - 如果窗口最大化，返回值为True;
    # 否则，为False;
    # isFullScreen() - 如果窗口全屏显示，返回值为True;
    # 否则，为False;
    # isActiveWindow() - 如果是活动窗口，返回值为True;
    # 否则，为False;;
    # windowstate() - 返回窗口状态的组合值.
