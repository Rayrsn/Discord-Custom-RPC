#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Sat Apr  3 16:40:12 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class frameclass(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: frameclass.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((470, 620))
        self.SetTitle("Custom RPC")
        self.SetBackgroundColour(wx.Colour(34, 35, 42))

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        grid_sizer_1 = wx.GridSizer(16, 2, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Client ID: *")
        label_1.SetMinSize((200, 20))
        label_1.SetForegroundColour(wx.Colour(221, 220, 213))
        label_1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "\n")
        self.text_ctrl_1.SetMinSize((190, 25))
        self.text_ctrl_1.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.LEFT, 13)

        label_12 = wx.StaticText(self.panel_1, wx.ID_ANY, "Button 1:")
        label_12.SetMinSize((200, 20))
        label_12.SetForegroundColour(wx.Colour(221, 220, 213))
        label_12.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_1.Add(label_12, 0, wx.ALIGN_CENTER | wx.RIGHT, 50)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Details:")
        label_2.SetMinSize((200, 20))
        label_2.SetForegroundColour(wx.Colour(221, 220, 213))
        label_2.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)

        label_8 = wx.StaticText(self.panel_1, wx.ID_ANY, "Label:")
        label_8.SetMinSize((200, 20))
        label_8.SetForegroundColour(wx.Colour(221, 220, 213))
        label_8.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_8, 0, wx.ALIGN_CENTER, 0)

        self.text_ctrl_2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_2.SetMinSize((190, 25))
        self.text_ctrl_2.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.LEFT, 13)

        self.text_ctrl_11 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_11.SetMinSize((190, 25))
        self.text_ctrl_11.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_11, 0, wx.LEFT, 13)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "State:")
        label_3.SetMinSize((200, 20))
        label_3.SetForegroundColour(wx.Colour(221, 220, 213))
        label_3.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)

        label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, "URL:")
        label_9.SetMinSize((200, 20))
        label_9.SetForegroundColour(wx.Colour(221, 220, 213))
        label_9.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_9, 0, wx.ALIGN_CENTER, 0)

        self.text_ctrl_3 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_3.SetMinSize((190, 25))
        self.text_ctrl_3.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_3, 0, wx.LEFT, 13)

        self.text_ctrl_10 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_10.SetMinSize((190, 25))
        self.text_ctrl_10.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_10, 0, wx.LEFT, 13)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Large Image Name:")
        label_4.SetMinSize((200, 20))
        label_4.SetForegroundColour(wx.Colour(221, 220, 213))
        label_4.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.text_ctrl_4 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_4.SetMinSize((190, 25))
        self.text_ctrl_4.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_4, 0, wx.LEFT, 13)

        label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, "Button 2:")
        label_13.SetMinSize((200, 20))
        label_13.SetForegroundColour(wx.Colour(221, 220, 213))
        label_13.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_1.Add(label_13, 0, wx.ALIGN_CENTER | wx.RIGHT, 50)

        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "Large Image Text:")
        label_5.SetMinSize((200, 20))
        label_5.SetForegroundColour(wx.Colour(221, 220, 213))
        label_5.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_5, 0, wx.ALIGN_CENTER, 0)

        label_10 = wx.StaticText(self.panel_1, wx.ID_ANY, "Label:")
        label_10.SetMinSize((200, 20))
        label_10.SetForegroundColour(wx.Colour(221, 220, 213))
        label_10.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_10, 0, wx.ALIGN_CENTER, 0)

        self.text_ctrl_5 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_5.SetMinSize((190, 25))
        self.text_ctrl_5.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_5, 0, wx.LEFT, 13)

        self.text_ctrl_9 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_9.SetMinSize((190, 25))
        self.text_ctrl_9.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_9, 0, wx.LEFT, 13)

        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "Small Image Name:")
        label_6.SetMinSize((200, 20))
        label_6.SetForegroundColour(wx.Colour(221, 220, 213))
        label_6.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_6, 0, wx.ALIGN_CENTER, 0)

        label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, "URL:")
        label_11.SetMinSize((200, 20))
        label_11.SetForegroundColour(wx.Colour(221, 220, 213))
        label_11.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_CENTER, 0)

        self.text_ctrl_6 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_6.SetMinSize((190, 25))
        self.text_ctrl_6.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_6, 0, wx.LEFT, 13)

        self.text_ctrl_8 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_8.SetMinSize((190, 25))
        self.text_ctrl_8.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_8, 0, wx.LEFT, 13)

        label_7 = wx.StaticText(self.panel_1, wx.ID_ANY, "Small Image Text:")
        label_7.SetMinSize((200, 20))
        label_7.SetForegroundColour(wx.Colour(221, 220, 213))
        label_7.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_7, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.text_ctrl_12 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_12.SetMinSize((190, 25))
        self.text_ctrl_12.SetBackgroundColour(wx.Colour(183, 182, 182))
        grid_sizer_1.Add(self.text_ctrl_12, 0, wx.LEFT, 13)

        self.checkbox_2 = wx.CheckBox(self.panel_1, wx.ID_ANY, "Enable Time           ", style=wx.ALIGN_RIGHT)
        self.checkbox_2.SetForegroundColour(wx.Colour(221, 220, 213))
        self.checkbox_2.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_1.Add(self.checkbox_2, 0, wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT, 35)

        static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        static_line_1.SetMinSize((227, 2))
        static_line_1.SetForegroundColour(wx.Colour(255, 0, 0))
        grid_sizer_1.Add(static_line_1, 0, wx.TOP, 16)

        static_line_2 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        static_line_2.SetMinSize((227, 2))
        static_line_2.SetForegroundColour(wx.Colour(255, 0, 0))
        grid_sizer_1.Add(static_line_2, 0, wx.TOP, 16)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self.button_1.SetMinSize((220, 30))
        self.button_1.SetBackgroundColour(wx.Colour(34, 35, 42))
        self.button_1.SetForegroundColour(wx.Colour(34, 35, 42))
        self.button_1.SetBitmap(wx.Bitmap(".\\update.bmp", wx.BITMAP_TYPE_ANY), dir=wx.TOP)
        self.button_1.SetBitmapPressed(wx.Bitmap(".\\update_pressed.bmp", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(self.button_1, 0, wx.BOTTOM, 0)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self.button_2.SetMinSize((220, 30))
        self.button_2.SetBackgroundColour(wx.Colour(34, 35, 42))
        self.button_2.SetForegroundColour(wx.Colour(34, 35, 42))
        self.button_2.SetBitmap(wx.Bitmap(".\\disconnect.bmp", wx.BITMAP_TYPE_ANY), dir=wx.TOP)
        self.button_2.SetBitmapPressed(wx.Bitmap(".\\disconnect_pressed.bmp", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(self.button_2, 0, wx.BOTTOM, 0)

        self.panel_1.SetSizer(grid_sizer_1)

        self.Layout()
        # end wxGlade

# end of class frameclass

class appclass(wx.App):
    def OnInit(self):
        self.frame = frameclass(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class appclass

if __name__ == "__main__":
    app = appclass(0)
    app.MainLoop()
