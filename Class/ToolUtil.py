#coding:utf-8

import sys
import os;
import json;

reload(sys)
sys.setdefaultencoding('utf8') 

class ToolMsgObj(object):
	def ClientMsg(self,key,value):
		pass


def GetFileName(filePath):
	filePath = str(filePath)
	filePath = unicode(filePath,"utf-8")
	name = os.path.basename(filePath).split('.', 1)[0]
	return name

def GetFileEndName(filePath):
	filePath = str(filePath)
	filePath = unicode(filePath,"utf-8")
	name = os.path.basename(filePath).split('.', 1)[1]
	return name