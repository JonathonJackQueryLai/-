#-*- coding: UTF-8 -*- 。
import winsound,threading
class myMusic(threading.Thread):
    def __init__(self,win):
        threading.Thread.__init__(self)
        self.win=win
    def run(self):
        self.OnMusic(self)

    def OnMusic(self, event):
        # music

        #soundFile = 'sound.wav'
        soundFile2 = u'F:\\Users\周柏豪 - 够钟.wav'
        soundFile1 = r'F:\Users\Sissel - Should It Matter.wav'

        while (True):


            music1=winsound.PlaySound(soundFile2, winsound.SND_FILENAME)
            music = winsound.PlaySound(soundFile1, winsound.SND_FILENAME)
