import json
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from matplotlib import pyplot as plt
from dominant_color_detection import detect_colors
from skimage import io
from skimage.color import rgb2lab, deltaE_cie76
import numpy as np

def ColorFeauture(path):
	colors, ratios = detect_colors(path, 3)

	colors[0] = colors[0][1:]

	#Separate most dominant color into its respective ints.
	RGB = []
	RGB.append(int(colors[0][0:2], 16))
	RGB.append(int(colors[0][2:4], 16))
	RGB.append(int(colors[0][4:], 16))
	
	#Convert RGB into LAB for more linear color ranges.
	lab = []
	rgb_color = [[RGB[0]/255, RGB[1]/255, RGB[2]/255]]
	lab = rgb2lab(rgb_color)

	temp1 = lab[0][0]
	temp2 = lab[0][1]
	temp3 = lab[0][2]
	
	print(path)
	print(lab)
	color = []
	if(temp1 >= 60 and temp1 <= 80 and temp2 >= -40 and temp2 <= 80 and temp3 >= -128 and temp3 <= -45):
		color.append(1) #Blue
	elif(temp1 >= 30 and temp1 <= 70 and temp2 >= 40 and temp2 <= 128 and temp3 >= 15 and temp3 <= 128):
		color.append(4) #Red
	elif(temp1 >= 70 and temp1 <= 90 and temp2 >= -20 and temp2 <= 20 and temp3 >= 70 and temp3 <= 128):
		color.append(5) #Yellow
	elif(temp1 >= 30 and temp1 <= 80 and temp2 >= -5 and temp2 <= 5 and temp3 >= -20 and temp3 <= 20):
		color.append(6) #White/Grey
	elif(temp1 >= 0 and temp1 <= 10 and temp2 >= -15 and temp2 <= 15 and temp3 >= -15 and temp3 <= 15):
		color.append(7) #Black
	else:
		color.append(-1) #Other
	
	return np.hstack(color)
	