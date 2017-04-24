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
from builtins import object

__author__ = 'Boundless'
__date__ = 'November 2016'
__copyright__ = '(C) 2016 Boundless, http://boundlessgeo.com'

# This will get replaced with a git SHA1 when you do a git archive

import os
import sys
import glob
import datetime
import webbrowser
import time
from stat import S_ISREG, ST_CTIME, ST_MODE

from qgis.PyQt.QtCore import QDir
from qgis.PyQt.QtGui import QIcon, QAction

from qgis.core import QgsApplication

from qgissysinfo.createreport import createReport

from reportingtool.reportdialog import ReportDialog

pluginPath = os.path.dirname(__file__)


class ReportingTool(object):
    def __init__(self, iface):
        self.iface = iface
        try:
            from reportingtool.tests import testerplugin
            from qgistester.tests import addTestModule
            addTestModule(testerplugin, "Reporting tool")
        except:
            pass

    def initGui(self):
        icon = QIcon(os.path.dirname(__file__) + "reportingtool.png")
        self.action = QAction(icon, "Boundless Support Tool", self.iface.mainWindow())
        self.action.setObjectName("startreportingtool")
        self.action.triggered.connect(self.run)

        self.separator = QAction(self.iface.mainWindow())
        self.separator.setObjectName("reportingtoolseparator")
        self.separator.setSeparator(True)

        actions = self.iface.mainWindow().menuBar().actions()
        for action in actions:
            if action.menu().objectName() == 'mPluginMenu':
                menuPlugin = action.menu()
                for a in menuPlugin.actions():
                    if a.isSeparator():
                        menuPlugin.insertAction(a, self.action)

        helpMenu = self.iface.helpMenu()
        for action in helpMenu.actions():
            if action.objectName() == "mActionNeedSupport":
                helpMenu.insertActions(action, [self.action, self.separator])

        try:
            from lessons import addLessonsFolder
            folder = os.path.join(os.path.dirname(__file__), "_lessons")
            addLessonsFolder(folder)
        except:
            pass

    def unload(self):
        helpMenu = self.iface.helpMenu()
        helpMenu.removeAction(self.action)
        helpMenu.removeAction(self.separator)

        actions = self.iface.mainWindow().menuBar().actions()
        for action in actions:
            if action.menu().objectName() == 'mPluginMenu':
                menuPlugin = action.menu()
                menuPlugin.removeAction(self.action)

        try:
            from reportingtool.tests import testerplugin
            from qgistester.tests import removeTestModule
            removeTestModule(testerplugin, "Reporting tool")
        except:
            pass

    def run(self):
        os.system("python {}".format(os.path.join(pluginPath, "ext-libs", "qgissysinfo", "createreport.py")))
        filePath = self.lastReport()
        with open(filePath) as f:
            report = f.read()

        dlg = ReportDialog(report, filePath)
        dlg.exec_()

    def lastReport(self):
        reportsPath = os.path.expanduser("~")
        reports = (fn for fn in glob.glob(os.path.join(reportsPath, "QgisSystemReport*")))
        reports = ((os.stat(f), f) for f in reports)
        reports = ((stat[ST_CTIME], f) for stat, f in reports if S_ISREG(stat[ST_MODE]))
        reports = sorted(reports)

        return reports[-1][1]
