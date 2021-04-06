import cv2
from PyShapes import *
import numpy as np
import scipy
from scipy import ndimage
import imutils


def ShapeFeatureTest(path):
    features = []
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    v = np.median(gray)
    sigma = 0.33
    #---- apply optimal Canny edge detection using the computed median----
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(gray, lower_thresh, upper_thresh)
    cv2.imshow('edged',edged)
    cv2.waitKey(0)
    blur = cv2.GaussianBlur(img, (15, 15), 1)
    #gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(blur, 100, 150)
    dilate = cv2.dilate(canny, np.ones((5, 5)), iterations=1)
    contours= cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    

    for cnt in contours:
        if (cv2.contourArea(cnt) > 10000):
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            print(len(approx))
            if len(approx)==5:
                print("pentagon")
                cv2.drawContours(img,[cnt],0,255,-1)
            elif len(approx)==3:
                print("triangle")
                cv2.drawContours(img,[cnt],0,(0,255,0),-1)
            elif len(approx)==4:
                print("square")
                cv2.drawContours(img,[cnt],0,(0,0,255),-1)
            elif len(approx) == 8:
                print("Octagon")
                cv2.drawContours(img,[cnt],0,(255,255,0),-1)
            else:
                print("circle")
                cv2.drawContours(img,[cnt],0,(0,255,255),-1)
    cv2.imshow('img',dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def ShapeFeature(path):
    features = []
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    v = np.median(gray)
    sigma = 0.33
    #---- apply optimal Canny edge detection using the computed median----
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(gray, lower_thresh, upper_thresh)
    cv2.imwrite("out.png", edges)
    shapes = PyShape("out.png")


    result = shapes.get_all_shapes()
    total = 0
    for shape in result:
        total += result[shape]
    for shape in result:
        if(total == 0):
            features.append(0)
        else:
            features.append(result[shape]/total)

    return np.hstack(features)


