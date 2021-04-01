#import libraries
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import easyocr#This needs to be installed
import numpy as np

def wordDetection(path):
    wordfeature = []
    #converts the image into text
    reader = easyocr.Reader(['en'],gpu=False) 


    #appends boo with all the texts from all the images
    boo = reader.readtext(path)


    #appends the word feature vector with an integer.     
    if any("STOP" in s for s in boo):
        if any("BUS" in s for s in boo):
            wordfeature.append(0)
        else:
            wordfeature.append(2/7)
    elif any("NO" in s for s in boo) or any("NO PARKING" in s for s in boo) or any("GRASS" in s for s in boo):
        wordfeature.append(0)
    elif any("YIELD" in s for s in boo):
        wordfeature.append(3/7)
    elif any("SPEED" in s for s in boo) or any("LIMIT" in s for s in boo) or any("15" in s for s in boo) or any("20" in s for s in boo) or any("10" in s for s in boo) or any("25" in s for s in boo) or any("SPEED LIMIT" in s for s in boo) or any("35" in s for s in boo) or any("45" in s for s in boo):
        wordfeature.append(4/7)
    elif any("PARKING" in s for s in boo) or any("DISABLED" in s for s in boo) or any("PERMIT" in s for s in boo) or any("PARKING BY DISABLED" in s for s in boo) or any("PERMIT ONLY" in s for s in boo) or any("PARKING BY" in s for s in boo) or any("FINE" in s for s in boo):
        wordfeature.append(5/7)
    elif any("ONE WAY" in s for s in boo):
        wordfeature.append(0)
    elif any("TOW AWAY" in s for s in boo) or any("ZONE" in s for s in boo):
        wordfeature.append(0)
    elif any("SLOW" in s for s in boo):
        wordfeature.append(0)
    elif any("DO NOT" in s for s in boo) or any("ENTER" in s for s in boo) or any("DO NOT ENTER" in s for s in boo):
        wordfeature.append(0)
    elif any("NO SOLICITING" in s for s in boo) or any("SOLICITING" in s for s in boo):
        wordfeature.append(0)
    elif any("VEHICLES MUST" in s for s in boo) or any("AHFAD" in s for s in boo) or any("AHEAD" in s for s in boo) or any("ALCT" in s for s in boo):
        wordfeature.append(6/7)
    elif (len(boo)==0):
        wordfeature.append(1/7)
    else:
        wordfeature.append(1)

    return np.hstack(wordfeature)
