# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_record_setting.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings, QVariant


class Ui_window_record_setting(object):
    def setupUi(self, window_record_setting):
        self.setting = QSettings("MySoft", "DeepHelmet")
        self.output_flag = self.setting.value("output_flag")
        self.record_setting_fps = self.setting.value("record_setting_fps")
        self.record_setting_width = self.setting.value("record_setting_width")
        self.record_setting_height = self.setting.value("record_setting_height")


        window_record_setting.setObjectName("window_record_setting")
        window_record_setting.resize(516, 364)
        self.buttonBox = QtWidgets.QDialogButtonBox(window_record_setting)
        self.buttonBox.setGeometry(QtCore.QRect(150, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(window_record_setting)
        self.widget.setGeometry(QtCore.QRect(50, 80, 442, 107))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.save_flag = QtWidgets.QLabel(self.widget)
        self.save_flag.setObjectName("save_flag")
        self.gridLayout.addWidget(self.save_flag, 0, 0, 1, 1)
        self.Yes = QtWidgets.QRadioButton(self.widget)
        self.Yes.setObjectName("Yes")
        self.gridLayout.addWidget(self.Yes, 0, 1, 1, 1)
        self.No = QtWidgets.QRadioButton(self.widget)
        self.No.setObjectName("No")
        self.gridLayout.addWidget(self.No, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.show_fps = QtWidgets.QLineEdit(self.widget)
        self.show_fps.setObjectName("show_fps")
        self.gridLayout.addWidget(self.show_fps, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.width = QtWidgets.QLineEdit(self.widget)
        self.width.setObjectName("width")
        self.gridLayout.addWidget(self.width, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)

        self.retranslateUi(window_record_setting)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.cancel)
        self.buttonBox.accepted.connect(window_record_setting.accept)
        self.buttonBox.rejected.connect(window_record_setting.reject)
        self.Yes.toggled.connect(lambda: self.btnstate(self.Yes))
        self.No.toggled.connect(lambda: self.btnstate(self.No))
        QtCore.QMetaObject.connectSlotsByName(window_record_setting)
        ############设置button语言###############
        self.button_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
        self.button_save = self.buttonBox.button(QtWidgets.QDialogButtonBox.Save)
        self.button_cancel.setText("取消")
        self.button_save.setText("保存")
        #####################################3


        if(self.output_flag == 'Yes'):
            self.Yes.setChecked(True)
        else:
            self.No.setChecked(True)

        self.show_fps.setText(self.record_setting_fps)
        self.width.setText(self.record_setting_width)
        self.lineEdit.setText(self.record_setting_height)

    def retranslateUi(self, window_record_setting):
        _translate = QtCore.QCoreApplication.translate
        window_record_setting.setWindowTitle(_translate("window_record_setting", "OutputSetting"))
        # self.setWindowTitle('OutputSetting')
        self.save_flag.setText(_translate("window_record_setting", "开启输出："))
        self.Yes.setText(_translate("window_record_setting", "开启"))
        self.No.setText(_translate("window_record_setting", "关闭"))
        self.label_2.setText(_translate("window_record_setting", "输出帧率："))
        self.label.setText(_translate("window_record_setting", "输出分辨率："))


    def btnstate(self, btn):
        # 输出按钮1与按钮2的状态，选中还是没选中
        if btn.text() == '开启':
            if btn.isChecked() == True:
                self.output_flag = 'Yes'

        if btn.text() == "关闭":
            if btn.isChecked() == True:
                self.output_flag = 'No'

        ########### 需要翻译 setText !!!!!!!!!!!################
        if btn.text() == '翻译':
            if btn.isChecked() == True:
                self.output_flag = 'Yes'

        if btn.text() == "翻译":
            if btn.isChecked() == True:
                self.output_flag = 'No'


    def save(self):
        self.record_setting_fps = self.show_fps.text()
        self.record_setting_width = self.width.text()
        self.record_setting_height = self.lineEdit.text()
        self.setting.setValue("output_flag", QVariant(self.output_flag))
        self.setting.setValue("record_setting_fps", QVariant(self.record_setting_fps))
        self.setting.setValue("record_setting_width", QVariant(self.record_setting_width))
        self.setting.setValue("record_setting_height", QVariant(self.record_setting_height))
        pass


    def cancel(self):
        pass