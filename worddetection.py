# -*- coding: utf-8 -*-

#import libraries
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import easyocr#This needs to be installed
import numpy as np

def wordDetection(path):
    #converts the image into text
    reader = easyocr.Reader(['en'],gpu=False) 


    #appends boo with all the texts from all the images
    boo = reader.readtext(path)


    #appends the word feature vector with an integer.     
    if any("STOP" in s for s in boo):
        if any("BUS" in s for s in boo):
            wordfeature = -1
        else:
            wordfeature = 1
    elif any("YIELD" in s for s in boo):
        wordfeature = 2
    elif any("SPEED" in s for s in boo):
        wordfeature = 3
    elif any("PARKING" in s for s in boo):
        wordfeature = 4
    else:
        wordfeature = -1

    return wordfeature
    
    
    
    
    
    
    