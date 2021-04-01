import glob
import json
import os
from ShapeFeature import ShapeFeature, ShapeFeatureTest
from worddetection import wordDetection
from ColorDetection2 import ColorFeauture
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

def writeJSON(path, prediction):
    diction = {}
    count = 0
    print(prediction)
    for filename in glob.glob(path + "*.png"):
        name = os.path.split(filename)[-1]
        diction[name[:-4]] = {"signTags": [prediction[count]]}
        count += 1
    with open('person.json', 'w') as json_file:
        json.dump(diction, json_file)

def getData(path):
    data = []
    datatruth = []
    f = open(path + "tags.json")
    f = json.load(f)
    for filename in glob.glob(path + "*.png"):
        data.append(np.concatenate((ColorFeauture(filename), ShapeFeature(filename), wordDetection(filename))))
        #data.append(ShapeFeature(filename))
        name = os.path.split(filename)[-1]
        datatruth.append(f[name[:-4]]['signTags'])
        print(f[name[:-4]]['signTags'])

    data = np.vstack(data)
    datatruth = np.hstack(datatruth)
    return data, datatruth

alltrain = []
alltraintruth = []

train, traintruth = getData("BigData1/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)

train, traintruth = getData("BigData2/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)

train, traintruth = getData("BigData3/Out/")
alltrain.append(train)
alltraintruth.append(traintruth)

scores = []
confus = []

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
        confus.append(confusion_matrix(testtruth, forest.predict(test)))
    for j in range(0, 3):
        classifier = neighbors.KNeighborsClassifier(10, weights='distance')
        classifier.fit(train, traintruth)
        scores.append(classifier.score(test, testtruth))
        confus.append(confusion_matrix(testtruth, classifier.predict(test)))
print(scores)
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
    confus.append(confusion_matrix(testtruth, forest.predict(test)))
    classifier = neighbors.KNeighborsClassifier(10, weights='distance')
    classifier.fit(train, traintruth)
    scores.append(classifier.score(test, testtruth))
    confus.append(confusion_matrix(testtruth, classifier.predict(test)))
    
print(scores)
with open('Round2', 'w') as f:
    for item in scores:
        f.write("%s\n" % item)
with open('confusion.txt', 'w') as f:
    for item in confus:
        f.write("%s\n" % item)