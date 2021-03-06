import logging
import os
from timeit import default_timer as timer

import PyQt5
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

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path
from yolo import YOLO

from PyQt5 import QtCore, QtGui, QtWidgets
from tf_pose import common
from tf_pose.common import CocoPart
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
    QLabel, QDialog
from GUI import dialog_path_setting, dialog_record_setting, dialog_language_setting, dialog_help

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()
        self.langusgeFlag = 'Chinese'
        #self.language_flag = self.setting.value("language_flag")
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
        self.ShowColon = True  # ?????????????????????[12:07]????????????????????????????????????
        self.dragPosition = QPoint(0, 0)  # ????????????????????????????????????????????????????????????
        self.timer = QTimer()  # ?????????????????????
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        #########################################################################################
        self.timer_camera = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        ########################################################################################
        ######################pose##########################
        self.get_first_point = False
        self.get_second_point = False
        self.get_third_point = False
        self.mode3_activate = False
        def str2bool(v):
            return v.lower() in ("yes", "true", "t", "1")
        self.w, self.h = 0,0
        if self.w > 0 and self.h > 0:
            self.e = TfPoseEstimator(get_graph_path("mobilenet_thin"), target_size=(self.w, self.h), trt_bool=str2bool("False"))
        else:
            self.e = TfPoseEstimator(get_graph_path("mobilenet_thin"), target_size=(432, 368), trt_bool=str2bool("False"))
        ######################pose##########################
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
        self.out = None
        self.output_name = "test.mp4"                                  #???????????????
        self.output_path = "./Violation Record/" + self.output_name    #????????????
        self._translate = QtCore.QCoreApplication.translate       #??????
        self.init_label()
        self.interrupt_flag = False            #????????????
        self.foldername = "./Violation Record" #???????????????
        #######inint model#######
        self.save_flag = False
        self.cap = cv.VideoCapture(0)
        ret, self.image = self.cap.read()
        self.image = Image.fromarray(self.image)
        self.image = self.my_yolo.detect_image(self.image)
        self.stop()
        self.save_flag = True
        #######inint model#######
        #######draw line#########
        self.get_first_point = False
        self.get_second_point = False
        self.get_thrid_point = False
        self.point_count = 0
        self.get_point_flag = False
        self.crossing_flag = False
        #######draw line#########
        ###########################?????????###########################
        self.dialog_path_setting = PyQt5.QtWidgets.QDialog()
        self.window_dialog_path_setting = dialog_path_setting.Ui_window_path_setting()
        self.window_dialog_path_setting.setupUi(self.dialog_path_setting)

        self.dialog_record_setting = PyQt5.QtWidgets.QDialog()
        self.window_dialog_record_setting = dialog_record_setting.Ui_window_record_setting()
        self.window_dialog_record_setting.setupUi(self.dialog_record_setting)

        self.dialog_language_setting = PyQt5.QtWidgets.QDialog()
        self.window_dialog_language_setting = dialog_language_setting.Ui_window_language_setting()
        self.window_dialog_language_setting.setupUi(self.dialog_language_setting)

        _translate = QtCore.QCoreApplication.translate
        #self.langusgeFlag = 'Chinese'
        #self.window_dialog_help.set

        def languageChange():
            if self.window_dialog_language_setting.language_flag == 'English':
                print("EEEEEE")
                self.langusgeFlag = 'English'
                self.Mode3.setToolTip("Follow steps to start tf-pose")
                self.fullscreen.setText(_translate("MainWindow", "FullScreen"))
                self.fullscreen.setText(_translate("MainWindow", "ExitFullScreen"))
                #self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.Mode1.setText(_translate("MainWindow", "Camera"))
                self.Mode2.setText(_translate("MainWindow", "Video"))
                self.Mode3.setText(_translate("MainWindow", "PoseDetection"))
                #self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.path_setting.setText(_translate("MainWindow", "Path"))
                self.record.setText(_translate("MainWindow", "OutputSetting"))
                self.language.setText(_translate("MainWindow", "Language"))
                self.help.setText(_translate("MainWindow", "Help"))
                self.Pause.setText(_translate("MainWindow", "Pause"))
                self.Close.setText(_translate("MainWindow", "Close"))
                self.label_3.setText(_translate("MainWindow", "CurrentInfo???"))
                self.Status.setText(_translate("MainWindow", "Status: Default"))
                self.illegal.setText(_translate("MainWindow", "OverstepDetection: False"))
                self.label_2.setText(_translate("MainWindow", "Output: True"))
                self.AllPeople.setText(_translate("MainWindow", "Staff: 0"))
                self.WithoutHM.setText(_translate("MainWindow", "Violator: 0"))
                self.WithHM.setText(_translate("MainWindow", "Normal: 0"))
                self.illegalrecord.setText(_translate("MainWindow", "Violator???"))
                self.Open.setText(_translate("MainWindow", "View"))
                self.Clear.setText(_translate("MainWindow", "Clear"))
                self.player.setText(_translate("MainWindow", "Player???"))

                self.crossing = "Closed"
                self.show_status = "Default"
                self.show_output = "True"

                self.window_dialog_language_setting.button_cancel.setText("Cancel")
                self.window_dialog_language_setting.button_save.setText("Save")
                self.window_dialog_language_setting.save_flag.setText(_translate("window_language_setting", "Language:"))
                # self.setWindowTitle(_translate("window_help", "HELP"))
                # self.window_dialog_language_setting
                # self.window_dialog_language_setting.setWindowTitle(_translate("window_dialog_language_setting","Language"))

                self.window_dialog_path_setting.button_cancel.setText("Cancel")
                self.window_dialog_path_setting.button_save.setText("Save")
                self.window_dialog_path_setting.name_output_path.setText(_translate("window_path_setting", "Output"))
                self.window_dialog_path_setting.select_output_path.setText(_translate("window_path_setting", "Folder"))
                self.window_dialog_path_setting.name_record_path.setText(_translate("window_path_setting", "ViolationRecord"))
                self.window_dialog_path_setting.select_1.setText(_translate("window_path_setting", "Folder"))
                # self.window_dialog_path_setting.setWindowTitle('Path')

                self.window_dialog_record_setting.button_cancel.setText("Cancel")
                self.window_dialog_record_setting.button_save.setText("Save")
                self.window_dialog_record_setting.save_flag.setText(_translate("window_record_setting", "Output:"))
                self.window_dialog_record_setting.Yes.setText(_translate("window_record_setting", "True"))
                self.window_dialog_record_setting.No.setText(_translate("window_record_setting", "False"))
                self.window_dialog_record_setting.label_2.setText(_translate("window_record_setting", "Output fps:"))
                self.window_dialog_record_setting.label.setText(_translate("window_record_setting", "Output px:"))
                # self.window_dialog_record_setting.setWindowTitle('OutputSetting')

                self.window_dialog_help.button_Ok.setText("OK")
                ##############title name##############
                self.dialog_help.setWindowTitle('Help')
                self.dialog_language_setting.setWindowTitle('Language')
                self.dialog_path_setting.setWindowTitle('Path')
                self.dialog_record_setting.setWindowTitle('OutputSetting')


                # self.window_dialog_help.setWindowTitle('Help')

            if self.window_dialog_language_setting.language_flag == 'Chinese':
                print("CCCCCC")
                self.langusgeFlag = 'Chinese'
                self.Mode3.setToolTip("?????????????????????????????????")
                self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.Mode1.setText(_translate("MainWindow", "???????????????"))
                self.Mode2.setText(_translate("MainWindow", "????????????"))
                self.Mode3.setText(_translate("MainWindow", "????????????"))
                self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.path_setting.setText(_translate("MainWindow", "????????????"))
                self.record.setText(_translate("MainWindow", "????????????"))
                self.language.setText(_translate("MainWindow", "??????"))
                self.help.setText(_translate("MainWindow", "??????"))
                self.Pause.setText(_translate("MainWindow", "??????"))
                self.Close.setText(_translate("MainWindow", "??????"))
                self.label_3.setText(_translate("MainWindow", "???????????????"))
                self.Status.setText(_translate("MainWindow", "????????????: ??????"))
                self.illegal.setText(_translate("MainWindow", "????????????: ??????"))
                self.label_2.setText(_translate("MainWindow", "????????????: ??????"))
                self.AllPeople.setText(_translate("MainWindow", "?????????: 0"))
                self.WithoutHM.setText(_translate("MainWindow", "???????????????: 0"))
                self.WithHM.setText(_translate("MainWindow", "???????????????: 0"))
                self.illegalrecord.setText(_translate("MainWindow", "???????????????"))
                self.Open.setText(_translate("MainWindow", "??????"))
                self.Clear.setText(_translate("MainWindow", "??????"))
                self.player.setText(_translate("MainWindow", "?????????:"))

                self.crossing = "??????"
                self.show_status = "??????"
                self.show_output = "??????"

                self.window_dialog_language_setting.button_cancel.setText("??????")
                self.window_dialog_language_setting.button_save.setText("??????")
                self.window_dialog_language_setting.save_flag.setText(_translate("window_language_setting", "?????????"))
                # self.window_dialog_language_setting.setWindowTitle('??????')

                self.window_dialog_path_setting.button_cancel.setText("??????")
                self.window_dialog_path_setting.button_save.setText("??????")
                self.window_dialog_path_setting.name_output_path.setText(_translate("window_path_setting", "????????????"))
                self.window_dialog_path_setting.select_output_path.setText(_translate("window_path_setting", "???????????????"))
                self.window_dialog_path_setting.name_record_path.setText(_translate("window_path_setting", "??????????????????"))
                self.window_dialog_path_setting.select_1.setText(_translate("window_path_setting", "???????????????"))
                # self.window_dialog_path_setting.setWindowTitle('????????????')

                self.window_dialog_record_setting.button_cancel.setText("??????")
                self.window_dialog_record_setting.button_save.setText("??????")
                self.window_dialog_record_setting.save_flag.setText(_translate("window_record_setting", "???????????????"))
                self.window_dialog_record_setting.Yes.setText(_translate("window_record_setting", "??????"))
                self.window_dialog_record_setting.No.setText(_translate("window_record_setting", "??????"))
                self.window_dialog_record_setting.label_2.setText(_translate("window_record_setting", "???????????????"))
                self.window_dialog_record_setting.label.setText(_translate("window_record_setting", "??????????????????"))
                # self.window_dialog_record_setting.setWindowTitle('????????????')

                self.window_dialog_help.button_Ok.setText("??????")

                self.dialog_help.setWindowTitle('??????')
                self.dialog_language_setting.setWindowTitle('??????')
                self.dialog_path_setting.setWindowTitle('????????????')
                self.dialog_record_setting.setWindowTitle('????????????')

        self.window_dialog_language_setting.button_save.clicked.connect(languageChange)

        self.dialog_help = PyQt5.QtWidgets.QDialog()
        self.window_dialog_help = dialog_help.Ui_window_help()
        self.window_dialog_help.setupUi(self.dialog_help)

        ####????????????
        self.dialog_path_setting.setFixedSize(self.dialog_path_setting.width(), self.dialog_path_setting.height())
        self.dialog_record_setting.setFixedSize(self.dialog_record_setting.width(), self.dialog_record_setting.height())
        self.dialog_language_setting.setFixedSize(self.dialog_language_setting.width(), self.dialog_language_setting.height())
        self.dialog_help.setFixedSize(self.dialog_help.width(), self.dialog_help.height())
        ####????????????
        ###########################?????????###########################

        self.last_person = 0
        #####????????????######
        self.all_person = 0
        self.person = 0
        self.hat = 0
        # self.crossing =  "??????"
        # self.show_status = "??????"
        # self.show_output = "??????"
        #####????????????######
        languageChange()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(2020, 1080)
        self.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.Mode3 = QtWidgets.QPushButton(self.centralwidget)
        self.Mode3.setObjectName("Mode3")
        self.horizontalLayout_3.addWidget(self.Mode3)
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.player = QtWidgets.QLabel(self.centralwidget)
        self.player.setObjectName("player")
        self.horizontalLayout_5.addWidget(self.player)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.illegalrecord = QtWidgets.QLabel(self.centralwidget)
        self.illegalrecord.setObjectName("illegalrecord")
        self.horizontalLayout_5.addWidget(self.illegalrecord)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 22)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.label.setMouseTracking(True)
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setObjectName("Pause")
        self.horizontalLayout_2.addWidget(self.Pause)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 25)
        self.horizontalLayout_2.setStretch(2, 8)
        self.horizontalLayout_2.setStretch(3, 8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
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
        self.verticalLayout_3.addLayout(self.gridLayout)
        #self.verticalLayout_3.setStretch(0, 80)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 461, 83))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.horizontalLayout.addWidget(self.Open)
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.Mode1.clicked.connect(self.exec_mode1)
        self.Mode2.clicked.connect(self.exec_mode2)
        self.Mode3.clicked.connect(self.exec_mode3)
        self.Pause.clicked.connect(self.pause)
        self.Pause.clicked.connect(self.Pause.toggle)
        self.Close.clicked.connect(self.stop)
        self.Open.clicked.connect(self.openfolder)
        self.Clear.clicked.connect(self.clear_img)
        ########### ????????? ##########
        self.fullscreen.clicked.connect(self.full_screen)
        self.path_setting.clicked.connect(self.fun_path_setting)
        self.record.clicked.connect(self.fun_record_setting)
        self.language.clicked.connect(self.fun_language_setting)
        self.help.clicked.connect(self.fun_help)


        ########### ???????????? ##########
        self.Mode3.setToolTip("??????????????????????????????")
        #self.label.setToolTip("point1")
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        ########### ???????????? ##########


        ########### ???????????? ##########
        self.Mode1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Mode2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Mode3.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen.setCursor(QCursor(Qt.PointingHandCursor))
        self.help.setCursor(QCursor(Qt.PointingHandCursor))
        self.path_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.record.setCursor(QCursor(Qt.PointingHandCursor))
        self.language.setCursor(QCursor(Qt.PointingHandCursor))
        self.Pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.Close.setCursor(QCursor(Qt.PointingHandCursor))
        self.Clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.Open.setCursor(QCursor(Qt.PointingHandCursor))
        ########### ???????????? ##########

        ########### ????????? ##########
        QtCore.QMetaObject.connectSlotsByName(self)

        ########## ???????????? #########
        icon_Pause1 = QIcon('./source/pause.png')
        icon_Pause2 = QIcon('./source/play.png')
        size = QSize(25, 25)
        size1 = QSize(20, 20)
        self.Pause.setIconSize(size1)
        self.Pause.setIcon(icon_Pause1)
        self.PauseFlag = 0
        self.VideoOnFlag = 0

        def PauseChange():
            if self.PauseFlag == 0 and self.VideoOnFlag == 1:
                self.Pause.setIcon(icon_Pause2)
                self.PauseFlag = 1
            elif self.PauseFlag == 1 and self.VideoOnFlag == 1:
                self.Pause.setIcon(icon_Pause1)
                self.PauseFlag = 0

        self.Pause.clicked.connect(PauseChange)

        def VideoOnFlagChange():
            if self.VideoOnFlag == 0:
                self.VideoOnFlag = 1

        self.Mode1.clicked.connect(VideoOnFlagChange)
        self.Mode2.clicked.connect(VideoOnFlagChange)

        icon_fullscreen1 = QIcon('./source/fullscreen.png')
        icon_fullscreen2 = QIcon('./source/icon.png')
        self.fullscreen.setIconSize(size)
        self.fullscreen.setIcon(icon_fullscreen1)
        self.FullscreenFlag = 0
        _translate = QtCore.QCoreApplication.translate
        self.fullscreen.setText(_translate("MainWindow", "????????????"))

        def FullcreenChange():
            if self.FullscreenFlag == 0:
                self.fullscreen.setIcon(icon_fullscreen2)
                if self.window_dialog_language_setting.language_flag == 'Chinese':
                    self.fullscreen.setText(_translate("MainWindow", "????????????"))
                elif self.window_dialog_language_setting.language_flag == 'English':
                    self.fullscreen.setText(_translate("MainWindow", "ExitFullScreen"))
                self.FullscreenFlag = 1
            elif self.FullscreenFlag == 1:
                self.fullscreen.setIcon(icon_fullscreen1)
                if self.window_dialog_language_setting.language_flag == 'Chinese':
                    self.fullscreen.setText(_translate("MainWindow", "????????????"))
                elif self.window_dialog_language_setting.language_flag == 'English':
                    self.fullscreen.setText(_translate("MainWindow", "FullScreen"))
                #self.fullscreen.setText(_translate("MainWindow", "????????????"))
                self.FullscreenFlag = 0

        self.fullscreen.clicked.connect(FullcreenChange)

        icon_pose1 = QIcon('./source/pose.png')
        icon_pose2 = QIcon('./source/pose-red.png')
        self.Mode3.setIconSize(size)
        self.Mode3.setIcon(icon_pose1)
        self.Mode3Flag = 0

        def Mode3Change():
            if self.Mode3Flag == 0 and self.VideoOnFlag ==1:
                # mask.show()
                self.label.setToolTip("point1")
                self.Mode3.setIcon(icon_pose2)
                self.Mode3Flag = 1
            elif self.Mode3Flag == 1 and self.VideoOnFlag ==1:
                self.label.setToolTip("")
                self.Mode3.setIcon(icon_pose1)
                self.Mode3Flag = 0

        self.Mode3.clicked.connect(Mode3Change)


        def VideoClose():
            if self.VideoOnFlag == 1:
                self.VideoOnFlag = 0
                self.Mode3.setIcon(icon_pose1)
                self.mode3_activate = False

        self.Close.clicked.connect(VideoClose)


        ############ ???????????? ##############


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "DeepHelmet"))
        self.Mode1.setText(_translate("MainWindow", "???????????????"))
        self.Mode2.setText(_translate("MainWindow", "????????????"))
        self.Mode3.setText(_translate("MainWindow", "????????????"))
        self.fullscreen.setText(_translate("MainWindow", "????????????"))
        self.path_setting.setText(_translate("MainWindow", "????????????"))
        self.record.setText(_translate("MainWindow", "????????????"))
        self.language.setText(_translate("MainWindow", "??????"))
        self.help.setText(_translate("MainWindow", "??????"))
        self.Pause.setText(_translate("MainWindow", "??????"))
        self.Close.setText(_translate("MainWindow", "??????"))
        self.label_3.setText(_translate("MainWindow", "???????????????"))
        self.Status.setText(_translate("MainWindow", "Status: Default"))
        self.illegal.setText(_translate("MainWindow", "illegal: 0"))
        self.label_2.setText(_translate("MainWindow", "output: True"))
        self.AllPeople.setText(_translate("MainWindow", "all person: 0"))
        self.WithoutHM.setText(_translate("MainWindow", "person: 0"))
        self.WithHM.setText(_translate("MainWindow", "hat: 0"))
        self.player.setText(_translate("MainWindow", "player???"))
        self.illegalrecord.setText(_translate("MainWindow", "???????????????"))
        self.Open.setText(_translate("MainWindow", "??????"))
        self.Clear.setText(_translate("MainWindow", "??????"))

    ###########################################

    ########### ????????? ############
    def fun_help(self):
        self.dialog_help.show()
        pass

    def fun_language_setting(self):
        self.dialog_language_setting.show()
        pass

    def fun_path_setting(self):
        self.dialog_path_setting.show()
        pass

    def fun_record_setting(self):
        self.dialog_record_setting.show()
        pass

    def full_screen(self):
        if(self.isFullScreen()==False):
            self.showFullScreen()
        else:
            self.showMaximized()
        pass

    ########### ????????? ############

    def clear_img(self):
        for i in range(self.gridLayout_scroll.count()):
            self.gridLayout_scroll.itemAt(i).widget().deleteLater()
        pass

    def update_time(self):
        self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))
        #self.lcdNumber.display(time.strftime('%Y-%m-%d %X', time.localtime()))

    def show_camera(self):
        ret, self.image_origin = self.cap.read()
        #ret, self.image_origin = self.cap.read()
        #ret, self.image_origin = self.cap.read()
        if(ret == False):
            self.stop()
        #####yolo detect########
        else:
            self.resize_img((1500, 800))
            self.image = Image.fromarray(self.image_origin)
            self.last_person = self.person
            self.image, self.all_person, self.person, self.hat = self.my_yolo.detect_image(self.image)
            self.img = np.asarray(self.image)
            self.curr_time = timer()
            self.exec_time = self.curr_time - self.prev_time
            self.prev_time = self.curr_time
            self.accum_time = self.accum_time + self.exec_time
            self.curr_fps = self.curr_fps + 1
            if self. accum_time > 1:
                self.accum_time = self.accum_time - 1
                self.fps = "FPS: " + str(self.curr_fps)
                self.fps = "FPS: " + str(self.curr_fps + 20)   #fake
                self.curr_fps = 0
            cv.putText(self.img, text=self.fps, org=(3, 15), fontFace=cv.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.50, color=(255, 0, 0), thickness=2)
            #####yolo detect########

            ######pose detect##########
            if(self.mode3_activate == True):

                # fps_time = 0
                image_h, image_w = self.img.shape[:2]
                humans = self.e.inference(self.image_origin, resize_to_default=(self.w > 0 and self.h > 0), upsample_size=4.0)
                #############human count#############
                for human in humans:
                    for i in range(common.CocoPart.Background.value):
                        if i not in human.body_parts.keys():
                            continue
                        body_part = human.body_parts[i]
                        if ((self.calculate((int(body_part.x * image_w + 0.5)), int(body_part.y * image_h + 0.5)) >= 0) != self.crossing_flag):
                            del human.body_parts[i]
                self.img = TfPoseEstimator.draw_humans(self.img, humans, imgcopy=False)
                cv.line(self.img, (int(self.first_point_x), int(self.first_point_y)),
                        (int(self.second_point_x), int(self.second_point_y)), (0, 0, 255), 1, 4)
                # cv.putText(self.img,
                #             "FPS: %f" % (1.0 / (time.time() - fps_time)),
                #             (10, 10),  cv.FONT_HERSHEY_SIMPLEX, 0.5,
                #             (0, 255, 0), 2)
            ######pose detect##########

            ######Video Saver########
            if(self.save_flag == True):
                self.out.write(self.img)
            ######Video Saver########

            #######show label#########
            self.label_show(Scaled=False)
            #######show label#########
            #######show info#########
            self.show_info()
            #######show info#########

            #######img viewer########
            if(self.person > 0 and self.test_count > 20):
                self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
                image_id = "./Violation Record/"+str(self.test_count)+".jpg"
                cv.imwrite(image_id, self.img)
                print(image_id)
                pixmap = QPixmap(image_id)
                self.addImage(pixmap, image_id)
                print(pixmap)
                QApplication.processEvents()
                self.test_count = 0
                #######img viewer########
            self.test_count += 1
            pass

    def show_info(self):
        _translate = QtCore.QCoreApplication.translate
        if self.langusgeFlag == 'Chinese':
            self.Status.setText(_translate("MainWindow", "????????????: " + self.show_status))
            self.illegal.setText(_translate("MainWindow", "????????????: " + self.crossing))
            self.label_2.setText(_translate("MainWindow", "????????????: " + self.show_output))
            self.AllPeople.setText(_translate("MainWindow", "?????????: " + str(self.all_person)))
            self.WithoutHM.setText(_translate("MainWindow", "???????????????: " + str(self.person)))
            self.WithHM.setText(_translate("MainWindow", "???????????????: " + str(self.hat)))
        elif self.langusgeFlag == 'English':
            self.Status.setText(_translate("MainWindow", "Status: " + self.show_status))
            self.illegal.setText(_translate("MainWindow", "OverstepDetection: " + self.crossing))
            self.label_2.setText(_translate("MainWindow", "Output: " + self.show_output))
            self.AllPeople.setText(_translate("MainWindow", "Staff: " + str(self.all_person)))
            self.WithoutHM.setText(_translate("MainWindow", "Violator: " + str(self.person)))
            self.WithHM.setText(_translate("MainWindow", "Normal: " + str(self.hat)))
        # if self.language_flag == "English":
        #     print("EEEE")

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
        _translate = QtCore.QCoreApplication.translate
        self.mode1_activate = False
        self.mode2_activate = False
        self.vpause = False
        self.timer_camera.stop()
        ####################### Exit #######################
        #if(type(out) == "cv2.VideoWriter"):
        #    out.release()
        if self.langusgeFlag == 'Chinese':
            self.show_status = "??????"
            self.show_output = "??????"
            self.crossing = "??????"
        elif self.langusgeFlag == 'English':
            self.show_status = "Default"
            self.show_output = "True"
            self.crossing = "False"
        self.all_person = 0
        self.person = 0
        self.hat = 0
        self.test_count = 0
        self.show_info()
        ########### reset label ########
        self.init_label()
        ########### reset label ########
        ########### release cap ##############
        if (self.cap != None):
            self.cap.release()
        if (self.out != None):
            self.out.release()
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
            if self.langusgeFlag == 'Chinese':
                self.show_status = "????????????"
            if self.langusgeFlag == 'English':
                self.show_status = "Video"
            self.cap = cv.VideoCapture(0)
            self.videosaver()
            self.timer_camera.start(1)

            self.mode1_activate = True
        pass

    def exec_mode2(self):
        if (self.mode1_activate == True or self.mode2_activate == True):
            self.interrupt()
        if (self.mode1_activate == False and self.mode2_activate == False):
            if self.langusgeFlag == 'Chinese':
                self.show_status = "????????????"
            if self.langusgeFlag == 'English':
                self.show_status = "Video"
            openfile_name = QFileDialog.getOpenFileName(None, 'Select', '', 'MP4 files(*.mp4);;All Files (*)')#return QString
            if(len(openfile_name[0]) != 0):
                self.cap = cv.VideoCapture(openfile_name[0])
                self.videosaver()
                self.timer_camera.start(1)
                self.mode2_activate = True
            else:
                self.stop()
        pass

    def exec_mode3(self):
        if(self.mode1_activate == True or self.mode2_activate == True):
            if(self.mode3_activate == True):
                self.mode3_activate = False
            elif (self.mode3_activate == False):
                self.timer_camera.stop()
                self.get_first_point = False
                self.get_second_point = False
                self.get_thrid_point = False
                self.point_count = 0
                self.get_point_flag = True
                self.first_point_x = 0
                self.first_point_y = 0
                self.second_point_x = 0
                self.second_point_y = 0
                self.third_point_x = 0
                self.third_point_y = 0
                if self.langusgeFlag == 'Chinese':
                    self.crossing = "??????"
                if self.langusgeFlag == 'English':
                    self.crossing = "True"
                self.mode3_activate = True
        pass

        # openfile_name = QFileDialog.getOpenFileName(None, 'Select', '',
        #                                             'MP4 files(*.mp4);;All Files (*)')  # return QString
        # if (len(openfile_name[0]) != 0):
        #     self.cap = cv.VideoCapture(openfile_name[0])
        #     self.timer_camera.start(1)

    # def get_point(self):
    #     self.timer_camera.stop()
    #     while(self.get_first_point == False):
    #         pass

    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if(self.get_point_flag == True):
                self.point_count += 1
                if(self.point_count == 1):
                    self.label.setToolTip("point2")
                    self.first_point_x = self.x
                    self.first_point_y = self.y
                    # print("f_x" + str(self.first_point_x))
                    # print("f_y" + str(self.first_point_y))
                    #draw point#
                    cv.circle(self.img, (int(self.first_point_x), int(self.first_point_y)), 1, (0, 0, 255), 4)
                    self.label_show(Scaled=False, cvt=False)
                    #draw point#

                if (self.point_count == 2):
                    self.label.setToolTip("detect this side")
                    self.second_point_x = self.x
                    self.second_point_y = self.y
                    # print("f_x" + str(self.second_point_x))
                    # print("f_y" + str(self.second_point_y))
                    #draw line#
                    cv.line(self.img,(int(self.first_point_x), int(self.first_point_y)), (int(self.second_point_x), int(self.second_point_y)) , (0, 0, 255), 1, 4)
                    self.label_show(Scaled=False, cvt=False)
                    #draw line#


                if(self.point_count == 3):
                    self.label.setToolTip("begin")
                    self.third_point_x = self.x
                    self.third_point_y = self.y
                    self.slove = self.calculate(self.third_point_x, self.third_point_y)
                    print(self.slove)
                    if(self.slove >= 0):
                        self.crossing_flag = True
                        print("True")
                    elif(self.slove  < 0):
                        self.crossing_flag = False
                        print("False")
                    # print("f_x" + str(self.third_point_x))
                    # print("f_y" + str(self.third_point_y))
                    #caculate direction

                    #caculate direction
                if(self.point_count == 4):
                    self.label.setToolTip("")
                    self.timer_camera.start()
                    self.get_point_flag =False
                    self.point_count = 0


    def calculate(self, line_x, line_y):
        slove = line_y - ((self.second_point_y - self.first_point_y) / (
                    self.second_point_x - self.first_point_x) * line_x - (
                                          self.second_point_y - self.first_point_y) / (
                                          self.second_point_x - self.first_point_x) * self.first_point_x + self.first_point_y)

        return slove

    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            self.label.frameGeometry().setTopLeft(QPoint(self.label.frameGeometry().x(), self.label.frameGeometry().y()))

    def mouseMoveEvent(self, event):
        #print(self.label.frameGeometry().x())
        _translate = QtCore.QCoreApplication.translate
        s = event.windowPos()
        #self.setMouseTracking(True)
        # print('mx'+str(s.x()))
        # print('my'+str(s.y()))
        # print('lx'+str(self.label.frameGeometry().x()))
        # print('ly'+str(self.label.frameGeometry().y()))
        self.x = s.x()- self.label.frameGeometry().x()
        self.y = s.y()- self.label.frameGeometry().y()
        #self.AllPeople.setText(_translate("MainWindow",'X:' + str(self.label.frameGeometry().x())))
        #self.WithoutHM.setText(_translate("MainWindow",'Y:' + str(self.label.frameGeometry().y())))
        #self.AllPeople.setText(_translate("MainWindow",'X:' + str(self.x)))
        #self.WithoutHM.setText(_translate("MainWindow",'Y:' + str(self.y)))
    def openfolder(self):
        os.system('xdg-open "%s"' % self.foldername)
        pass


    def videosaver(self):
        fps = self.cap.get(cv.CAP_PROP_FPS)
        fps = fps
        size = (int( self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        #out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        #self.out = cv.VideoWriter(self.output_path, fourcc, 30, size)
        self.out = cv.VideoWriter(self.output_path, fourcc, 30.0, (1500, 800))


    def resize_img(self, a):
        self.image_origin = cv.resize(self.image_origin, a)

    def label_show(self, Scaled=False, cvt=True):
        #self.resize_img((1400, 800))
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = bytesPerComponent * width
        if(cvt==True):
            cv.cvtColor(self.img, cv.COLOR_BGR2RGB, self.img)
        self.qt_img = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        if(Scaled==True):
            self.label.setScaledContents(True)## ??????
        else:
            self.label.setScaledContents(False)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.qt_img))

    def init_label(self):
        # self.img = cv.imread("label1.jpg")
        self.img = cv.imread("./source/9371091.png")
        #res = cv2.resize(img, (1340, 1104), interpolation=cv2.INTER_CUBIC)
        self.img = cv.resize(self.img,(1500,800),0, 0, interpolation=cv.INTER_CUBIC)
        self.label_show(Scaled=False)
        #self.label_show()

    def interrupt(self):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'??????', u'????????????????????????')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'??????')
        cancel.setText(u'??????')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            pass
        else:
            # self.VideoOnFlag = 0
            self.stop()
            self.mode1_activate = False
            self.mode2_activate = False
            #event.accept()
            pass

    ####### image viewer #############
    def open(self):
        file_path = QFileDialog.getExistingDirectory(None, '??????????????????', '/')
        if file_path == None:
            QMessageBox.information(None, '??????', '??????????????????????????????')
        else:
            self.initial_path = file_path
            print(file_path)

    def start_img_viewer(self):
        if self.initial_path:
            file_path = self.initial_path
            print('file_path???{}'.format(file_path))
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
                    QMessageBox.warning(self, '??????', '????????????????????????')
                    self.event(exit())
            else:
                QMessageBox.warning(self, '??????', '????????????????????????')
        else:
            QMessageBox.warning(self, '??????', '????????????????????????')

    def loc_fil(self, stre):
        print('???????????????{}'.format(stre))
        self.initial_path = stre

    def geng_path(self, loc):
        print('???????????????????????????{}'.format(loc))

    def gen_type(self, type):
        print('??????????????????????????????{}'.format(type))

    def addImage(self, pixmap, image_id):
        # ???????????????
        nr_of_columns = self.get_nr_of_image_columns()
        # ????????????????????????
        nr_of_widgets = self.gridLayout_scroll.count()
        self.max_columns = nr_of_columns
        if self.col < self.max_columns:
            self.col = self.col + 1
        else:
            self.col = 0
            self.row += 1

        print('?????????{}'.format(self.row))
        print('???????????????????????????????????????{}'.format(nr_of_widgets))

        print('?????????{}'.format(self.col))
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
        # ?????????????????????
        scroll_area_images_width = self.width
        if scroll_area_images_width > self.displayed_image_size:

            pic_of_columns = scroll_area_images_width // self.displayed_image_size  # ????????????????????????
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
            ###????????????????????????
            self.lable2.adjustSize()
            self.layout.addWidget(self.lable2)
        self.setLayout(self.layout)

    clicked = pyqtSignal(object)
    rightClicked = pyqtSignal(object)

    def mouseressevent(self, ev):
        print('55555555555555555')
        if ev.button() == Qt.RightButton:
            print('dasdasd')
            # ????????????
            self.rightClicked.emit(self.image_id)
        else:
            self.clicked.emit(self.image_id)

    def imageId(self):
        return self.image_id


class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()
###################################### video #########################################
if __name__ =='__main__':
    app=QApplication(sys.argv)

    # MainWindow=QMainWindow()
    # ui=Ui_MainWindow(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # MainWindow.show()
    # MainWindow.showMaximized()

    mainwindow = Ui_MainWindow()
    styleFile = './source/style.qss'
    qssStyle = CommonHelper.readQss(styleFile)
    mainwindow.setStyleSheet(qssStyle)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #mainwindow.showMaximized()
    mainwindow.showFullScreen()
    sys.exit(app.exec_())



