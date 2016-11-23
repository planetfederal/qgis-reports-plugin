import os
import subprocess
from qgis.PyQt import uic
import sys
from qgis.PyQt.QtGui import QApplication

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
        self.layout().insertWidget(1, self.bar)

    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.textBrowser.text())
        self.bar.pushMessage("", "Report text was copied to the clipboard", level=QgsMessageBar.SUCCESS, duration=5)

    def openReportFile(self):
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', self.reportFile))
        elif os.name == 'nt':
            os.startfile(self.reportFile)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', self.reportFile))