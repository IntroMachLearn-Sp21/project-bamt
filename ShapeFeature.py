import cv2
from PyShapes import *
import numpy as np
import scipy
from scipy import ndimage
import imutils


def ShapeFeatureTest(path):
    img = cv2.imread(path)
    #img = cv2.medianBlur(img,5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (3, 3), 0)
    x = cv2.Sobel(gray, cv2.CV_64F, 1,0, ksize=5, scale=1)
    y = cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=5, scale=1)
    absx= cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
    thresh = cv2.adaptiveThreshold(edge,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    contours,h = cv2.findContours(thresh,1,2)
    

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
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def ShapeFeature(path):
    features = []
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 50, 150)
    cv2.imwrite("out.png", edges)
    shapes = PyShape("out.png")


    result = shapes.get_all_shapes()
    total = 0
    for shape in result:
        total += result[shape]
    for shape in result:
        features.append(result[shape]/total)

    return np.hstack(features)


