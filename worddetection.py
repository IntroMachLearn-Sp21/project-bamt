# -*- coding: utf-8 -*-

#import libraries
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import easyocr#This needs to be installed
from matplotlib import pyplot as plt
import numpy as np


#initialize variables
samples=['stopsign1.jpg','20210308_181807.jpg','yield2.jpg','oneway2.jpg','20210310_173435.jpg','disabled1.jpg']
boo=[]
#boo is just a mega list of all the various words in every image. idk what to call it
wordfeature=[]


#converts the image into text
reader = easyocr.Reader(['en'],gpu=False) 


#appends boo with all the texts from all the images
for i in range(len(samples)):
    boo.append(reader.readtext(samples[i]))


x=1
#appends the word feature vector with an integer.     
for i in range(len(boo)):
    if any("STOP" in s for s in boo[i]):
        if any("BUS" in s for s in boo[i]):
            x=0#This line is filler code just to get an else statement. x is useless
            wordfeature.append(-1)
        else:
            wordfeature.append(1)
    elif any("YIELD" in s for s in boo[i]):
        wordfeature.append(2)
    elif any("SPEED" in s for s in boo[i]):
        wordfeature.append(3)
    elif any("PARKING" in s for s in boo[i]):
        wordfeature.append(4)
    else:
        wordfeature.append(-1)
    
    
    
    
    
    
    