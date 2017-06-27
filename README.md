[![Build Status](https://travis-ci.org/boundlessgeo/qgis-reports-plugin.svg?branch=master)](https://travis-ci.org/boundlessgeo/qgis-reports-plugin)

#QGIS Reporting tool

A plugin to collect information from your QGIS installation and your system, to help in debugging.

The plugin adds an item in the *Help* menu called "Troubleshooting Information, which opens the reporting dialog.

The report text is shown in the dialog, and also saved to a file in your filesystem. To open that file with your default text editor, click on the link where the filepath to it is displayed, in the lower part of the dialog.

Use the *Copy to clipboard* button to copy the content of the text panel.

#Creating a report from outside QGIS

The reporting plugin uses a library to collect the information need for the report. This library can be called from outside of QGIS, so you can collect that information even if your QGIS installation is broken and QGIS itself cannot be started.

To do so, do the following:

- open a console. It has to be a console that uses the same Python as QGIS, not the system one. For instance, if you installed QGIS in Windows using OSGeo4W, use the OSGeo4W shell.

- move to the folder where you have installed the plugin (usually `[your_user_folder]/.qgis2/python/plugins/reportingtool/ext-libs/qgissysinfo`) and run

```
$ python createreport.py
```

That will create a new report in the reports folder, just like the plugin does when run from QGIS.