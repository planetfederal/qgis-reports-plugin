import os
import sys
import site

if __name__ == "__main__":
	path = os.path.join(sys.path[0], 'extlibs')
	site.addsitedir(path)
	from qgissysinfo import createreport
	report, filePath = createreport.createReport()
	print ("Report saved to {}".format(filePath))

