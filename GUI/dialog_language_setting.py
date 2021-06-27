# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_language_setting.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings, QVariant

class Ui_window_language_setting(object):
    def setupUi(self, window_language_setting):
        self.setting = QSettings("MySoft", "DeepHelmet")
        self.language_flag = self.setting.value("language_flag")
        print(self.language_flag)

        window_language_setting.setObjectName("window_language_setting")
        window_language_setting.resize(516, 364)
        self.buttonBox = QtWidgets.QDialogButtonBox(window_language_setting)
        self.buttonBox.setGeometry(QtCore.QRect(150, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(window_language_setting)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 110, 341, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_flag = QtWidgets.QLabel(self.layoutWidget)
        self.save_flag.setObjectName("save_flag")
        self.horizontalLayout.addWidget(self.save_flag)
        self.Chinese = QtWidgets.QRadioButton(self.layoutWidget)
        self.Chinese.setObjectName("Chinese")
        self.horizontalLayout.addWidget(self.Chinese)
        self.English = QtWidgets.QRadioButton(self.layoutWidget)
        self.English.setObjectName("English")
        self.horizontalLayout.addWidget(self.English)

        self.retranslateUi(window_language_setting)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.cancel)
        self.buttonBox.accepted.connect(window_language_setting.accept)
        self.buttonBox.rejected.connect(window_language_setting.reject)
        self.Chinese.toggled.connect(lambda: self.btnstate(self.Chinese))
        self.English.toggled.connect(lambda: self.btnstate(self.English))
        QtCore.QMetaObject.connectSlotsByName(window_language_setting)
        ############设置button语言###############
        self.button_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
        self.button_save = self.buttonBox.button(QtWidgets.QDialogButtonBox.Save)
        self.button_cancel.setText("取消")
        self.button_save.setText("保存")
        #####################################3


        if(self.language_flag == 'Chinese'):
            self.Chinese.setChecked(True)
        else:
            self.English.setChecked(True)



    def retranslateUi(self, window_language_setting):
        _translate = QtCore.QCoreApplication.translate
        window_language_setting.setWindowTitle(_translate("window_language_setting", "Language"))
        # if self.language_flag == 'English':
        #     window_language_setting.setWindowTitle(_translate("window_language_setting", "Language"))
        # if self.language_flag == 'Chinese':
        #     window_language_setting.setWindowTitle(_translate("window_language_setting", "语言"))
        self.save_flag.setText(_translate("window_language_setting", "语言："))
        self.Chinese.setText(_translate("window_language_setting", "中文"))
        self.English.setText(_translate("window_language_setting", "English"))

    def btnstate(self, btn):
        # 输出按钮1与按钮2的状态，选中还是没选中
        if btn.text() == '中文':
            if btn.isChecked() == True:
                self.language_flag = 'Chinese'

        if btn.text() == "English":
            if btn.isChecked() == True:
                self.language_flag = 'English'

        ########### 需要翻译 setText !!!!!!!!!!!################
        if btn.text() == 'Chinese':
            if btn.isChecked() == True:
                self.language_flag = 'Chinese'

        if btn.text() == "English":
            if btn.isChecked() == True:
                self.language_flag = 'English'

    def save(self):
        self.setting.setValue("language_flag", QVariant(self.language_flag))
        pass


    def cancel(self):
        pass