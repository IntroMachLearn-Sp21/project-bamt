# project-bamt
## Required Libraries
1. os
2. numpy
3. easyocr
4. cv2
5. PyShapes
6. json
7. collections
8. skimage
9. argparse
10. pandas
11. dominant_color_detection
12. matplotlib

## Training Classifier
The python file train.py contains a function called Train that takes
a relative filepath to the directory with the images and json file. The
easiest was to do this is to have the folder with the images in the 
same directory as the train.py file. Within the train.py file the Train
function is called at the end of the file, change the argument to the path
to the images.

1. Move Folder with Training Images and JSON inside to the same Directory as train.py
2. Change the argument of the Train call within train.py to your folder path

## Testing Classifier
The test.py file works in a similar way to the training file. It has a
function called Test that accepts a path to the test image directory. 
Similar to test have the folder in the same directory and at the end
of the test.py file change the argument to the filepath of the images.

1. Move Folder with Test Images to the same Directory as test.py 
2. Change the argument of the Test call within test.py to your folder path
