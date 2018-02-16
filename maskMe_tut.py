import numpy as np
import cv2

print('Mask Me Man!')

# ------   Load the haarcascades   ------ #

## build our cv2 Cascade Classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

# ------   Prepare the image   ------ #

## Load our overlay image/ Uncomment any of them to try it out (or write in your own)
# imgMask = cv2.imread('corgic.png', -1)
imgMask = cv2.imread('mario_face.png', -1)
# imgMask = cv2.imread('samus_ht.png', -1)
# imgMask = cv2.imread('kirby.png', -1)
# imgMask = cv2.imread('deer_head.png', -1)




## Create the mask for the img
orig_mask = imgMask[:,:,3]

## Create the inverted mask for the img
orig_mask_inv = cv2.bitwise_not(orig_mask)

## Convert image to BGR and save the original image size (used later when re-sizing the image)
imgMask = imgMask[:,:,0:3]
origImgHeight, origImgWidth = imgMask.shape[:2]

# ------   Main Loop   ------ #

## set up camera
cam = cv2.VideoCapture(0)
print('Camera Accessed.')

while True:
    ## Capture video feed
    ret, frame = cam.read()

    ## Create greyscale image from the video feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ## Detect faces in input video stream
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

   ## Iterate over each face found
    for (x, y, w, h) in faces:
        ## Uncomment the next line for debug (draw box around all faces)
        # face = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        ## Detect a nose within the region bounded by each face (the ROI)
        nose = nose_cascade.detectMultiScale(roi_gray)

        for (nx,ny,nw,nh) in nose:
            ## Un-comment the next line for debug (draw box around the nose)
            # cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(255,0,0),2)

            ## The img should be three times the width of the nose
            imgWidth =  3 * nw
            imgHeight = imgWidth * origImgHeight

            ## Center the img on the bottom of the nose
            x1 = int(nx - (imgWidth*5))
            y1 = int(ny - (imgHeight*3))
            x2 = int(nx + nw + (imgWidth*5))
            y2 = int(ny + (imgHeight/2))

            ## Check for clipping
            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 > w:
                x2 = w
            if y2 > h:
                y2 = h

            ## Re-calculate the width and height of the image
            imgWidth = x2 - x1
            imgHeight = (y2 - y1)

            ## Re-size the original image and the masks to the img sizes
            ## calcualted above
            newImg = cv2.resize(imgMask, (imgWidth,imgHeight), interpolation = cv2.INTER_AREA)
            mask = cv2.resize(orig_mask, (imgWidth,imgHeight), interpolation = cv2.INTER_AREA)
            mask_inv = cv2.resize(orig_mask_inv, (imgWidth,imgHeight), interpolation = cv2.INTER_AREA)

            ## take ROI for img from background equal to size of image
            roi = roi_color[y1:y2, x1:x2]

            ## roi_bg contains the original image only where the mustache is not
            ## in the region that is the size of the mustache.
            roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

            ## roi_fg contains the image of the mustache only where the mustache is
            roi_fg = cv2.bitwise_and(newImg,newImg,mask = mask)

            ## join the roi_bg and roi_fg
            dst = cv2.add(roi_bg,roi_fg)

            ## place the joined image, saved to dst back over the original image
            roi_color[y1:y2, x1:x2] = dst

            break

    ## Display the resulting frame
    cv2.imshow('Video', frame)

    ## press any key to exit
    ## NOTE;  x86 systems may need to remove: " 0xFF == ord('q')"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ------   End of Main Loop   ------ #

## When everything is done, release the capture
cam.release()
cv2.destroyAllWindows()
