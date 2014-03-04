# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GetWKT
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from getwktdialog import GetWKTDialog
import os.path


class GetWKT:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'getwkt_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = GetWKTDialog(self.iface)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/getwkt/icon.png"),
            u"getWKT", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&getWKT", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&getWKT", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        mc = self.iface.mapCanvas()
        mw = self.iface.mainWindow()
        layer = mc.currentLayer()
        if layer is None:
            QMessageBox.warning(mw, "getWKT", "No selected layer")
            return 1
        if layer.selectedFeatureCount() == 0:
            QMessageBox.warning(mw, "getWKT", "No feature selected")
            return 1
        if layer.selectedFeatureCount() > 1:
            QMessageBox.warning(mw, "getWKT", "More than one feature is selected")  
            return 1
        # show the dialog if things are properly selected
        self.dlg.show()
        result = self.dlg.exec_()
        # f = layer.selectedFeatures()[0]
        # wkt = f.geometry().exportToWkt()
        # self.dlg.wktTextEdit.setPlainText(wkt)
        # if result == 1:







            