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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load GetWKT class from file GetWKT
    from getwkt import GetWKT
    return GetWKT(iface)
