import glob
import json
import os
from ShapeFeature import ShapeFeature, ShapeFeatureTest
from worddetection import wordDetection
from ColorDetection2 import ColorFeauture
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from joblib import dump, load

def getData(path):
    data = []
    datatruth = []
    f = open(path + "tags.json")
    f = json.load(f)
    for filename in glob.glob(path + "*.png"):
        data.append(np.concatenate((ShapeFeature(filename), wordDetection(filename), ColorFeauture(filename))))
        #data.append(ShapeFeature(filename))
        name = os.path.split(filename)[-1]
        datatruth.append(f[name[:-4]]['signTags'])
        print(f[name[:-4]]['signTags'])
        if (len(f[name[:-4]]['signTags']) < 1):
            data.pop()
            datatruth.pop()
        elif (f[name[:-4]]['signTags'][0] == 'Other') or (f[name[:-4]]['signTags'][0] == 'otherSign'):
            datatruth.pop()
            datatruth.append(['other'])
    data = np.vstack(data)
    datatruth = np.hstack(datatruth)
    return data, datatruth

def Train(trainpath):
    train, traintruth = getData(trainpath)
    forest = RandomForestClassifier(criterion='entropy', n_estimators=100, n_jobs=-1,  max_depth = 20)
    forest.fit(train, traintruth)
    dump(forest, 'network.joblib')

if __name__ == "__main__":
    Train("Small Data/Out/")