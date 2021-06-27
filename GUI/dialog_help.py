# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_help.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window_help(object):
    # def initUI(self):
    #     self.setWindowTitle('Help')
    #     self.show()

    def setupUi(self, window_help):
        window_help.setObjectName("window_help")
        window_help.resize(516, 364)
        self.buttonBox = QtWidgets.QDialogButtonBox(window_help)
        self.buttonBox.setGeometry(QtCore.QRect(160, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(window_help)
        self.textBrowser.setGeometry(QtCore.QRect(100, 30, 301, 231))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(window_help)
        self.buttonBox.accepted.connect(window_help.accept)
        self.buttonBox.rejected.connect(window_help.reject)
        QtCore.QMetaObject.connectSlotsByName(window_help)


        ############设置button语言###############
        self.button_Ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.button_Ok.setText("确定")
        #####################################3


    def retranslateUi(self, window_help):
        _translate = QtCore.QCoreApplication.translate
        # window_help.setWindowTitle(_translate("window_help", "HELP"))
        # self.setWindowTitle('Help')
        #webbrowser.open('http://stackoverflow.com')
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setHtml(
                                 "<div>DeepHelmet是一款用于工地检测工人是否佩戴安全帽,保障施工安全的软件</div>"
                                 "<div><a href='http://localhost:63342/Ubuntu-Yolo/help.html?_ijt=setjtu5qlbaouaps7q2d9ah12b'>了解更多</a><div>"
                                 "<br/>"
                                 "<br/>"
                                 "<div>Deephelmet is a software used to detect whether workers wear safety helmets on the construction site and ensure construction safety</div>"
                                 "<div><a href='http://localhost:63342/Ubuntu-Yolo/help.html?_ijt=setjtu5qlbaouaps7q2d9ah12b'>more</a><div>"
                                )
#         self.textBrowser.setHtml(_translate("window_help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSAJIHJHJKZHXFOAHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS</p></body></html>"))

