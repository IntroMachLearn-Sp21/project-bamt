import glob
import json
import os
from ShapeFeature import ShapeFeature
from worddetection import wordDetection
from ColorDetection2 import ColorFeauture
from color import ColorFeauture2
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from joblib import dump, load
from tempfile import TemporaryFile

def getData(path):
    data = []
    datatruth = []
    f = open(path + "tags.json")
    f = json.load(f)
    count = 1
    for filename in glob.glob(path + "*.png"):
        print(count)
        count += 1
        # Features being used
        data.append(np.concatenate((ShapeFeature(filename), wordDetection(filename), ColorFeauture(filename), ColorFeauture2(filename))))
        #data.append(ShapeFeature(filename))
        name = os.path.split(filename)[-1]
        try:
            datatruth.append(f[name[:-4]]['signTags'])
            print(f[name[:-4]]['signTags'])
            if (len(f[name[:-4]]['signTags']) < 1):
                data.pop()
                datatruth.pop()
            elif (f[name[:-4]]['signTags'][0] == 'Other') or (f[name[:-4]]['signTags'][0] == 'otherSign'):
                datatruth.pop()
                datatruth.append(['other'])
        except Exception as e:
            data.pop()
    data = np.vstack(data)
    datatruth = np.hstack(datatruth)
    return data, datatruth

def Train(trainpath):
    train, traintruth = getData(trainpath)
    with open('train.npy', 'wb') as f:
        np.save(f, train)
    with open('traintruth.npy', 'wb') as f:
        np.save(f, traintruth)
    forest = RandomForestClassifier(criterion='entropy', n_estimators=100, n_jobs=-1,  max_depth = 20) # Change Forest parameters
    forest.fit(train, traintruth)
    dump(forest, 'network.joblib')

if __name__ == "__main__":
    Train("FullData/") #####################  Change to location of the Training Data ##################################