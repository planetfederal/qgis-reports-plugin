# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : November 2016, February 2020
    Copyright            : 2016 Boundless, http://boundlessgeo.com
                           2020 Planet Inc, https://planet.com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

# This will get replaced with a git SHA1 when you do a git archiveimport os
__revision__ = '$Format:%H$'

import os
import sys
import subprocess

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QApplication, QSizePolicy
from qgis.core import Qgis
from qgis.gui import QgsMessageBar

WIDGET, BASE = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'reportdialog.ui'))


class ReportDialog(BASE, WIDGET):

    def __init__(self, info, reportFile):
        super(ReportDialog, self).__init__(None)
        self.setupUi(self)

        self.reportFile = reportFile
        self.textBrowser.setText(info)
        self.fileLabel.setText("A copy of the report is available at <a href='#'>%s</a>" % reportFile)
        self.fileLabel.linkActivated.connect(self.openReportFile)
        self.copyToClipboardButton.clicked.connect(self.copyToClipboard)

        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout().insertWidget(0, self.bar)

    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.textBrowser.toPlainText())
        self.bar.pushMessage("", "Report text was copied to the clipboard", level=Qgis.Info, duration=5)

    def openReportFile(self):
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', self.reportFile))
        elif os.name == 'nt':
            os.startfile(self.reportFile)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', self.reportFile))
