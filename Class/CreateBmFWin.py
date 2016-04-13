#coding:utf-8

import sys
import os;
import json;

from PyQt4 import QtCore, QtGui
from ui.ui_CreateBmF import Ui_CreateBmFont
from createBmFont import createBmFont

reload(sys)
sys.setdefaultencoding('utf8') 

PROJ_PATH = "%s/" % (os.path.dirname(os.path.realpath(__file__)),)

class CreateBmFWin(QtGui.QMainWindow, Ui_CreateBmFont):
    _window_list = []

    def __init__(self):
        super(CreateBmFWin, self).__init__()

        CreateBmFWin._window_list.append(self)

        self.setupUi(self)

        QtCore.QObject.connect(self.btn_selPlist, QtCore.SIGNAL('clicked()'),
                self, QtCore.SLOT('_BtnEventSelPlist()'))
        QtCore.QObject.connect(self.btn_selPng, QtCore.SIGNAL('clicked()'),
                self, QtCore.SLOT('_BtnEventSelPng()'))
        QtCore.QObject.connect(self.btn_selSavePath, QtCore.SIGNAL('clicked()'),
                self, QtCore.SLOT('_BtnEventSelSavePath()'))
        QtCore.QObject.connect(self.btn_export, QtCore.SIGNAL('clicked()'),
                self, QtCore.SLOT('_BtnEventSelExport()'))


    @QtCore.pyqtSlot()
    def _BtnEventSelPlist(self):
        print u"选择plist文件"
        plistFile = QtGui.QFileDialog.getOpenFileName(self,"","(.plist)");
        self.txt_plistPath.setText(plistFile)
        print(plistFile)

        pngFile = plistFile.replace(".plist",".png")
        if os.path.isfile(pngFile) :
            self.txt_pngPath.setText(pngFile)
            print(pngFile)


    @QtCore.pyqtSlot()
    def _BtnEventSelPng(self):
        print u"选择png文件"
        pngFile = QtGui.QFileDialog.getOpenFileName(self,"","(.png)");
        self.txt_pngPath.setText(pngFile)
        print(pngFile)

    @QtCore.pyqtSlot()
    def _BtnEventSelSavePath(self):
        print u"选择存储路径"
        savePath = QtGui.QFileDialog.getExistingDirectory(self,"","select project");
        self.txt_savePath.setText(savePath)
        print(savePath) 

    @QtCore.pyqtSlot()
    def _BtnEventSelExport(self):
        plistFile = str(self.txt_plistPath.text())
        pngFile = str(self.txt_pngPath.text())
        savePath = str(self.txt_savePath.text())
        print(plistFile)
        print(pngFile)
        print(savePath)
        createBmFont().createFont(plistFile,pngFile,savePath)


