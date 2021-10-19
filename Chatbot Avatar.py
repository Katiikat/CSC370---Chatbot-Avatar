import wx
from wx.adv import Animation, AnimationCtrl


class Main_Panel(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='W E L C O M E   H U M A N S')
        sizer = wx.BoxSizer(wx.VERTICAL)
        my_animation_asset = Animation('French Guy Chatbot Avatar.gif')
        my_animation_control = AnimationCtrl(self, -1, my_animation_asset)
        my_animation_control.Play()
        sizer.Add(my_animation_control)
        self.SetSizerAndFit(sizer)
        self.Show()
        my_animation_control


if __name__ == '__main__':
    app = wx.App()
    Main_Panel(None)

    app.MainLoop()

    # Potential avatars
    # anime https://giphy.com/gifs/alltheanimeuk-anime-tv-animation-U4vVmILgvI4aQyVuV2
    # anime https://giphy.com/gifs/swimming-anime-ohGsTYBMlOkE
    # Eggs https://giphy.com/gifs/MgqfpGFvuXkGs
    # Weird looking guy https://gfycat.com/acclaimedcreamykitfox
    # Bitmoji?


