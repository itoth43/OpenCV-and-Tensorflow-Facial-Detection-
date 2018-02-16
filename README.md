# Facial Detection "SnapChat Mimic"

For those interested in getting started with Python, OpenCV, Googles Tensorflow, Machine Learning, and Object Detection.

This is a simple Python program using OpenCV (https://opencv.org) made to mimic the snapchats
filter idea using facial detection. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

(Warning, the Terminal will be used. The terminal is not something to be afraid of and all great developers will strive to master it)

### Installing and Important Files

#### Python

Download and Install Python (be sure to check the options for Pip3 install and PATH appending):
https://www.python.org/downloads/

(I am using Python 3.6.3):
https://www.python.org/downloads/release/python-363/

#### OpenCV

Download and Install openCV:

##### Windows:

https://github.com/opencv/opencv/releases
(opencv-3.3.1-vc14.exe)

##### Mac:

brew install opencv3 --with-contrib

(Homebrew Install if not installed already):

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### Haar Cascades

Haar Cascades:
A Haar Cascade works by training the cascade on thousands of negative images with the positive image superimposed on it. The haar cascade is capable of detecting features from the source.


Front Face:

https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Nose:

https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/haarcascade_mcs_nose.xml

More Libraries of Haar Cascades:

https://github.com/opencv/opencv/tree/master/data/haarcascades
https://github.com/opencv/opencv_contrib/tree/master/modules/face/data/cascadesa

## Code and Files

The necessary files for this example are available in this repo, including:

- Haar Cascades
- Mask Images
- Python Code

### Understanding the Code

```
# ------   Load the haarcascades   ------ #

## build our cv2 Cascade Classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
```

This is the section where the object of 

### Running the code (web cam required)

From your terminal, move to the directory that your code and files are stored in. 


Once in your directory

## Continuing the Journey with Tensorflow

If you want to continue your journey in object detection and maybe learn about object recognition, here is how you can start using tensorflow (https://www.tensorflow.org/install/) 

## Authors

* **Isaiah Toth**

A Software Consultant/Engineer and Clemson University Graduate 2018.
