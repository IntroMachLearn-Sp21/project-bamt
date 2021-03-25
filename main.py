import glob
import json
from ShapeFeature import ShapeFeature
from worddetection import wordDetection
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import neighbors
from sklearn.metrics import confusion_matrix

def getData(path):
    data = []
    datatruth = []
    for filename in glob.glob(path + "*.png"):
        data.append(np.hstack([ShapeFeature(filename), wordDetection(filename)]))
    data = np.vstack(data)
    f = open(path + "tags.json")
    f = json.load(f)
    for i in f:
        datatruth.append(f[i]['signTags'])
    datatruth = np.hstack(datatruth)
    return data, datatruth

train1, traintruth1 = getData("BigData1/Out/")
train2, traintruth2 = getData("BigData2/Out/")
train3, traintruth3 = getData("BigData3/Out/")
test, testtruth = getData("SmallData/Out/")
print("Train 1: ", train1.shape)
print("Train truth 1: ", traintruth1.shape)
print("Train 2: ", train2.shape)
print("Train truth 2: ", traintruth2.shape)
print("Train 3: ", train3.shape)
print("Train truth 3: ", traintruth3.shape)
print("Test: ", test.shape)
print("Test truth: ", testtruth.shape)

train = np.concatenate((train1, train2, train3), axis=0)
traintruth = np.concatenate((traintruth1, traintruth2, traintruth3), axis=0)
print("Train: ", train.shape)
print("Train truth: ", traintruth.shape)

""" # KNN
classifier = neighbors.KNeighborsClassifier(10, weights='distance')
classifier.fit(train, traintruth)
guess = classifier.predict(test)
mat = confusion_matrix(testtruth, geuss)
print(classifier.score(test, testtruth))
print(mat)
"""
# RF
forest = RandomForestClassifier(criterion='entropy', n_estimators=100, n_jobs=-1, max_features = 10, max_depth = 20)
forest.fit(train, traintruth)
guess = forest.predict(test)
mat = confusion_matrix(testtruth, guess)
print(forest.score(test, testtruth))
print(mat)