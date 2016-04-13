#coding:utf-8

import sys
import os;
import json;

from PyQt4 import QtCore, QtGui
from ui.ui_MainTool import Ui_MainWindow
from CreateBmFWin import CreateBmFWin

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

        QtCore.QObject.connect(self.btn_crtBmF, QtCore.SIGNAL('clicked()'),
                self, QtCore.SLOT('_BtnEventCrtBmf()'))

    @QtCore.pyqtSlot()
    def _BtnEventCrtBmf(self):
        print u"点中了"
        w = CreateBmFWin()
        self.setCentralWidget(w)


