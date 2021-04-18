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
    #print(boo)
    
    #appends the word feature vector with an integer.     
    if any("STOP" in s for s in boo) or any("(STOP)" in s for s in boo) or any("STOPI" in s for s in boo) or any("STOP " in s for s in boo):
        if any("BUS" in s for s in boo):
            wordfeature.append(0)
            print('bus')
        elif any("HERE" in s for s in boo) or any("TO" in s for s in boo):
            wordfeature.append(2*6/10)
        else:
            wordfeature.append(2*2/10)
            print('stop')
    elif any("YIELD" in s for s in boo) or any("Yield" in s for s in boo) or any("YIELD/" in s for s in boo) or any("YIELD" in s for s in boo) or any("YIELD," in s for s in boo) or any("YIELD " in s for s in boo):
        wordfeature.append(2*3/10)
        print('yield')
    elif any("NO" in s for s in boo) or any("NO PARKING" in s for s in boo) or any("GRASS" in s for s in boo) or any("Nu" in s for s in boo):
        wordfeature.append(0)
    elif any("TABLE" in s for s in boo):
        wordfeature.append(0)
    elif any("HUMP" in s for s in boo):
        wordfeature.append(0)
    elif any("BUS" in s for s in boo):
        wordfeature.append(0)
    elif any("SPEED" in s for s in boo) or any("LIMIT" in s for s in boo) or any("15" in s for s in boo) or any("20" in s for s in boo) or any("10" in s for s in boo) or any("25" in s for s in boo) or any("SPEED LIMIT" in s for s in boo) or any("35" in s for s in boo) or any("45" in s for s in boo) or any("LIMT" in s for s in boo) or any("Limit" in s for s in boo)  or any("50" in s for s in boo) or any("MPH" in s for s in boo) or any("M.P.H." in s for s in boo) or any("22" in s for s in boo) or any("40" in s for s in boo):
        wordfeature.append(2*4/10)
        print('speed')
    elif any("ONE WAY" in s for s in boo) or any("ONE" in s for s in boo) or any("WAY" in s for s in boo):
        wordfeature.append(0)
    elif any("TOW AWAY" in s for s in boo) or any("ZONE" in s for s in boo):
        wordfeature.append(0)
    elif any("SLOW" in s for s in boo):
        wordfeature.append(0)
    elif any("CAUTION" in s for s in boo):
        wordfeature.append(0)
    elif any("DETOUR" in s for s in boo):
        wordfeature.append(0)
    elif any("SCHOOL" in s for s in boo):
        wordfeature.append(0)
    elif any("VEHICLES" in s for s in boo):
        wordfeature.append(0)
    elif any("CHILDREN" in s for s in boo) or any("PLAYING" in s for s in boo):
        wordfeature.append(0)
    elif any("NEIGHBORHOOD" in s for s in boo):
        wordfeature.append(0)
    elif any("BIKE LANE" in s for s in boo):
        wordfeature.append(0)
    elif any("MOTOR" in s for s in boo):
        wordfeature.append(0)
    elif any("FIRE" in s for s in boo):
        wordfeature.append(0)
    elif any("COUNTY" in s for s in boo):
        wordfeature.append(0)
    elif any("ON RED" in s for s in boo):
        wordfeature.append(0)
    elif any("WRONG" in s for s in boo) or any("WAY" in s for s in boo):
        wordfeature.append(0)
    elif any("LANE" in s for s in boo):
        wordfeature.append(0)
    elif any("FREIGHT" in s for s in boo):
        wordfeature.append(0)
    elif any("ENDS" in s for s in boo):
        wordfeature.append(0)
    elif any("TURN" in s for s in boo):
        wordfeature.append(0)
    elif any("HUMPS" in s for s in boo):
        wordfeature.append(0)
    elif any("TIME" in s for s in boo):
        wordfeature.append(0)
    elif any("STANDING" in s for s in boo):
        wordfeature.append(0)
    elif any("OUTLET" in s for s in boo):
        wordfeature.append(0)
    elif any("AUTHORIZED" in s for s in boo):
        wordfeature.append(0)
    elif any("REQUIRED" in s for s in boo):
        wordfeature.append(0)
    elif any("RTS" in s for s in boo):
        wordfeature.append(0)
    elif any("AUTONOMOUS" in s for s in boo):
        wordfeature.append(0)
    elif any("SUPERIOR TOWING" in s for s in boo):
        wordfeature.append(0)
    elif any("BIKE ROUTE" in s for s in boo):
        wordfeature.append(0)
    elif any("ROAD" in s for s in boo) or any("WORK" in s for s in boo):
        wordfeature.append(0)
    elif any("TO" in s for s in boo) or any("SOUTH" in s for s in boo):
        wordfeature.append(0)
    elif any("ROAD CLOSED" in s for s in boo) or any("THRU TRAFFIC" in s for s in boo):
        wordfeature.append(0)
    elif any("TRAFFIC" in s for s in boo) or any("CIRCLE" in s for s in boo):
        wordfeature.append(0)
    elif any("PET WASTE" in s for s in boo) or any("PLEASE KEEP" in s for s in boo):
        wordfeature.append(0)
    elif any("STAY AWAY" in s for s in boo) or any("DO NOT FEED" in s for s in boo):
        wordfeature.append(0)
    elif any("R" in s for s in boo) or any("R R" in s for s in boo):
        wordfeature.append(0)
    elif any("SHARE" in s for s in boo) or any("ROAD" in s for s in boo):
        wordfeature.append(0)
    elif any("STREET" in s for s in boo) or any("SWEEPING" in s for s in boo)or any("MONDAY" in s for s in boo):
        wordfeature.append(0)
    elif any("DEAD" in s for s in boo) or any("END" in s for s in boo):
        wordfeature.append(0)
    elif any("KEEP" in s for s in boo) or any("RIGHT" in s for s in boo):
        wordfeature.append(0)
    elif any("DO NOT" in s for s in boo) or any("ENTER" in s for s in boo) or any("DO NOT ENTER" in s for s in boo):
        wordfeature.append(0)
    elif any("NO SOLICITING" in s for s in boo) or any("SOLICITING" in s for s in boo):
        wordfeature.append(0)
    elif any("PARKING" in s for s in boo) or any("DISABLED" in s for s in boo) or any("PERMIT" in s for s in boo) or any("PARKING BY DISABLED" in s for s in boo) or any("PERMIT ONLY" in s for s in boo) or any("PARKING BY" in s for s in boo) or any("PARKING BY DISABLED" in s for s in boo) or any("PARKING " in s for s in boo) or any("TOW-AWAY ZONE" in s for s in boo) or any("MAX FINE" in s for s in boo)  or any("HANDICAPPED" in s for s in boo) or any("FINE" in s for s in boo) or any("VAN" in s for s in boo) or any("PARKING |" in s for s in boo) or any("S250 MAX" in s for s in boo):
        wordfeature.append(2*5/10)
        print('disabled')
    elif any("VEHICLES MUST" in s for s in boo) or any("AHFAD" in s for s in boo) or any("AHEAD" in s for s in boo) or any("ALCT" in s for s in boo) or any("KHEAD" in s for s in boo) or any("3" in s for s in boo) or any("TRAIL" in s for s in boo) or any("500" in s for s in boo) or any("FEET" in s for s in boo) or any("PEDESTRIAN" in s for s in boo):
        wordfeature.append(2*6/10)
        print('pedestrian')
    elif any("ONLY" in s for s in boo):
        wordfeature.append(0)
    elif (len(boo)==0):
        wordfeature.append(2*1/10)
    elif (len(boo[0][1]) > 1):
        if (boo[0][1][0] =='S'):
            wordfeature.append(2*7/10)
        elif (boo[0][1][0] =='Y'):
            wordfeature.append(2*8/10)
        elif (boo[0][1][0] =='P'):
            wordfeature.append(2*9/10)
        else:
            wordfeature.append(2*1)
    else:
        wordfeature.append(2*1)
    return np.hstack(wordfeature)
