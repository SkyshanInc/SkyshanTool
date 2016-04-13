# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_createBmFont.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CreateBmFont(object):
    def setupUi(self, CreateBmFont):
        CreateBmFont.setObjectName(_fromUtf8("CreateBmFont"))
        CreateBmFont.resize(800, 600)
        CreateBmFont.setMinimumSize(QtCore.QSize(800, 600))
        CreateBmFont.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(CreateBmFont)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 101, 30))
        self.label_2.setStyleSheet(_fromUtf8("font: 16pt \"Helvetica\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_selPlist = QtGui.QPushButton(self.centralwidget)
        self.btn_selPlist.setGeometry(QtCore.QRect(640, 40, 101, 32))
        self.btn_selPlist.setObjectName(_fromUtf8("btn_selPlist"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 101, 30))
        self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Helvetica\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_selPng = QtGui.QPushButton(self.centralwidget)
        self.btn_selPng.setGeometry(QtCore.QRect(640, 100, 101, 32))
        self.btn_selPng.setObjectName(_fromUtf8("btn_selPng"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 101, 30))
        self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Helvetica\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_selSavePath = QtGui.QPushButton(self.centralwidget)
        self.btn_selSavePath.setGeometry(QtCore.QRect(640, 160, 101, 32))
        self.btn_selSavePath.setObjectName(_fromUtf8("btn_selSavePath"))
        self.btn_export = QtGui.QPushButton(self.centralwidget)
        self.btn_export.setGeometry(QtCore.QRect(310, 290, 211, 71))
        self.btn_export.setObjectName(_fromUtf8("btn_export"))
        self.txt_plistPath = QtGui.QLineEdit(self.centralwidget)
        self.txt_plistPath.setGeometry(QtCore.QRect(170, 40, 450, 30))
        self.txt_plistPath.setObjectName(_fromUtf8("txt_plistPath"))
        self.txt_pngPath = QtGui.QLineEdit(self.centralwidget)
        self.txt_pngPath.setGeometry(QtCore.QRect(170, 100, 450, 30))
        self.txt_pngPath.setObjectName(_fromUtf8("txt_pngPath"))
        self.txt_savePath = QtGui.QLineEdit(self.centralwidget)
        self.txt_savePath.setGeometry(QtCore.QRect(170, 160, 450, 30))
        self.txt_savePath.setObjectName(_fromUtf8("txt_savePath"))
        self.btn_back = QtGui.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(0, 0, 110, 32))
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        CreateBmFont.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CreateBmFont)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        CreateBmFont.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CreateBmFont)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CreateBmFont.setStatusBar(self.statusbar)

        self.retranslateUi(CreateBmFont)
        QtCore.QMetaObject.connectSlotsByName(CreateBmFont)

    def retranslateUi(self, CreateBmFont):
        CreateBmFont.setWindowTitle(_translate("CreateBmFont", "MainWindow", None))
        self.label_2.setText(_translate("CreateBmFont", "Png文件：", None))
        self.btn_selPlist.setText(_translate("CreateBmFont", "选择", None))
        self.label_3.setText(_translate("CreateBmFont", "Plist文件：", None))
        self.btn_selPng.setText(_translate("CreateBmFont", "选择", None))
        self.label_4.setText(_translate("CreateBmFont", "输出目录：", None))
        self.btn_selSavePath.setText(_translate("CreateBmFont", "选择", None))
        self.btn_export.setText(_translate("CreateBmFont", "导出", None))
        self.btn_back.setText(_translate("CreateBmFont", "返回", None))

