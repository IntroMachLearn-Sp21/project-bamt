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
   # print(boo)
    
    #appends the word feature vector with an integer.     
    if any("STOP" in s for s in boo) or any("(STOP)" in s for s in boo) or any("STOPI" in s for s in boo) or any("STOP " in s for s in boo):
        if any("BUS" in s for s in boo):
            wordfeature.append(0)
           # print('bus')
        else:
            wordfeature.append(2*2/9)
          #  print('stop')
    elif any("YIELD" in s for s in boo) or any("Yield" in s for s in boo) or any("YIELD/" in s for s in boo) or any("YIELD" in s for s in boo) or any("YIELD," in s for s in boo) or any("YIELD " in s for s in boo):
        wordfeature.append(2*3/9)
      #  print('yield')
    elif any("NO" in s for s in boo) or any("NO PARKING" in s for s in boo) or any("GRASS" in s for s in boo) or any("Nu" in s for s in boo):
        wordfeature.append(0)
      #  print('other')
    elif any("SPEED" in s for s in boo) or any("LIMIT" in s for s in boo) or any("15" in s for s in boo) or any("20" in s for s in boo) or any("10" in s for s in boo) or any("25" in s for s in boo) or any("SPEED LIMIT" in s for s in boo) or any("35" in s for s in boo) or any("45" in s for s in boo) or any("LIMT" in s for s in boo) or any("Limit" in s for s in boo) or any("LimiT" in s for s in boo):
        wordfeature.append(2*4/9)
      #  print('speed')
    elif any("ONE WAY" in s for s in boo) or any("ONE" in s for s in boo) or any("WAY" in s for s in boo):
        wordfeature.append(0)
      #  print('other')
    elif any("TOW AWAY" in s for s in boo) or any("ZONE" in s for s in boo):
        wordfeature.append(0)
     #   print('other')
    elif any("SLOW" in s for s in boo):
        wordfeature.append(0)
      #  print('other')
    elif any("DO NOT" in s for s in boo) or any("ENTER" in s for s in boo) or any("DO NOT ENTER" in s for s in boo):
        wordfeature.append(0)
      #  print('other')
    elif any("NO SOLICITING" in s for s in boo) or any("SOLICITING" in s for s in boo):
        wordfeature.append(0)
       # print('other')
    elif any("PARKING" in s for s in boo) or any("DISABLED" in s for s in boo) or any("PERMIT" in s for s in boo) or any("PARKING BY DISABLED" in s for s in boo) or any("PERMIT ONLY" in s for s in boo) or any("PARKING BY" in s for s in boo) or any("PARKING BY DISABLED" in s for s in boo) or any("ONLY" in s for s in boo) or any("PARKING " in s for s in boo):
        wordfeature.append(2*5/9)
       # print('disabled')
    elif any("VEHICLES MUST" in s for s in boo) or any("AHFAD" in s for s in boo) or any("AHEAD" in s for s in boo) or any("ALCT" in s for s in boo) or any("KHEAD" in s for s in boo):
        wordfeature.append(2*6/9)
       # print('pedestrian')
    elif (len(boo)==0):
        wordfeature.append(2*1/9)
       # print('no words')
    elif (len(boo[0][1]) > 1):
        if (boo[0][1][0] =='S'):
            wordfeature.append(2*7/9)
           # print('syes')
        elif (boo[0][1][0] =='Y'):
            wordfeature.append(2*8/9)
           # print('yyes')
        else:
            wordfeature.append(2*1)
           # print('garbage1')
    else:
        wordfeature.append(2*1)
      #  print('garbage2')

    return np.hstack(wordfeature)
