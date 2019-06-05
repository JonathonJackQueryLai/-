#-*- coding: UTF-8 -*- 。
import  subprocess
import Gui
#查看内容
class Open(object):
    def __init__(self,win):
        pass
    def Open(self, win):
        #subprocess.Popen('explorer.exe 空格(图片存放的路径)', shell=True)
        subprocess.Popen('explorer.exe F:\NP_Big_Homework\SpiderMan\image', shell=True)
       # subprocess.Popen('explorer.exe D:\KuGou2012\KuGou.exe')

