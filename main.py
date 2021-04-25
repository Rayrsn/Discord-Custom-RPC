#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
      ___           ___           ___           ___     
     /\  \         /\  \         |\__\         /\  \    
    /::\  \       /::\  \        |:|  |       /::\  \   
   /:/\:\  \     /:/\:\  \       |:|  |      /:/\:\  \  
  /::\~\:\  \   /::\~\:\  \      |:|__|__   /::\~\:\  \ 
 /:/\:\ \:\__\ /:/\:\ \:\__\     /::::\__\ /:/\:\ \:\__\
 \/_|::\/:/  / \/__\:\/:/  /    /:/~~/~    \/_|::\/:/  /
    |:|::/  /       \::/  /    /:/  /         |:|::/  / 
    |:|\/__/        /:/  /     \/__/          |:|\/__/  
    |:|  |         /:/  /                     |:|  |    
     \|__|         \/__/                       \|__|    
"""

import wx
from wx.adv import TaskBarIcon as TaskBarIcon
import os
import sys
from wx.core import Icon
import pypresence
from pypresence import Presence
import time

import json
conf=open('config.json')
config=json.load(conf)

client_id=config['Main']['client_id']
state=config['Main']['state']
details=config['Main']['details']
large_image=config['Main']['large_image']
large_text=config['Main']['large_text']
small_image=config['Main']['small_image']
small_text=config['Main']['small_text']
button_label1=config['Main']['button_label1']
button_url1=config['Main']['button_url1']
button_label2=config['Main']['button_label2']
button_url2=config['Main']['button_url2']

cd = dir_path = os.path.dirname(os.path.realpath(__file__))

# PLEASE DON'T REMOVE THESE. IF YOU DO, PLEASE GIVE CREDIT WHEN ASKED ABOUT THE PROGRAM, THANK YOU!!


client_id_App = "827873727396053002"
RPC = Presence(client_id=client_id_App)
RPC.connect()
RPC.update(state="Checkout the Github!", large_image="logo",large_text="Discord Custom RPC", buttons=[{"label": "Github", "url": "https://github.com/Rayrsn/Discord-Custom-RPC"}])

class DemoTaskBarIcon(TaskBarIcon):
    TBMENU_RESTORE = wx.NewIdRef()
    TBMENU_CLOSE   = wx.NewIdRef()
    TBMENU_CHANGE  = wx.NewIdRef()
    TBMENU_REMOVE  = wx.NewIdRef()
    
    def __init__(self, frame):
        TaskBarIcon.__init__(self, wx.adv.TBI_DOCK) 
        self.frame = frame

        img = wx.Image("icon.ico", wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(img)
        self.icon = Icon(bmp)
        self.icon.CopyFromBitmap(bmp)
        self.SetIcon(self.icon, "Discord Custom RPC")
        self.imgidx = 1

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=self.TBMENU_RESTORE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarChange, id=self.TBMENU_CHANGE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRemove, id=self.TBMENU_REMOVE)


    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.TBMENU_RESTORE, "Restore Custom RPC")
        menu.Append(self.TBMENU_CLOSE,   "Close Custom RPC")
        return menu


    def MakeIcon(self, img):
        if "wxMSW" in wx.PlatformInfo:
            img = img.Scale(16, 16)
        elif "wxGTK" in wx.PlatformInfo:
            img = img.Scale(22, 22)
        icon = wx.Icon(img.ConvertToBitmap())
        return icon
        

    def OnTaskBarActivate(self, evt):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()


    def OnTaskBarClose(self, evt):
        wx.CallAfter(self.frame.Close)


    def OnTaskBarChange(self, evt):
        names = [ "default" ]
        name = names[self.imgidx]

        eImg = getattr(self.icon, name)
        self.imgidx += 1
        if self.imgidx >= len(names):
            self.imgidx = 0

        icon = self.MakeIcon(eImg.Image)
        self.SetIcon(icon, "This is a new icon: " + name)


    def OnTaskBarRemove(self, evt):
        self.RemoveIcon()



class frameclass(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((470, 620))
        self.SetTitle("Custom RPC")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("./icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(34, 35, 42))

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        grid_sizer_1 = wx.GridSizer(16, 2, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Client ID: *")
        label_1.SetMinSize((200, 20))
        label_1.SetForegroundColour(wx.Colour(221, 220, 213))
        label_1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
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
        self.button_1.SetBitmap(wx.Bitmap(cd + "/" + "update.bmp", wx.BITMAP_TYPE_ANY), dir=wx.TOP)
        self.button_1.SetBitmapPressed(wx.Bitmap(cd + "/" + "update_pressed.bmp", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(self.button_1, 0, wx.BOTTOM, 0)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self.button_2.SetMinSize((220, 30))
        self.button_2.SetBackgroundColour(wx.Colour(34, 35, 42))
        self.button_2.SetForegroundColour(wx.Colour(34, 35, 42))
        self.button_2.SetBitmap(wx.Bitmap(cd + "/" + "disconnect.bmp", wx.BITMAP_TYPE_ANY), dir=wx.TOP)
        self.button_2.SetBitmapPressed(wx.Bitmap(cd + "/" + "disconnect_pressed.bmp", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(self.button_2, 0, wx.BOTTOM, 0)

        self.panel_1.SetSizer(grid_sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.updatefunc, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.dcfunc, self.button_2)
        self.Bind(wx.EVT_TEXT, self.get_textbox_client_id, self.text_ctrl_1)
        self.Bind(wx.EVT_TEXT, self.get_textbox_details, self.text_ctrl_2)
        self.Bind(wx.EVT_TEXT, self.get_textbox_state, self.text_ctrl_3)
        self.Bind(wx.EVT_TEXT, self.get_textbox_large_img_name, self.text_ctrl_4)
        self.Bind(wx.EVT_TEXT, self.get_textbox_large_img_text, self.text_ctrl_5)
        self.Bind(wx.EVT_TEXT, self.get_textbox_small_img_name, self.text_ctrl_6)
        self.Bind(wx.EVT_TEXT, self.get_textbox_small_img_text, self.text_ctrl_12)
        self.Bind(wx.EVT_TEXT, self.get_textbox_label_btn1, self.text_ctrl_11)
        self.Bind(wx.EVT_TEXT, self.get_textbox_url_btn1, self.text_ctrl_10)
        self.Bind(wx.EVT_TEXT, self.get_textbox_label_btn2, self.text_ctrl_9)
        self.Bind(wx.EVT_TEXT, self.get_textbox_url_btn2, self.text_ctrl_8)
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.text_ctrl_1.ChangeValue(client_id)
        self.text_ctrl_2.ChangeValue(details)
        self.text_ctrl_3.ChangeValue(state)
        self.text_ctrl_4.ChangeValue(large_image)
        self.text_ctrl_5.ChangeValue(large_text)
        self.text_ctrl_6.ChangeValue(small_image)
        self.text_ctrl_12.ChangeValue(small_text)
        self.text_ctrl_11.ChangeValue(button_label1)
        self.text_ctrl_10.ChangeValue(button_url1)
        self.text_ctrl_9.ChangeValue(button_label2)
        self.text_ctrl_8.ChangeValue(button_url2)

        self.tbicon = DemoTaskBarIcon(self)

    def get_textbox_client_id(self, evt):
        client_id_ent = (str(self.text_ctrl_1.GetValue()))
	
    def get_textbox_details(self, evt):
        global details
        details = (str(self.text_ctrl_2.GetValue()))

    def get_textbox_state(self, evt):
        global state
        state = (str(self.text_ctrl_3.GetValue()))

    def get_textbox_large_img_name(self, evt):
        global large_image_name
        large_image_name = (str(self.text_ctrl_4.GetValue()))
        
    def get_textbox_large_img_text(self, evt):
        global large_text
        large_text = (str(self.text_ctrl_5.GetValue()))
        
    def get_textbox_small_img_name(self, evt):
        global small_image_name
        small_image_name = (str(self.text_ctrl_6.GetValue()))
        
    def get_textbox_small_img_text(self, evt):
        global small_text
        small_text = (str(self.text_ctrl_12.GetValue()))

    def get_textbox_label_btn1(self, evt):
        global button_label1
        button_label1 = (str(self.text_ctrl_11.GetValue()))

    def get_textbox_url_btn1(self, evt):
        global button_url1
        button_url1 = (str(self.text_ctrl_10.GetValue()))
             
    def get_textbox_label_btn2(self, evt):
        global button_label2
        button_label2 = (str(self.text_ctrl_9.GetValue()))

    def get_textbox_url_btn2(self, evt):
        global button_url2
        button_url2 = (str(self.text_ctrl_8.GetValue()))
    
    
    
    def updatefunc(self, evt):
        global RPC
        RPC.clear()

        client_id_ent = (str(self.text_ctrl_1.GetValue()))
        details = (str(self.text_ctrl_2.GetValue()))
        state = (str(self.text_ctrl_3.GetValue()))
        large_image_name = (str(self.text_ctrl_4.GetValue()))
        large_text = (str(self.text_ctrl_5.GetValue()))
        small_image_name = (str(self.text_ctrl_6.GetValue()))
        small_text = (str(self.text_ctrl_12.GetValue()))
        button_label1 = (str(self.text_ctrl_11.GetValue()))
        button_url1 = (str(self.text_ctrl_10.GetValue()))
        button_label2 = (str(self.text_ctrl_9.GetValue()))
        button_url2 = (str(self.text_ctrl_8.GetValue()))
        client_id = client_id_ent

        print(client_id)

        enabletime = self.checkbox_2.GetValue()

        if enabletime==True:
                kwargs={}
                if details!="":
                    kwargs['details']=details
                if state!="":
                    kwargs['state']=state
                if large_image_name!="":
                    kwargs['large_image']=large_image_name
                if large_text!="":
                    kwargs['large_text']=large_text
                if small_image_name!="":
                    kwargs['small_image']=small_image_name
                if small_text!="":
                    kwargs['small_text']=small_text
                if button_label1!="" or button_label2!="":
                    kwargs['buttons']=[]
                if button_label1!="" and button_url1!="":
                    firstbutton={'label':str(button_label1),'url':str(button_url1)}
                    kwargs["buttons"].append(firstbutton)
                if button_label2!="" and button_url2!="":
                    secondbutton={'label':str(button_label2),'url':str(button_url2)}
                    kwargs["buttons"].append(secondbutton)
                
                start_time=time.time()
                kwargs['start']=int(start_time)
        elif enabletime==False:
                kwargs={}
                if details!="":
                    kwargs['details']=details
                if state!="":
                    kwargs['state']=state
                if large_image_name!="":
                    kwargs['large_image']=large_image_name
                if large_text!="":
                    kwargs['large_text']=large_text
                if small_image_name!="":
                    kwargs['small_image']=small_image_name
                if small_text!="":
                    kwargs['small_text']=small_text
                if button_label1!="" or button_label2!="":
                    kwargs['buttons']=[]
                if button_label1!="" and button_url1!="":
                    firstbutton={'label':str(button_label1),'url':str(button_url1)}
                    kwargs["buttons"].append(firstbutton)
                if button_label2!="" and button_url2!="":
                    secondbutton={'label':str(button_label2),'url':str(button_url2)}
                    kwargs["buttons"].append(secondbutton)                
        
        RPC = Presence(client_id=client_id)
        RPC.connect()
        print('rpc connected')
        try:
            config['Main']['client_id']=client_id
            config['Main']['state']=state
            config['Main']['details']=details
            config['Main']['large_image']=large_image_name
            config['Main']['large_text']=large_text
            config['Main']['small_image']=small_image_name
            config['Main']['small_text']=small_text
            config['Main']['button_label1']=button_label1
            config['Main']['button_url1']=button_url1
            config['Main']['button_label2']=button_label2
            config['Main']['button_url2']=button_url2
            with open("config.json","w") as new_config:
                json.dump(config,new_config)
            RPC.clear()
            print('rpc closed')
            RPC.update(**kwargs)
        except pypresence.exceptions.InvalidID:
            wx.MessageBox("Invalid Client ID", "Warning" ,wx.OK | wx.ICON_INFORMATION)
        
        

    def dcfunc(self, evt):
        RPC.clear()
        RPC.close()
        print('disconnected')


    def onClose(self, evt):
        
        self.Destroy()
        sys.exit()
        
    def onMinimize(self, event):
        if self.IsIconized():
            self.Hide()

class popup(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Invalid Client ID")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(3, 1, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        grid_sizer_1.Add((240, 20), 0, 0, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "Invalid Client ID")
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((240, 20), 0, 0, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())

        self.Layout()
        



class appclass(wx.App):
    def OnInit(self):
        self.frame = frameclass(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = appclass(0)
    app.MainLoop()
