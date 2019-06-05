#-*- coding: UTF-8 -*- 。
import requests
# 从 bs4 中导入 BeautifulSoup

from bs4 import BeautifulSoup
import urllib
import os
import threading

#直接拿来用
def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


# 用一个列表来保存页面的 URL 的
class Spider(threading.Thread):


    def __init__(self,win):
        threading.Thread.__init__(self)
        self.win=win
        self.PAGE_URL_LIST = []
        self.PAGE_URL_LIST_ = []

    def run(self):
        self.Claw()




    def Claw(self):
        self.BASE_PAGE_URL =  'https://www.doutula.com/photo/list/?page='
        self.page = self.win.userText.GetValue()



        if self.page == '':
            self.page = 0
        count = 1
        for x in range(int(self.page)):
            url = self.BASE_PAGE_URL + str(x)
            #添加文本
            self.win.listBox.Append(url)
            #添加一个类
            self.PAGE_URL_LIST_.append(url)
            print ('Downpage %d : %s' % (count, url))
            count = count + 1

            #enumerate用于在for循环中得到计数
        for index, page_url in enumerate(self.PAGE_URL_LIST_, start=1):

            # 地雷
            if self.win.forceStop:

                return
            # 请求这个链接
            response = requests.get(page_url)
            # 使用返回的数据，构建一个 BeautifulSoup 对象,返回二进制响应内容，text是文字内容可能出现乱码，接着放到解析引擎中
            soup = BeautifulSoup(response.content, 'lxml')
            # 获取所有 class='img-responsive lazy image_dtz'的 img 标签,返回列表
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            #写进文件
            for img in img_list:
                #炸弹！炸弹！
                if self.win.forceStop:

                    return
                # 因为 src 属性刚开始获取的是 loading 的图片，因此使用 data-original 比较靠谱
                src = img['data-original']
                # 有些图片是没有 http 的，那么要加一个 http
                if not src.startswith('http'):
                    src = 'http:' + src
                # 获取图片的名称face_url.split('/')[-1]
                filename =u'乌鸦坐飞机'+src.split('/')[-1]
                # 拼接完整的路径
                path = os.path.join('F:\NP_Big_Homework\SpiderMan\image', filename)
                urllib.urlretrieve(src,path ,Schedule)
            self.win.gauge.SetValue((index) * (100 /(count - 1)))
            self.win.listBox.Append('完成一个URL')
        self.win.listBox.Append('所有图片下载完成')






