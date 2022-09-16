import cv2, os
import numpy as np
import glob

label = "Uninfected"
uninfected_list = glob.glob("cell_images/"+label+"/*.png")
file = open("dataset.csv", "a")

for path in uninfected_list:
    src = cv2.imread(path)

    # Gaussian blur of the image with 5X5 kernel and std of 2
    image = cv2.GaussianBlur(src, (5,5), 2)

    # converting color space of the image to gray
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
    # setting pixel values in relation to threshold value(here 127)
    ret,thresh = cv2.threshold(img_gray, 127, 255, 0)

    # extracting contours in cv2.RETR_TREE(1) mode and cv2.CHAIN_APPROX_SIMPLE(2) method
    contours,_ = cv2.findContours(thresh, 1, 2)

    file.write(label)
    file.write(",")

    # for every contour
    for i in range(5):
        try:
            area = cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")

        file.write(",")

    file.write("\n")

label = "Parasitized"
infected_list = glob.glob("cell_images/"+label+"/*.png")
file = open("dataset.csv", "a")

for img_path in infected_list:

    img = cv2.imread(img_path)
    blur_img = cv2.GaussianBlur(img, (5, 5), 2)
    gray_img = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)

    file.write(label)
    file.write(",")

    for i in range(5):
        try:
            area = cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")
        file.write(",")
    file.write("\n")

file.close()
