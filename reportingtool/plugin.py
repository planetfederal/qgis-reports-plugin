# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : November 2016
    Copyright            : (C) 2016 Boundless, http://boundlessgeo.com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
from __future__ import absolute_import
from builtins import object

__author__ = 'Boundless'
__date__ = 'November 2016'
__copyright__ = '(C) 2016 Boundless, http://boundlessgeo.com'

# This will get replaced with a git SHA1 when you do a git archive

import os
import datetime

from qgis.PyQt.QtCore import QDir
from qgis.PyQt.QtGui import QIcon, QAction

from qgis.core import QgsApplication

import qgissysinfo.systeminfo
import webbrowser

from reportingtool.reportdialog import ReportDialog

class ReportingTool(object):
    def __init__(self, iface):
        self.iface = iface
        try:
            from reportingtool.tests import testerplugin
            from qgistester.tests import addTestModule
            addTestModule(testerplugin, "Reporting tool")
        except:
            pass

        try:
            from lessons import addLessonsFolder
            folder = os.path.join(os.path.dirname(__file__), "_lessons")
            addLessonsFolder(folder)
        except:
            pass

    def initGui(self):
        icon = QIcon(os.path.dirname(__file__) + "reportingtool.png")
        self.action = QAction(icon, "Troubleshooting Information", self.iface.mainWindow())
        self.action.setObjectName("startreportingtool")
        self.action.triggered.connect(self.run)

        self.separator = QAction(self.iface.mainWindow())
        self.separator.setObjectName("reportingtoolseparator")
        self.separator.setSeparator(True)

        helpMenu = self.iface.helpMenu()
        for action in helpMenu.actions():
            if action.objectName() == "mActionNeedSupport":
                helpMenu.insertActions(action, [self.action, self.separator])

    def unload(self):
        helpMenu = self.iface.helpMenu()
        helpMenu.removeAction(self.action)
        helpMenu.removeAction(self.separator)

        try:
            from reportingtool.tests import testerplugin
            from qgistester.tests import removeTestModule
            removeTestModule(testerplugin, "Reporting tool")
        except:
            pass

    def run(self):
        from reportingtool import createreport
        fullPath, info = createreport.createreport()

        dlg = ReportDialog(info, fullPath)
        dlg.exec_()
