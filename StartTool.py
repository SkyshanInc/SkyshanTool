#############################################################################
##
##
#############################################################################
#coding:utf-8
import sys
import os;
import json;

from PyQt4 import QtCore, QtGui

from Class.MainWindow import MainWindow

if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(a.exec_())
