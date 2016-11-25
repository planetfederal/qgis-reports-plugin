# -*- coding: utf-8 -*-

import os
import datetime
import site


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
    filename = "%s-%s.txt" % (datetime.date.today().isoformat(), i)
    fullPath = os.path.join(reportsDir, filename)
    while os.path.exists(fullPath):
        i += 1
        filename = "%s-%s.txt" % (datetime.date.today().isoformat(), i)
        fullPath = os.path.join(reportsDir, filename)

    with open(fullPath, "w") as f:
        f.write(info)

    return fullPath, info

if __name__ == "__main__":
    path = createreport()
    print "Report created at " + path