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

### Understanding the Masking Process (from the code)

```
# ------   Load the haarcascades   ------ #

## build our cv2 Cascade Classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
```

Here we will build the Haar cascade classifier for the face and nose. 

```
# ------   Prepare the image   ------ #

## Load our overlay image/ Uncomment any of them to try it out (or write in your own)
imgMask = cv2.imread('mario_face.png', -1)

```

We load the image with -1 (negative one) as the second parameter to load all the layers in the image. 
  - The image is made up of 4 layers (or channels): Blue, Green, Red, and an Alpha transparency layer (knows as BGR-A). The alpha channel is made up of a combination of the other 3 layers.
```

## Create the mask for the img
orig_mask = imgMask[:,:,3]
```

Now we take the alpha layer and create a new single-layer image that we will use for masking.
```

## Create the inverted mask for the img
orig_mask_inv = cv2.bitwise_not(orig_mask)
```

Take the inverse of our mask. The initial mask will define the area for the image, and the inverse mask will be for the region around the image.
```

## Convert image to BGR and save the original image size (used later when re-sizing the image)
imgMask = imgMask[:,:,0:3]
origImgHeight, origImgWidth = imgMask.shape[:2]
```

Here we convert the image to a 3-channel BGR image (BGR rather than BGR-A is required when we overlay the image over the webcam image later). Then Save the original image sizes, which we will use later when re-sizing the mustache image.  
  
If you have more questions, please see References
### Running the code (web cam required)

From your terminal, move to the directory that your code and files are stored in. 


Once in your directory

## Continuing the Journey with Tensorflow

Security Example (Using a faster model, but compromises accuracy for speed): 

<img src="https://github.com/itoth43/OpenCV-and-Tensorflow-Facial-Detection-/blob/master/security_Example.jpg" alt="Security Human Recognition and Detection" width="300"/>

Human Counting Example (Using a slower model, but compromises speed for accuracy):

<img src="https://github.com/itoth43/OpenCV-and-Tensorflow-Facial-Detection-/blob/master/headCount_Example.jpg" alt="Human Counting. Recognition and Detection" width="300"/>

If you want to continue your journey in object detection and learn about object recognition, 

here is a great site for tutorials using tensorflow and object detection: (https://pythonprogramming.net) that help me when I first started with Tensorflow

## Authors

* **Isaiah Toth**

A Clemson University Graduate 2018 and Software Consultant/Engineer.

## References and Resources for further learning

https://sublimerobots.com/2015/02/dancing-mustaches/

https://pythonprogramming.net
