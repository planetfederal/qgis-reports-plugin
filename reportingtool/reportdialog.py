import os
import subprocess
from qgis.PyQt import uic
import sys

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

    def openReportFile(self):
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', self.reportFile))
        elif os.name == 'nt':
            os.startfile(self.reportFile)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', self.reportFile))