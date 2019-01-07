.. (c) 2016 Boundless, http://boundlessgeo.com
   This code is licensed under the GPL 2.0 license.

.. _support_usage:

Usage
=====

Using the *Support Tool*, you can create a report in two ways:

* :ref:`using_qgis_interface`.
* :ref:`using_command_line`.

.. _using_qgis_interface:

Using QGIS's interface
----------------------

In QGIS, to use the *Support Tool*, click the :menuselection:`Help -->
Boundless support tool` menu item.

.. figure:: img/open_report_tool.png

After a few seconds, the :guilabel:`Troubleshooting Information` dialog
opens, already displaying all information that was collected.

.. figure:: img/diagnostics_dialog.png

The report is saved automatically in your file system, in your home folder. You
can open it with the default text editor by clicking the provided link.

You can also copy the full report by clicking the :guilabel:`Copy to clipboard`
button.

.. _using_command_line:

Using the command shell
-----------------------

The *Support Tool* uses a Python library to collect the needed
information for the report. This library can be called from outside of QGIS,
so you can obtain the same information even if your QGIS installation is
broken and QGIS itself cannot be started.

To run the report tool library, do the following:

#. From Boundless Desktop folder open the Console Shell.

   .. figure:: img/open_commnad_shell.png

#. If you are using QGIS from `Boundless Desktop`_ installation, you can simply\
   run the following command::

     createreport

#. If you are using QGIS from the community installers, move to the
   profile folder where you have installed the plugin.

   On Windows, type::

     cd %userprofile%\AppData\Roaming\QGIS\QGIS3\profiles\<profile_name>\python\plugins\reportingtool

   On Mac OX or Linux, type::

     cd ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/reportingtool

   Then, run the following command::

     python createreport.py

The command will create a new report in your home folder, just like the plugin does when used
from inside QGIS.
