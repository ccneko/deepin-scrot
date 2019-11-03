#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 Deepin, Inc.
#               2011 Hou Shaohui
#
# Author:     Hou Shaohui <houshao55@gmail.com>
# Maintainer: Hou ShaoHui <houshao55@gmail.com>
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

# locale
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os, sys, time
from mainscrot import MainScrot
from window import getScrotPixbuf
from argparse import ArgumentParser
from tipswindow import countdownWindow
from utils import makeMenuItem, getFormatTime
from constant import DEFAULT_FILENAME
saveFiletype = "png"

def openFileDialog(fullscreen=True, filetype='png'):
    '''Save file to file.'''
    pixbuf = getScrotPixbuf(fullscreen)
    dialog = Gtk.FileChooserDialog(
                                   "Save..",
                                   None,
                                   Gtk.FileChooserAction.SAVE,
                                   (Gtk.STOCK_CANCEL, Gtk.ResponseType.REJECT,
                                    Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
        

    dialog.set_default_response(Gtk.ResponseType.ACCEPT)
    dialog.set_position(Gtk.WindowPosition.CENTER)
    dialog.set_local_only(True)
        
    
    dialog.set_current_folder(os.environ['HOME'])
    dialog.set_current_name("%s%s.%s" % (DEFAULT_FILENAME, getFormatTime(), saveFiletype))

       
        

    optionMenu = Gtk.MenuBar()
    optionMenu.set_size_request(155, -1)
    menu = Gtk.Menu()
    menu.set_size_request(155, -1)
    
    pngItem = makeMenuItem('PNG (*.png)',
                 lambda item, data: setSaveFiletype(dialog, 'png'))
    
    jpgItem = makeMenuItem('JPEG (*.jpeg)',
                 lambda item, data: setSaveFiletype(dialog, 'jpeg'))
    
    bmpItem = makeMenuItem('BMP (*.bmp)',
                 lambda item, data: setSaveFiletype(dialog, 'bmp'))
    
    
    
    
    menu.append(pngItem)
    menu.append(jpgItem)
    menu.append(bmpItem)
    #optionMenu.set_menu(menu)
    
    
    hbox = Gtk.HBox()
    hbox.pack_end(optionMenu, expand=False, fill=False, padding=0)
    dialog.vbox.pack_start(hbox, expand=False, fill=False, padding=0)
    hbox.show_all()                          
            
    response = dialog.run()
        
    if response == Gtk.ResponseType.ACCEPT:
        filename = dialog.get_filename()
        pixbuf.savev(filename, filetype, ["quality"], ["100"]) # to allow custom quality later
        print("Save snapshot to %s" % (filename))
    elif response == Gtk.ResponseType.REJECT:
        print('Closed, no files selected')
    dialog.destroy()

def setSaveFiletype(widget, filetype):
    widget.set_current_name("%s%s.%s" % (DEFAULT_FILENAME, getFormatTime(), filetype))
    saveFiletype = filetype
       

def processArguments():
    '''init processArguments '''
    parser = ArgumentParser(usage="Usage: %prog [options] [arg]")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--full", action="store_true", dest="fullscreen", help="Taking the fullscreen shot")
    group.add_argument("-w", "--window", action="store_true", dest="window", help="Taking the currently focused window")
    parser.add_argument("-d", "--delay", dest="delay", type=int, help="wait NUM seconds before taking a shot", metavar="NUM")
    parser.add_argument("-v", "--version", action='version', version='%(prog) 2.0')
    
    args = parser.parse_args()
    if args.fullscreen:
        if args.delay:
            countdownWindow(args.delay) # to fix: timeout before delay (tipswindow.py: glib.timeout_add(1000, ...))
            openFileDialog()
        else:
            openFileDialog()
    elif args.window:
        if args.delay:
            countdownWindow(args.delay)
            openFileDialog(False)
        else:
            openFileDialog(False)
    elif args.fullscreen and args.window or args.delay:
        countdownWindow(args.delay)
        MainScrot()
    else:
         MainScrot()
        
        

if __name__ == '__main__':
    processArguments()
    