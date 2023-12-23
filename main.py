
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
    
		for file in os.walk(path):
			
			if "-ocr" in file:
				dirname = os.path.dirname(path)
				file_path = os.path.join(dirname, file)

				remove_file(file_path)

def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")

if __name__ == '__main__':
	main()
