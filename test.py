import glob
import json
import os
from ShapeFeature import ShapeFeature, ShapeFeatureTest
from worddetection import wordDetection
from ColorDetection2 import ColorFeauture
from color import ColorFeauture2
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from joblib import dump, load

def writeJSON(path, prediction):
    diction = {}
    count = 0
    for name in path:
        diction[name] = {"signTags": [prediction[count]]}
        count += 1
    with open('prediction.json', 'w') as json_file:
        json.dump(diction, json_file)

def getData(path):
    data = []
    names = []
    for filename in glob.glob(path + "*.png"):
        # Features being used
        data.append(np.concatenate((ShapeFeature(filename), wordDetection(filename), ColorFeauture(filename), ColorFeauture2(filename))))
        #data.append(ShapeFeature(filename))
        name = os.path.split(filename)[-1]
        names.append(name[:-4])
    data = np.vstack(data)
    return data, names

def Test(trainpath):
    test, paths = getData(trainpath)
    forest = load('network.joblib') 
    prediction = forest.predict(test)
    writeJSON(paths, prediction)

if __name__ == "__main__":
    Test("Small Data/Out/") #####################  Change to location of the Test Data ##################################