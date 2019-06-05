#-*- coding: UTF-8 -*- 。


import wx


import claw,music,Result
import threading


class mainFram(wx.Frame):

    # 实例化一个窗口对象
    def __init__(self):
        self.count=0

        # 对话框

        wx.Frame.__init__(self, None, title="Python2.7之表情图片爬爬虫", size=(500, 500))
        # 面板
        bkg = wx.Panel(self)
        self.claw1 = claw.Spider(self)
        #埋伏炸弹
        self.forceStop = False
        #music
        self.myMusic=music.myMusic(self)
        #爬取图片结果
        result1 = Result.Open(self)
        # 下栏框
        self.CreateStatusBar()
        self.SetStatusText("欢迎来到乌鸦坐飞机 python2.7 !")

        # 背景颜色
        bkg.SetBackgroundColour(((220),(136),(176)))
        bkg.Refresh()
        self.listBox = wx.ListBox(bkg, -1, pos=(100, 100), size=(300, 200), choices=self.claw1.PAGE_URL_LIST,
                                  style=wx.LB_SINGLE)
        self.listBox.Append('##############请输入url数目################')

         # A StatusBar in the bottom of the window




            # 按钮
        RunButton = wx.Button(bkg, -1, label='Run', pos=(0, 50))
        RunButton.Bind(wx.EVT_BUTTON, self.start)

        OpenButton = wx.Button(bkg, label='Open', pos=(0, 100))
        OpenButton.Bind(wx.EVT_BUTTON, result1.Open)

        StopButton = wx.Button(bkg, label='Stop !', pos=(0, 150))
        StopButton.Bind(wx.EVT_BUTTON, self.forceStopAct)

        musicButton = wx.Button(bkg, label='Music', pos=(0, 200))
        musicButton.Bind(wx.EVT_BUTTON, self.musicStart)


        self.userLabel = wx.StaticText(bkg, -1, "URL个数:")
        self.userText = wx.TextCtrl(bkg, -1, pos=(100, 0))
        # 进度条
        self.gauge = wx.Gauge(bkg, -1, 100, pos=(0, 400), size=(100, 20), style=wx.GA_HORIZONTAL)


            # self.Bind(wx.EVT_IDLE,self.ongauge)
            # self.Bind(wx.EVT_LISTBOX, self.ongauge)
            # 显示结果

    def start(self, event):
        self.claw1.start()

    def musicStart(self, event):
        self.myMusic.setDaemon(True)
        self.myMusic.start()

    def forceStopAct(self, event):
        self.listBox.Append("爬虫已经停止")
        self.forceStop = True



#进度条的方法
    def ongauge(self,event):

        if self.count > int(100):
           self.count = 0
        self.count += 10
        self.gauge.SetValue(self.count)






