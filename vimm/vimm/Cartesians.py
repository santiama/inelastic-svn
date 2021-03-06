# Vimm: Visual Interface to Materials Manipulation
#
# Copyright 2010 Caltech.  Copyright 2005 Sandia Corporation.  Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government
# retains certain rights in this sofware.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  
# USA


#!/usr/bin/env python
# generated by wxGlade 0.3.2 on Thu May 13 15:44:31 2004

import wx
import wx.grid
from vimm.Canvas import Canvas
from vimm.Renderers import RenderOptions, SimpleRenderer
from vimm.NumWrap import array


class Cartesians(wx.Frame):
    def __init__(self, parent, id, material, canvas, render_options, **kwds):
        # begin wxGlade: Cartesians.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, parent, id, "Cartesian Editor", **kwds)

        self.material = material
        self.canvas = canvas
        self.render_options = render_options

        self.create_menus()
        self.create_widgets()
        self.statusbar = self.CreateStatusBar(1, 0)
        
        self.__set_properties()

        self.input_cartesian_data()
        
        self.__do_layout()
        return
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Cartesians.__set_properties
        self.grdCartesians.CreateGrid(len(self.material.geo.atoms), 5)
        self.grdCartesians.SetRowLabelSize(40)
        self.grdCartesians.SetColLabelSize(20)
        self.grdCartesians.SetColLabelValue(0, "Atom")
        self.grdCartesians.SetColLabelValue(1, "Element")
        self.grdCartesians.SetColLabelValue(2, "A")
        self.grdCartesians.SetColLabelValue(3, "B")
        self.grdCartesians.SetColLabelValue(4, "C")
        self.grdCartesians.SetSize((500,500))
        return
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Cartesians.__do_layout
        szrMain = wx.BoxSizer(wx.VERTICAL)
        szrMain.Add(self.grdCartesians, 1, wx.EXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(szrMain)
        szrMain.Fit(self)
        szrMain.SetSizeHints(self)
        self.Fit()
        self.Layout()
        return
        # end wxGlade

    def create_menus(self):
        # Menu Bar
        self.mnuMainMenu = wx.MenuBar()
        self.SetMenuBar(self.mnuMainMenu)
        self.mnuFile = wx.Menu()
        self.mnuFile.Append(wx.NewId(), "Exit", "Exit Cartesian Editor", wx.ITEM_NORMAL)
        self.mnuMainMenu.Append(self.mnuFile, "File")
        return
        # Menu Bar end

    def create_widgets(self):
        self.grdCartesians = wx.grid.Grid(self, -1)
        wx.grid.EVT_GRID_CELL_CHANGE(self, self.cell_change)
        return

    def input_cartesian_data(self):
        for atom in self.material.geo.atoms:
            i = self.material.geo.atoms.index(atom)
            self.grdCartesians.SetCellValue(i,0,atom.get_label()) 
            self.grdCartesians.SetCellValue(i,1,atom.get_symbol())
            x,y,z = atom.get_xyz()
            self.grdCartesians.SetCellValue(i,2, str(x))
            self.grdCartesians.SetCellValue(i,3, str(y))
            self.grdCartesians.SetCellValue(i,4, str(z))

    def cell_change(self, evt):
        row = evt.GetRow()
        col = evt.GetCol()

        if col == 0:
            val = self.grdCartesians.GetCellValue(row,col)
            self.material.geo.atoms[row].set_label(val)
            self.redraw()
        elif col == 1:
            print "You probably shouldn't edit this"
        else:
            new_x = float(self.grdCartesians.GetCellValue(row, 2))
            new_y = float(self.grdCartesians.GetCellValue(row, 3))
            new_z = float(self.grdCartesians.GetCellValue(row, 4))
            new_xyz = array([new_x, new_y, new_z])
            self.material.geo.atoms[row].set_xyz(new_xyz)
            self.redraw()

    def redraw(self):
        shapes = SimpleRenderer(self.material.geo,self.render_options)
        self.canvas.newshapes(shapes, 0)
        
# end of class Cartesians

