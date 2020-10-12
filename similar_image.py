import cv2
import glob

min1 = None

paths = glob.glob("dataBase/*.jpg")
image = cv2.imread('querry.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

for path in paths:
    img = cv2.imread(path)
    gray_image1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    c1 = 0
    i = 0
    while i < len(histogram) and i < len(histogram1):
        c1 += (histogram[i] - histogram1[i])**2
        i += 1
    c1 = c1**(1 / 2)
    if min1 == None:
        min1 = c1
        res = path
    else:
        if min1 > c1:
            min1 = c1
            res = path

print("Image similar to querry image is '{}'".format(res.split('/')[1]))
