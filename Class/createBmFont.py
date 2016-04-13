#coding:utf-8
import os;
import json;
import hashlib;
import json;
import subprocess
import argparse
import shutil
import time
import sys
from xml.etree import ElementTree
import ToolUtil

reload(sys)
sys.setdefaultencoding('utf8') 

usage = """
BmFont 文件工具制作 v1.0
注：
    1:通过plist文件生成font文件
    2:plist打包的图片必须是 文字图片 且图片的名称必须是文字命名的
        例：图片文字为 "中" -> 中.png
    
使用方法：
    1.python createBmFont -h 打印帮助信息
    2.python createBmFont -n plist文件名
        注*先将压好的plist,png文件放到BmFontFactor/文件夹
    
"""
BMFONTCFG = """
info face="微软雅黑" size=@itemSize bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=0,0 outline=0
common lineHeight=@lineSize base=95 scaleW=@width scaleH=@height pages=1 packed=0 alphaChnl=1 redChnl=0 greenChnl=0 blueChnl=0
page id=0 file="@pngName"
chars count=@count
"""

#-----------------------------------------------------------------------
nameList = [] 
class createBmFont(object):
    """docstring for createBmFont"""
    def __init__(self,msgObj):
        super(createBmFont, self).__init__()
        self._mPlitP = None
        self._mPngP = None
        self._mSaveP = None
        self._mSaveName = None
        self._mMsgObj = msgObj
        
        
    def tree_to_dict(self,tree):
        d = {}
        for index, item in enumerate(tree):
            if item.tag == 'key':
                if tree[index+1].tag == 'string':
                    d[item.text] = tree[index + 1].text
                elif tree[index + 1].tag == 'true':
                    d[item.text] = True
                elif tree[index + 1].tag == 'false':
                    d[item.text] = False
                elif tree[index+1].tag == 'dict':
                    d[item.text] = self.tree_to_dict(tree[index+1])
        return d

    def gen_png_from_plist(self,plist_filename,cfgContent):
        file_path = plist_filename.replace('.plist', '')

        root = ElementTree.fromstring(open(plist_filename, 'r').read())
        plist_dict = self.tree_to_dict(root[0])
      
        to_list = lambda x: x.replace('{','').replace('}','').split(',')
        
        count = 0
        itemSize = 0
        #读取plist文字的配置信息，生成新的fnt文件信息
        mFntCfgCon = []
        for k,v in plist_dict['frames'].items():
            rectlist = to_list(v['frame'])
            fileName = k.split('.')[0]
            charID = ord(u''+fileName)
            x = int( rectlist[0] )
            y = int( rectlist[1] )
            width = int( rectlist[3] if v['rotated'] else rectlist[2] )
            height = int( rectlist[2] if v['rotated'] else rectlist[3] )
            offsetSize = to_list(v['offset'])
            xoffset = int( offsetSize[0] )
            yoffset = int( offsetSize[1] )

            if itemSize == 0 :
                itemSize = width

            mFntCfgCon.append(str("char id=%s  " % charID))
            mFntCfgCon.append(str("x=%d" % x).ljust(8,' '))
            mFntCfgCon.append(str("y=%d" % y).ljust(8,' '))
            mFntCfgCon.append(str("width=%d" % width).ljust(15,' '))
            mFntCfgCon.append(str("height=%d" % height).ljust(15,' '))
            mFntCfgCon.append(str("xoffset=%d" % xoffset).ljust(12,' '))
            mFntCfgCon.append(str("yoffset=%d" % yoffset).ljust(12,' '))
            mFntCfgCon.append(str("xadvance=%d" % width).ljust(15,' '))
            mFntCfgCon.append(str("page=0").ljust(11,' '))
            mFntCfgCon.append(str("chnl=15").ljust(10,' '))
            mFntCfgCon.append(str("letter=\"%s\"" % fileName))
            mFntCfgCon.append("\n")

            count = count + 1

        metadata = plist_dict['metadata']
        size = to_list(metadata['size'])

        cfgContent = cfgContent.replace("@width",size[0])
        cfgContent = cfgContent.replace("@height",size[1])
        cfgContent = cfgContent.replace("@pngName",str("%s.png" % self._mSaveName))
        cfgContent = cfgContent.replace("@itemSize",str(itemSize))
        cfgContent = cfgContent.replace("@lineSize",str(itemSize-1))

        cfgContent = cfgContent.replace("@count",str(count))
        mFntCfgConStr = ''.join(mFntCfgCon)
        cfgContent = cfgContent + mFntCfgConStr + "\n"

        return cfgContent

    def SaveCfgFont(self,mSaveCfgContent):
        f = open( os.path.join(self._mSaveP, str("%s.fnt" % self._mSaveName)) , "w")
        f.write(mSaveCfgContent)
        f.close()
        savePngPath = os.path.join(self._mSaveP, str("%s.png" % self._mSaveName))
        if savePngPath != self._mPngP :
            shutil.copyfile(self._mPngP,  savePngPath)
        else:
            print u"已经存在%s.png文件" % (self._mSaveName)

    def createFont(self,plitP,pngP,saveP):
        cfgContent = str(BMFONTCFG).lstrip()

        self._mPlitP = plitP
        self._mPngP = pngP
        self._mSaveP = saveP

        self._mSaveName = ToolUtil.GetFileName(pngP) 
        print self._mSaveName

        mSaveCfgContent = None
        if (os.path.exists(self._mPlitP)):
            mSaveCfgContent = self.gen_png_from_plist(self._mPlitP,cfgContent)
        else:
            print u"【无可用生成字库的plist文件】"
            try:
                self._mMsgObj.ClientMsg("Fail",u"【无可用生成字库的plist文件】")
            except Exception, e:
                return 0
            

        if mSaveCfgContent:
            self.SaveCfgFont(mSaveCfgContent)
            try:
                self._mMsgObj.ClientMsg("Success",u"【生成成功！！】")
            except Exception, e:
                return 0
        else:
            try:
                self._mMsgObj.ClientMsg("Fail",u"【无法生成Font文件】")
            except Exception, e:
                return 0
