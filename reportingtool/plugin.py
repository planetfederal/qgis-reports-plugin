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

__author__ = 'Boundless'
__date__ = 'November 2016'
__copyright__ = '(C) 2016 Boundless, http://boundlessgeo.com'

# This will get replaced with a git SHA1 when you do a git archive

from qgis.PyQt.QtCore import QDir
from qgis.PyQt.QtGui import QIcon, QAction
from reportdialog import ReportDialog
from qgis.core import QgsApplication
import qgissysinfo.systeminfo
import os
import datetime
import createreport

class ReportingTool:
    def __init__(self, iface):
        self.iface = iface
        try:
            from .tests import testerplugin
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
        self.action = QAction(icon, "Reporting tool", self.iface.mainWindow())
        self.action.setObjectName("startreportingtool")
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("Reporting tool", self.action)

        helpIcon = QgsApplication.getThemeIcon('/mActionHelpAPI.png')
        self.helpAction = QAction(helpIcon, "Reporting tool Help", self.iface.mainWindow())
        self.helpAction.setObjectName("reportingtoolHelp")
        self.helpAction.triggered.connect(lambda: webbrowser.open_new(
                        "file://" + os.path.join(os.path.dirname(__file__), "docs", "html", "index.html")))
        self.iface.addPluginToMenu("Reporting tool", self.helpAction)

    def unload(self):
        self.iface.removePluginMenu("Reporting tool", self.helpAction)
        self.iface.removePluginMenu("Reporting tool", self.action)
        try:
            from .tests import testerplugin
            from qgistester.tests import removeTestModule
            removeTestModule(testerplugin, "Reporting tool")
        except:
            pass

    def run(self):
        fullPath = createreport.createreport()

        dlg = ReportDialog(info, fullPath)
        dlg.exec_()

        
