# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 10:05
# @Author  : @乌鸦坐飞机
# @Desc    : downingThreading
import threading
import sys
import requests
import re
import random
import time
import os
random.random()
import http
# class MyThread(threading.Thread):
#     def __init__(self,name,value):
#         threading.Thread.__init__(self,name = name)
#         self.value = value
def run():

    # print('Current %s is running ...' % threading.current_thread().name)

    count = 0
    for i in range(60,80):

        url = 'https://www.doutula.com/article/list/?page=%s'%i
        # print('current %s is visiting  %s' % (threading.current_thread().name,url))
        print(url)
        time.sleep(random.random())
        header = {
            'Uer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
            # 'Content - Range':
        }
        req = requests.get(url=url, headers=header)
        content = req.text
        res = re.findall(r'https://www.doutula.com/article/detail/\d+', content)
       
       
            content = req.text
            # print(i)
            res = re.findall('<a href="https://www.doutula.com/article/detail/\d+">.*?</a>', content)

            temp = res[0]
            title = re.findall(r'<a.*?>(.*?)</a>', temp)
            try:
                os.makedirs('F:\\firePic\\%s' % title[0])
            except Exception:
                pass
            Pic = re.findall(r'https://ws\d.sinaimg.cn/large/.*?.jpg|https://ws\d.sinaimg.cn/large/.*?.gif',
                             content)
            for j in Pic:
                try:

                    html = requests.get(j, headers=header)
                    pictures = html.content
                    with open("F:/firePic/%s/" % title[0] + j[-15::], 'wb') as ff:
                        ff.write(pictures)
                except Exception as ex:
                    print(ex)
        # print('current %s is ending  %s' % (threading.current_thread().name, url))

    # end = time.time()


# def run1(value1):
#     time.sleep(random.random())
#     start = time.time()
#     print('Current %s is running ...' % threading.current_thread().name)
#     for i in range(value1, value1+10):
#         count = 0
#         url = 'https://www.doutula.com/article/list/?page=%s' % i
#         header = {
#             'Uer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
#         }
#         req = requests.get(url=url, headers=header)
#         content = req.text
#         # 1-10
#         res = re.findall(r'https://www.doutula.com/article/detail/\d+', content)
#         count = 0
#         for i in res:
#             req = requests.get(i, headers=header)
#             content = req.text
#             # print(i)
#             res = re.findall('<a href="https://www.doutula.com/article/detail/\d+">.*?</a>', content)
#
#             temp = res[0]
#             title = re.findall(r'<a.*?>(.*?)</a>', temp)
#
#             try:
#                 os.makedirs('F:\\firePic\\%s' % title[0])
#             except Exception:
#                 pass
#             Pic = re.findall(r'https://ws\d.sinaimg.cn/large/.*?.jpg|https://ws\d.sinaimg.cn/large/.*?.gif',
#                              content)
#             for j in Pic:
#                 html = requests.get(j, headers=header)
#                 pictures = html.content
#                 with open("F:/firePic/%s/" % title[0] + j[-15::], 'wb') as ff:
#                     ff.write(pictures)
#                     count += 1
#     print('总张数为：%s' % count)
#
#
#     print('Current %s is ended ...time-consuming:%s' % (threading.current_thread().name, end - start))

if __name__ == '__main__':
    start = time.time()
    # t1 = threading.Thread(target=run,name='thread_1',args=([i for i in range(10,20)],))
    # t2 = threading.Thread(target=run,name='thread_2',args=([j for j in range(20,30)],))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    run()
    end = time.time()
    print('time-consuming:%s'%(end - start))








