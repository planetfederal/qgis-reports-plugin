# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import datetime
import site
import sip
for c in ('QDate', 'QDateTime', 'QString', 'QTextStream', 'QTime', 'QUrl', 'QVariant'):
    sip.setapi(c, 2)
from qgis import utils
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ext-libs'))


def _showException(type, value, tb, msg, messagebar=False):
    print(msg)
    logmessage = ''
    for s in traceback.format_exception(type, value, tb):
        logmessage += s.decode('utf-8', 'replace') if hasattr(s, 'decode') else s
    print(logmessage)


def _open_stack_dialog(type, value, tb, msg, pop_error=True):
    print(msg)

utils.showException = _showException
utils.open_stack_dialog = _open_stack_dialog

def mkdir(newdir):
    newdir = newdir.strip('\n\r ')
    if os.path.isdir(newdir):
        pass
    else:
        (head, tail) = os.path.split(newdir)
        if head and not os.path.isdir(head):
            mkdir(head)
        if tail:
            os.mkdir(newdir)

def createreport():
    p = os.path.join(os.path.abspath("."), 'ext-libs')
    site.addsitedir(p)
    import qgissysinfo.systeminfo
    info = qgissysinfo.info_as_text()

    reportsDir = os.path.join(os.path.expanduser("~"), ".qgis2", 'reports')
    if not os.path.exists(reportsDir):
        mkdir(reportsDir)

    i = 1
    filename = "{}-{}.txt".format(datetime.date.today().isoformat(), i)
    fullPath = os.path.join(reportsDir, filename)
    while os.path.exists(fullPath):
        i += 1
        filename = "{}-{}.txt".format(datetime.date.today().isoformat(), i)
        fullPath = os.path.join(reportsDir, filename)

    with open(fullPath, "w") as f:
        f.write(info)

    return fullPath, info

if __name__ == "__main__":
    path, _ = createreport()
    # fix_print_with_import
    print("Report created at " + path)
