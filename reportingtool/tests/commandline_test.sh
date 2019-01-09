#!/bin/bash
# Generate a report and checks for  the presence of
# the main sections and second level sections

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPORT_SCRIPT_CMD="${PYTHON_EXECUTABLE} ${SCRIPT_DIR}/../extlibs/qgissysinfo/createreport.py"
REPORT_PATH=$(${REPORT_SCRIPT_CMD}|sed -e 's/Report saved to //')
echo $REPORT_PATH
REPORT_TEXT=$(cat $REPORT_PATH| sed -e 's/\t/@@/g')


OLDIFS=$IFS
IFS=$'\n'


declare -a SECTIONS=(
"-QGIS plugins"
"-Python information"
"-QGIS providers"
"-QGIS settings"
"-Qt/PyQt information"
"-QGIS information"
"-System information" )

declare -a SUB_SECTIONS=(
"@@-Available Python plugins"
"@@-Active Python plugins"
"@@-Python version"
"@@-Python implementation"
"@@-Exec prefix"
"@@-Python binary path"
"@@-Prefix"
"@@-pip freeze"
"@@-Module search paths"
"@@-Available QGIS data provider plugins"
"@@-Plugin repositories"
"@@-Qt version"
"@@-Qt image plugins"
"@@-Qt library paths"
"@@-Qt database plugins"
"@@-PyQt version"
"@@-SIP version"
"@@-QGIS prefix path"
"@@-QGIS library path"
"@@-QGIS pkg data path"
"@@-QGIS lib exec path"
"@@-QGIS version"
"@@-QGIS application state"
"@@-CPU cores"
"@@-Operating system"
"@@-Installed RAM"
"@@-Hostname"
"@@-User name"
"@@-Home directory"
"@@-Processor" )


function check_section {
    echo -n "Checking for $1 ..."
    EXP=$(echo "$1" | sed -e 's/-/\\-/')
    echo $REPORT_TEXT | grep -q "$EXP"
    if [ "1" == "$?" ]; then
        echo "Test failed for $1!"
        exit 1
    fi
    echo " OK"
}

for section in "${SECTIONS[@]}" ; do
    check_section "$section"
done

for section in "${SUB_SECTIONS[@]}" ; do
    check_section "$section"
done

IFS=$OLDIFS
