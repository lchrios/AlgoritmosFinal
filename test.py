import wx


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Radio Button Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)

        rbDivCon = wx.RadioButton(panel, -1, " Divide n' Conquer ")  # , style = wx.RB_GROUP )
        rbMerge  = wx.RadioButton(panel, -1, " Merge List ")
        rbDyna   = wx.RadioButton(panel, -1, " Dynamic Programming ")
        rbWords  = wx.RadioButton(panel, -1, " Words ")
        rbBack   = wx.RadioButton(panel, -1, " Backtracking ")
        rbIP     = wx.RadioButton(panel, -1, " IPv4 ")
        rbBranch = wx.RadioButton(panel, -1, " Branch n' Bound")
        rbDij    = wx.RadioButton(panel, -1, " Dijkstra ")

        rbDivCon.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbMerge.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbDyna.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbWords.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbBack.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbIP.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbBranch.Bind(wx.EVT_RADIOBUTTON, self.onButton)
        rbDij.Bind(wx.EVT_RADIOBUTTON, self.onButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(rbDivCon, 0, wx.ALL, 5)
        sizer.Add(rbMerge, 0, wx.ALL, 5)
        sizer.Add(rbDyna, 0, wx.ALL, 5)
        sizer.Add(rbWords, 0, wx.ALL, 5)
        sizer.Add(rbBack, 0, wx.ALL, 5)
        sizer.Add(rbIP, 0, wx.ALL, 5)
        sizer.Add(rbBranch, 0, wx.ALL, 5)
        sizer.Add(rbDij, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        Map = dict({" Divide n' Conquer " : 0, " Merge List " : 1}, " Dynamic Programming " : 2, " Words " : 3)
    # ----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        btn = event.GetEventObject()
        label = btn.GetLabel()
        message = "You just selected %s" % label
        dlg = wx.MessageDialog(None, message, 'Message',
                               wx.OK | wx.ICON_EXCLAMATION)
        dlg.ShowModal()
        dlg.Destroy()


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()