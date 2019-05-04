import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title = title, size=(600, 500))
        self.panel = MyPanel(self)
        #self.panel = wx.Panel(self)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Panel Window")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()