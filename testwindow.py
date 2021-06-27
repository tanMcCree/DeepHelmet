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

class MaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('background:rgba(0,0,0,102);')
        self.setAttribute(Qt.WA_DeleteOnClose)

class MyWidget(QWidget):
    """测试遮罩的显示效果
    """

    # def show(self):
    #     """重写show，设置遮罩大小与parent一致
    #     """
    #     if self.parent() is None:
    #         return
    #
    #     parent_rect = self.parent().geometry()
    #     self.setGeometry(0, 0, parent_rect.width(), parent_rect.height())
    #     super().show()

    def __init__(self):
        super().__init__()
        # 设置白色背景，方便显示出遮罩
        self.setStyleSheet('background:white;')
        main_layout = QVBoxLayout()
        button = QPushButton('点击显示对话框')
        button.clicked.connect(self.show_dialog)
        main_layout.addStretch(5)
        main_layout.addWidget(button, 1, Qt.AlignCenter)
        self.setLayout(main_layout)
        self.show()

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(QLabel('<font color="red">mask test</font>'))
        dialog.setLayout(dialog_layout)
        mask = MaskWidget(self)
        mask.show()
        dialog.exec()
        mask.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    app.exec_()