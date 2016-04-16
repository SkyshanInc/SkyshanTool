# -*- coding: utf-8 -*- 

import sys
import os;
import json;

from PyQt4 import QtCore, QtGui
from ui.ui_MainTool import Ui_MainWindow
from CreateBmFWin import CreateBmFWin
import ToolUtil

reload(sys)
sys.setdefaultencoding('utf8') 

PROJ_PATH = "%s/" % (os.path.dirname(os.path.realpath(__file__)),)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    # Maintain the list of browser windows so that they do not get garbage
    # collected.
    _window_list = []

    def __init__(self):
        super(MainWindow, self).__init__()

        MainWindow._window_list.append(self)

        self.setupUi(self)
        self.otherCommonds = []
        self._projPath = None

        QtCore.QObject.connect(self.btn_crtBmF, QtCore.SIGNAL('clicked()'),
                self, QtCore.SLOT('_BtnEventCrtBmf()'))

        self.btn_selProj.clicked.connect(lambda: self._BtnEventSelProjPath())  


    def ReadToolsDirBatCom(self):
        if self._projPath :
            print u"===="
            self.otherCommonds = []
            comFList = ToolUtil.GetAllFileWithWord(self._projPath,".bat")
            self.DrawComToCreate(comFList)
        else:
            QtGui.QMessageBox.about(self, "%s",u"没有工程目录")

    def DrawComToCreate(self,comFList):
        for _file in comFList:
            name = ToolUtil.GetFileName(_file)
            btn = QtGui.QPushButton(self.tr(name))
            com = str(_file)
            # btn.clicked.connect(lambda: self._BtnEventDoCommond(com))
            btn.__Commond__ = com
            btn.clicked.connect(self._BtnEventDoCommond)
            self.lay_otherCom.addWidget(btn)

    def _BtnEventDoCommond(self,com):
        bu = self.sender()
        print str(bu.__Commond__)
        com = bu.__Commond__
        try:
            os.system(com)
        except Exception, e:
            QtGui.QMessageBox.about(self, "错误：%s.%s",ToolUtil.GetFileName(com),ToolUtil.GetFileEndName(com))
        

    @QtCore.pyqtSlot()
    def _BtnEventCrtBmf(self):
        self.hide()
        
        winD = CreateBmFWin(self)
        winD.show()

    @QtCore.pyqtSlot()
    def _BtnEventSelProjPath(self):
        print u"选择工程路径"
        savePath = QtGui.QFileDialog.getExistingDirectory(self,"","select project");
        self.txt_projPath.setText(savePath)
        print(savePath) 
        if savePath != "" :
            self._projPath = unicode( str(savePath),"utf-8")
            self.ReadToolsDirBatCom()

        


