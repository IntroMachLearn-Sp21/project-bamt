import glob
import json
from ShapeFeature import ShapeFeature
from worddetection import wordDetection
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import neighbors

def getData(path):
    data = []
    datatruth = []
    for filename in glob.glob(path + "*.png"):
        data.append(wordDetection(filename))
    data = np.vstack(data)
    f = open(path + "tags.json")
    f = json.load(f)
    for i in f:
        datatruth.append(f[i]['signTags'])
    datatruth = np.hstack(datatruth)
    return data, datatruth

train, traintruth = getData("C:/Users/Alen/Documents/Machine Learning/BigData/Out/")
test, testtruth = getData("C:/Users/Alen/Documents/Machine Learning/Small Data/Out/")
print(train.shape)
print(traintruth.shape)
print(test.shape)
print(testtruth.shape)

classifier = neighbors.KNeighborsClassifier(10, weights='distance')
classifier.fit(train, traintruth)
print(classifier.score(test, testtruth))