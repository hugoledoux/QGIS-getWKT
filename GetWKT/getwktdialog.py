# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GetWKTDialog
                                 A QGIS plugin
 click on a geometry and see its WKT. That's it.
                             -------------------
        begin                : 2014-03-04
        copyright            : (C) 2014 by Hugo Ledoux
        email                : h.ledoux@tudelft.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_getwkt import Ui_GetWKT
# create the dialog for zoom to point


class GetWKTDialog(QtGui.QDialog, Ui_GetWKT):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        mc = iface.mapCanvas()
        f = mc.currentLayer().selectedFeatures()
        # wkt = f.geometry().exportToWkt()
        self.wktTextEdit.setText("%s" % f[0].geometry().exportToWkt())
