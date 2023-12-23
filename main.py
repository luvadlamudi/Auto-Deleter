
import os
#import time
#import calendar
import shutil
#str(int(calendar.timegm(time.gmtime())))
# main function
def main():

	# specify the path
	path = r"C:\Users\elena\OneDrive\Desktop\testFiles"
	
	# check if there are files in the selected path
	if os.path.exists(path):
		for file in os.walk(path):
			
			if "-ocr" in file:
				os.remove(file)

