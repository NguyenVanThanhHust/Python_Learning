"""
https://towardsdatascience.com/heres-how-you-can-get-a-2-6x-speed-up-on-your-data-pre-processing-with-python-847887e63be5
"""

"""
Split the list of jpg files into 4 smaller groups.
Run 4 separate instances of the Python interpreter.
Have each instance of Python process one of the 4 smaller groups of data.
Combine the results from the 4 processes to get the final list of results
"""

import glob
import os
import cv2
import concurrent.futures
import time

def load_and_resize(image_filename):
  ### Read in the image data
  img = cv2.imread(image_filename)
  
  ### Resize the image
  img = cv2.resize(img, (600, 600)) 
  
  
# Create a pool of processes. By default, one is created for each CPU in machine
if __name__ == '__main__':
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Get a list of files to process
        image_files = glob.glob("Genuine/*.png")
    
        # Process the list of files, split the work the process to use all CPU
        executor.map(load_and_resize, image_files)
    end = time.time()
    print("time: ", end - start)
    
"""
CPU :~ 45 %
time:  2.9080498218536377
"""