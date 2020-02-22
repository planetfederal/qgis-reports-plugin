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

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import site

if __name__ == "__main__":
    path = os.path.join(sys.path[0], 'extlibs')
    site.addsitedir(path)
    from qgissysinfo import createreport
    report, filePath = createreport.createReport()
    print ("Report saved to {}".format(filePath))

