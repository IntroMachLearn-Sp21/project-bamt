import cv2
from PyShapes import *
import numpy as np

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


