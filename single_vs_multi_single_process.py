import glob 
import os
import cv2
import time

start = time.time()
# Loop all image in Genuine folder
for image_filename in glob.glob("Genuine/*.png"):
    # Read image in data
    img = cv2.imread(image_filename)
    
    # resize the image
    img = cv2.resize(img, (600, 600))
    
end = time.time()
print("time: ", end - start)
"""
time:  16.16359257698059
CPU : ~ 12 %
Memory : 22MB
"""

