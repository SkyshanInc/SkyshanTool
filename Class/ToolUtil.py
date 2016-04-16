#coding:utf-8

import sys
import os;
import json;
import platform

plat = platform.system()

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

def GetPlatform():
	return plat

#判断文件中是否包含关键字，是则将文件路径打印出来
def is_file_contain_word(file_list, query_word):
	tempList = []
	for _file in file_list:
		if query_word in _file:
			print _file
			tempList.append(_file)
	print("Finish searching.")

	return tempList
 
#返回指定目录的所有文件（包含子目录的文件）               
def GetAllFileWithWord(floder_path , query_word):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            file_list.append(dirpath + '\\' + name)

    file_list = is_file_contain_word(file_list,query_word)
    return file_list