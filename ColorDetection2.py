import json
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from matplotlib import pyplot as plt
import numpy as np
from cv2 import cv2
import easyocr
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import skimage
from skimage.viewer import ImageViewer
from sklearn.cluster import KMeans
import argparse
import pandas

#image = cv2.imread('StopIdeal5.jpeg')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

data = ["0vb3z2iLdClrRjUt.png","0KTSKyi9y6Lseh4F.png","Bj2SaMA7zbXhKqQc.png","4Tl1KQoKA1L9Ojmo.png","1brETb1XMtyZb9IQ.png","1EZFGgFhqElTDU2w.png","5GxrM9hl0BWla6Do.png","7ayGnCJEC2VBhiwn.png","eILS93wyfWyEX4hG.png"]# 0KTSKyi9y6Lseh4F.png '0vb3z2iLdClrRjUt.png'] 1brETb1XMtyZb9IQ.png 1EZFGgFhqElTDU2w.png
""" image = cv2.imread('3nLBUWJlvgfA8uIA.png')
print("The type of this input is {}".format(type(image)))
print("Shape: {}".format(image.shape))
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image) """
#plt.show()
def ColorFeauture(path):
	boundaries = [([0, 0, 50], [50,56,200]), ([22, 93, 150], [100,255,255]), ([50,0,0], [230,255,60]), ([145, 145, 135], [175,175,175])] #([17, 15, 100], [50, 56, 200]), ([100, 0, 100], [255,50,255]) ([25, 146, 190], [62, 174, 250]) ([0, 100, 0], [250, 200, 250])
#hundred = 100
#twohun = 200
#image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	height1 = 512
	width1 = 512
	height_width = (height1,width1)
	color = []
	image = skimage.io.imread(path)
	# Create  mask
	mask = np.ones(shape=image.shape[0:2], dtype="bool")
	# Draw a filled rectangle on the mask 
	rr, cc = skimage.draw.rectangle(start=(25, 90), end=(373, 444))
	mask[rr, cc] = False
	image[mask] = 0
	image_resized = cv2.resize(image,height_width)
	image_resized = cv2.cvtColor(image_resized,cv2.COLOR_BGR2RGB)
	#image = cv2.imread(path)
	#image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	#plt.imshow(image)
	#plt.show()
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(image_resized, lower, upper)
		output = cv2.bitwise_and(image_resized, image_resized, mask = mask)
		np.hstack([image_resized,output])
		# show the images
		#cv2.imshow("images", np.hstack([image_resized, output]))
		cv2.waitKey(0)
		test2 = cv2.countNonZero(mask)
		print(test2)
		if cv2.countNonZero(mask) > 20000 and cv2.countNonZero(mask) < 30000 or cv2.countNonZero(mask)> 70000 and cv2.countNonZero(mask) < 80000:
			color.append(1) # 1 is for red

		#elif cv2.countNonZero(mask) 
		elif cv2.countNonZero(mask) > 51000:
			color.append(2) # 2 is for yellow

		elif cv2.countNonZero(mask) < 51000 and cv2.countNonZero(mask) > 30000:
			color.append(3) # 3 is for blue
		
		elif cv2.countNonZero(mask) > 80000 and cv2.countNonZero(mask) < 90000 and cv2.countNonZero(mask)< 130000:
			color.append(4) #4 is white
		else:
			color.append(-1) # -1 for none of the above
	
	return np.hstack(color)
	print(color)	

#test = cv2.countNonZero(mask[2])
#print(color)
#print(test) 
#ColorFeature("Out")