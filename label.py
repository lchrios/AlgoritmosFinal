import wx

#Comentario de Branch
class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title = title, size=(800, 500))

        self.panel = SelectPanel(self)

class SelectPanel(wx.Panel):
    def __init__(self, parent):
        super(SelectPanel, self).__init__(parent)

        self.label = wx.StaticText(self, label = "Seleccione un algoritmo a ejecutar:", pos =(10, 15))


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(parent=None, title="Proyecto final: Algoritmos")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()
