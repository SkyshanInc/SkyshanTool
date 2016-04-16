# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_ToolsMainWin.ui'
#
# Created: Sat Apr 16 17:49:54 2016
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_crtBmF = QtGui.QPushButton(self.centralwidget)
        self.btn_crtBmF.setGeometry(QtCore.QRect(20, 60, 201, 61))
        self.btn_crtBmF.setStyleSheet(_fromUtf8("font: 24pt \"Helvetica\";"))
        self.btn_crtBmF.setObjectName(_fromUtf8("btn_crtBmF"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 101, 30))
        self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Helvetica\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_selProj = QtGui.QPushButton(self.centralwidget)
        self.btn_selProj.setGeometry(QtCore.QRect(590, 10, 101, 32))
        self.btn_selProj.setObjectName(_fromUtf8("btn_selProj"))
        self.txt_projPath = QtGui.QLineEdit(self.centralwidget)
        self.txt_projPath.setGeometry(QtCore.QRect(120, 10, 450, 30))
        self.txt_projPath.setObjectName(_fromUtf8("txt_projPath"))
        self.btn_buildIde = QtGui.QPushButton(self.centralwidget)
        self.btn_buildIde.setGeometry(QtCore.QRect(550, 60, 201, 61))
        self.btn_buildIde.setStyleSheet(_fromUtf8("font: 24pt \"Helvetica\";"))
        self.btn_buildIde.setObjectName(_fromUtf8("btn_buildIde"))
        self.btn_buildProj = QtGui.QPushButton(self.centralwidget)
        self.btn_buildProj.setGeometry(QtCore.QRect(300, 60, 201, 61))
        self.btn_buildProj.setStyleSheet(_fromUtf8("font: 24pt \"Helvetica\";"))
        self.btn_buildProj.setObjectName(_fromUtf8("btn_buildProj"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 130, 201, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.lay_otherCom = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.lay_otherCom.setMargin(0)
        self.lay_otherCom.setObjectName(_fromUtf8("lay_otherCom"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_crtBmF.setText(_translate("MainWindow", "创建BmFont", None))
        self.label_3.setText(_translate("MainWindow", "工程目录：", None))
        self.btn_selProj.setText(_translate("MainWindow", "选择", None))
        self.btn_buildIde.setText(_translate("MainWindow", "编译IDE", None))
        self.btn_buildProj.setText(_translate("MainWindow", "编译工程", None))

