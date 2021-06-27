# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_path_setting.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSettings, QVariant


class Ui_window_path_setting(object):
    def setupUi(self, window_path_setting):
        self.setting = QSettings("MySoft", "DeepHelmet")
        self.path_setting_record = self.setting.value("path_setting_record")
        self.path_setting_output = self.setting.value("path_setting_output")
        self.directory_output = self.path_setting_output
        self.directory_record = self.path_setting_record

        window_path_setting.setObjectName("window_path_setting")
        window_path_setting.resize(517, 367)
        self.buttonBox = QtWidgets.QDialogButtonBox(window_path_setting)
        self.buttonBox.setGeometry(QtCore.QRect(90, 240, 341, 31))
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(window_path_setting)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 100, 382, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_output_path = QtWidgets.QLabel(self.layoutWidget)
        self.name_output_path.setObjectName("name_output_path")
        self.gridLayout.addWidget(self.name_output_path, 0, 0, 1, 1)
        self.output_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.output_path.setText("")
        self.output_path.setObjectName("output_path")
        self.gridLayout.addWidget(self.output_path, 0, 1, 1, 1)
        self.select_output_path = QtWidgets.QPushButton(self.layoutWidget)
        self.select_output_path.setObjectName("select_output_path")
        self.gridLayout.addWidget(self.select_output_path, 0, 2, 1, 1)
        self.name_record_path = QtWidgets.QLabel(self.layoutWidget)
        self.name_record_path.setObjectName("name_record_path")
        self.gridLayout.addWidget(self.name_record_path, 1, 0, 1, 1)
        self.record_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.record_path.setEnabled(True)
        self.record_path.setObjectName("record_path")
        self.gridLayout.addWidget(self.record_path, 1, 1, 1, 1)
        self.select_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.select_1.setObjectName("select_1")
        self.gridLayout.addWidget(self.select_1, 1, 2, 1, 1)

        self.retranslateUi(window_path_setting)
        self.buttonBox.accepted.connect(window_path_setting.accept)
        self.buttonBox.rejected.connect(window_path_setting.reject)
        self.select_output_path.clicked.connect(self.select_dic_output)
        self.select_1.clicked.connect(self.select_dic_record)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(window_path_setting)
        ############设置button语言###############
        self.button_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
        self.button_save = self.buttonBox.button(QtWidgets.QDialogButtonBox.Save)
        self.button_cancel.setText("取消")
        self.button_save.setText("保存")
        #####################################3


        self.output_path.setText(self.path_setting_output)
        self.record_path.setText(self.path_setting_record)

    def retranslateUi(self, window_path_setting):
        _translate = QtCore.QCoreApplication.translate
        window_path_setting.setWindowTitle(_translate("window_path_setting", "Path"))
        # self.setWindowTitle('Path')
        self.name_output_path.setText(_translate("window_path_setting", "输出路径"))
        self.select_output_path.setText(_translate("window_path_setting", "选择文件夹"))
        self.name_record_path.setText(_translate("window_path_setting", "违规记录路径"))
        self.select_1.setText(_translate("window_path_setting", "选择文件夹"))

    def select_dic_output(self):
        self.directory_output = QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
        self.output_path.setText(self.directory_output)

    def select_dic_record(self):
        self.directory_record = QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
        self.record_path.setText(self.directory_record)

    def cancel(self):
        pass

    def save(self):
        self.path_setting_output = self.directory_output
        self.path_setting_record = self.directory_record
        print("output", self.path_setting_output)
        print("record", self.path_setting_record)
        self.setting.setValue("path_setting_output", QVariant(self.path_setting_output))
        self.setting.setValue("path_setting_record", QVariant(self.path_setting_record))
        pass

