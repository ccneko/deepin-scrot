#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 Deepin, Inc.
#               2011 Wang Yong
#
# Author:     Wang Yong <lazycat.manatee@gmail.com>
# Maintainer: Wang Yong <lazycat.manatee@gmail.com>
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
#import gtk.keysyms as keys
from gi.repository import GObject


def getKeyName(keyval):
    '''Get key name.'''
    keyUnicode = Gdk.keyval_to_unicode(keyval)
    if keyUnicode == 0:
        return Gdk.keyval_name(keyval)
    else:
        return str(chr(keyUnicode))
    
def getKeyEventModifiers(keyEvent):
    '''Get key event modifiers.'''
    modifiers = []
    
    # Add Ctrl modifier.
    if keyEvent.state & Gdk.ModifierType.CONTROL_MASK:
        modifiers.append("C")
        
    # Add Alt modifier.
    if keyEvent.state & Gdk.ModifierType.MOD1_MASK:
        modifiers.append("M")
        
    # Don't need add Shift modifier if keyval is upper character.
    if keyEvent.state & Gdk.ModifierType.SHIFT_MASK and not Gdk.keyval_is_upper(keyEvent.keyval):
        modifiers.append("S")
        
    return modifiers

def getKeyEventName(keyEvent):
    '''Get key event name.'''
    if keyEvent.is_modifier:
        return ""
    else:
        keyModifiers = getKeyEventModifiers(keyEvent)
        keyName = getKeyName(keyEvent.keyval)
        
        if keyModifiers == []:
            return keyName
        else:
            return "-".join(keyModifiers) + "-" + keyName
