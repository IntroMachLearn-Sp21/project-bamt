import glob
import json
from ShapeFeature import ShapeFeature
from worddetection import wordDetection
from ColorDetection2 import ColorFeauture
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

def getData(path):
    data = []
    datatruth = []
    for filename in glob.glob(path + "*.png"):
        data.append([ColorFeauture(filename), ShapeFeature(filename), wordDetection(filename)])
    data = np.vstack(data)
    f = open(path + "tags.json")
    f = json.load(f)
    for i in f:
        datatruth.append(f[i]['signTags'])
    datatruth = np.hstack(datatruth)
    return data, datatruth

alltrain = []
alltraintruth = []

train, traintruth = getData("C:/Users/Alen/Documents/Machine Learning/Small Data/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)

train, traintruth = getData("C:/Users/Alen/Documents/Machine Learning/Small Data/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)

train, traintruth = getData("C:/Users/Alen/Documents/Machine Learning/Small Data/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)

"""train, traintruth = getData("C:/Users/Alen/Documents/Machine Learning/Small Data/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)"""

scores = []

for i in range(0,3):
    train = []
    traintruth = []
    test = []
    testtruth = []
    tot = []
    for j in range(0,3):
        if(i == j):
            test = alltrain[i]
            testtruth = alltraintruth[i]
        else:
            train.append(alltrain[j])
            traintruth.append(alltraintruth[j])
    train = np.vstack(train)
    traintruth = np.hstack(traintruth)
    print(train.shape)
    for j in range(0, 3):
        forest = RandomForestClassifier(criterion='entropy', n_estimators=100, n_jobs=-1,  max_depth = 20)
        forest.fit(train, traintruth)
        scores.append(forest.score(test, testtruth))
    for j in range(0, 3):
        classifier = neighbors.KNeighborsClassifier(10, weights='distance')
        classifier.fit(train, traintruth)
        scores.append(classifier.score(test, testtruth))

with open('Round1', 'w') as f:
    for item in scores:
        f.write("%s\n" % item)


scores = []
alltrain = np.vstack(alltrain)
alltraintruth = np.hstack(alltraintruth)
train, test, traintruth, testtruth = train_test_split(alltrain, alltraintruth, test_size=.3)
for i in range(0,3):
    forest = RandomForestClassifier(criterion='entropy', n_estimators=100, n_jobs=-1, max_depth = 20)
    forest.fit(train, traintruth)
    scores.append(forest.score(test, testtruth))
    classifier = neighbors.KNeighborsClassifier(10, weights='distance')
    classifier.fit(train, traintruth)
    scores.append(classifier.score(test, testtruth))

with open('Round2', 'w') as f:
    for item in scores:
        f.write("%s\n" % item)
