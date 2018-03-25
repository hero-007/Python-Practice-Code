import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="BRUNO")
        panel = wx.Panel(self)

        ico = wx.Icon('boy.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Bienvenido Sir. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,
                               size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        speak.Speak('''Welcome back Sir, Broono at your service.''')

    def OnEnter(self, event):
        put = self.txt.GetValue()
        put = put.lower()
        link = put.split()
        if put == '':
            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            try:
                put = r.recognize_google(audio)
                put = put.lower()
                link = put.split()
                self.txt.SetValue(put)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}"
                      .format(e))
            except:
                print("Unknown exception occurred!")
