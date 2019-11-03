#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 Deepin, Inc.
#               2011 Wang Yong
#
# Author:     hou shaohui <houshaohui@linuxdeepin.com>
#
# Maintainer: hou shaohui <houshaohui@linuxdeepin.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class DeepinScrotSetup:
    ''' Deepin-Scrot setup Window '''

    def __init__(self):
        ''' Init. '''
        
        # Init widgets.
        self.window = self.initMainWindow()
        self.window.connect("destroy", lambda w: Gtk.main_quit())
        # self.window.connect("size-allocate", lambda w, a: updateShape(w, a, 4))
        self.generalMainbox = Gtk.VBox(False, 10)
        # setup 
        
        
        self.bodyAlign = Gtk.Alignment()
        self.bodyAlign.set_padding(10, 20, 10, 10)
        
        imageSetupFrame = Gtk.Frame("图片格式")

        imageSetupMainBox = Gtk.VBox()
        imageQualityHbox = Gtk.HBox(False,40)
        self.adj1 = Gtk.Adjustment(0, 0, 110, 10, 10, 10)
        self.imageQualityLabel  = Gtk.Label("质量:")
        self.imageQualityHscale = Gtk.HScale(self.adj1)
        self.imageQualityHscale.set_size_request(190, -1)
        self.imageQualityHscale.set_value_pos(Gtk.POS_RIGHT)
        self.imageQualityHscale.set_digits(0)
        self.imageQualityHscale.set_draw_value(True)
        self.imageQualityHscale.set_update_policy(Gtk.UPDATE_CONTINUOUS)
        imageQualityHbox.pack_start(self.imageQualityLabel, False, False)
        imageQualityHbox.pack_start(self.imageQualityHscale, False, False)
        
        imageFormatHbox = Gtk.HBox(False, 10)
        imageFormatLabel = Gtk.Label("图片格式:")

        
        imageFormatList = Gtk.OptionMenu()
        imageFormatList.set_size_request(180, -1)
        menu = Gtk.Menu()
        pngItem = Gtk.MenuItem("png - PNG 图像格式")
        jpegItem = Gtk.MenuItem("jpeg - JPEG 图像格式")
        bmpItem = Gtk.MenuItem("bmp - BMP 图像格式")
        menu.append(pngItem)
        menu.append(jpegItem)
        menu.append(bmpItem)
        imageFormatList.set_menu(menu)
        imageFormatHbox.pack_start(imageFormatLabel, False, False)
        imageFormatHbox.pack_start(imageFormatList, False, False)
        
        
        imageSetupMainBox.pack_start(imageQualityHbox)
        imageSetupMainBox.pack_start(imageFormatHbox)
        
        imageQualityAlign = Gtk.Alignment()
        imageQualityAlign.set_padding(10, 10, 10, 10)
        imageQualityAlign.add(imageSetupMainBox)
        imageSetupFrame.add(imageQualityAlign)
        
        # save 
        saveProjectFrame = Gtk.Frame("保存方案")
        saveProjectMainbox = Gtk.VBox()
        self.tipsaveRadio = Gtk.RadioButton(None, "提示保存")
        self.autosaveRadio = Gtk.RadioButton(self.tipsaveRadio, "自动保存")
        saveFilenameHbox = Gtk.HBox(False, 26)
        saveFilenameLabel = Gtk.Label("文件名:")
        self.saveFilenameEntry = Gtk.Entry()
        saveFilenameHbox.pack_start(saveFilenameLabel, False, False)
        saveFilenameHbox.pack_start(self.saveFilenameEntry)
        
        saveDirHbox = Gtk.HBox(False, 10)
        saveDirLabel = Gtk.Label("保存目录:")
        self.saveDirButton = Gtk.FileChooserButton("dir")
        self.saveDirButton.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        saveDirHbox.pack_start(saveDirLabel, False, False)
        saveDirHbox.pack_start(self.saveDirButton)
        saveDirMainbox = Gtk.VBox()
        
        saveDirMainbox.pack_start(saveFilenameHbox)
        saveDirMainbox.pack_start(saveDirHbox)
        saveDirAlign = Gtk.Alignment()
        saveDirAlign.set_padding(0, 0, 20, 10)
        saveDirAlign.add(saveDirMainbox)
        
        saveProjectAlign = Gtk.Alignment()
        saveProjectAlign.set_padding(10, 10, 10, 10)
        
        saveProjectFrame.add(saveProjectAlign)
        saveProjectAlign.add(saveProjectMainbox)
        saveProjectMainbox.pack_start(self.tipsaveRadio)
        saveProjectMainbox.pack_start(self.autosaveRadio)
        saveProjectMainbox.pack_start(saveDirAlign)
        
        # buttons
        controlBox = Gtk.HBox(True, 5)
        controlAlign = Gtk.Alignment()
        controlAlign.set(1.0, 0.0, 0.0, 0.0)
        controlAlign.add(controlBox)
        
        okButton = Gtk.Button(None, Gtk.STOCK_OK)
        cancelButton = Gtk.Button(None, Gtk.STOCK_CANCEL)
        applyButton = Gtk.Button(None, Gtk.STOCK_APPLY)
        controlBox.pack_start(okButton)
        controlBox.pack_start(cancelButton)
        controlBox.pack_start(applyButton)
        
        
        
        self.window.add(self.bodyAlign)
        self.bodyAlign.add(self.generalMainbox)
        self.generalMainbox.pack_start(imageSetupFrame)
        self.generalMainbox.pack_start(saveProjectFrame)
        self.generalMainbox.pack_start(controlAlign)
        

        

        
        self.window.show_all()
        Gtk.main()
  
        
    def initMainWindow(self):
        '''init Main Window'''
        window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        # window.set_decorated(False)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_title("Deepin Scrot")
        window.set_default_size(300, 517)
        window.set_resizable(False)
        window.set_icon_from_file("../theme/logo/deepin-scrot.ico")
        
        return window
        
if __name__ == '__main__':
    DeepinScrotSetup()
