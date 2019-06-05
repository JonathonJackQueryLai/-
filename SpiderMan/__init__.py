#-*- coding: UTF-8 -*- 。
#测试的
import urllib2

import requests,urllib,os
src=""
src1="http://imgs.xkcd.com/comics/barrel_cropped_(1).jpg"
# urllib.urlretrieve(src,filename='xkcd.png')
r=urllib2.urlopen(src)
r = r.read()
# print r.text
file1=open('F:\NP_Big_Homework\SpiderMan\\1.png','wb')
file1.write(r)
