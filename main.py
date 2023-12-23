#import libraries
import os

# main function
def main():

  # specify the path
  path = r"C:\Users\elena\OneDrive\Desktop\testFiles"

  # check if there are files in the selected path
  if os.path.exists(path):
      for root, dirs, files in os.walk(path):
          for file in files:
              if "-ocr" in file:
                  os.remove(os.path.join(root, file))

if __name__ == "__main__":
    main()
