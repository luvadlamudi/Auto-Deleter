
import os
import time
import calendar
import shutil
#str(int(calendar.timegm(time.gmtime())))
# main function
def main():

	


	# specify the path
	path = r"C:\Users\elena\OneDrive\Desktop\testFiles"

	

	# checking whether the file is present in path or not
	if os.path.exists(path):

		for file in path:
			if "-ocr" in file:
				




