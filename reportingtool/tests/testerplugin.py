# Tests for the QGIS Tester plugin. To know more see
# https://github.com/boundlessgeo/qgis-tester-plugin

import sys
import unittest

from qgissysinfo.tests import QgisSysInfoTests

try:
    from qgistester.test import Test
except:
    pass


def functionalTests():
    try:
        from qgistester.test import Tests
    except:
        return []

    infoTests = Test("Verify report dialog")
    infoTests.addStep("Open the reporting dialog and verify that it shows system information")
    infoTests.addStep("Verify that 'Copy to clipboard' button works correctly")

    return [infoTests]


def pluginSuite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(QgisSysInfoTests, 'test'))
    return suite


def unitTests():
    _tests = []
    _tests.extend(pluginSuite())
    return _tests


def run_tests():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(pluginSuite())
