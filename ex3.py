import cv2 as cv
# import numpy as np
  
def convert_to_greyScale(image) :
  h, w, _ = image.shape
  for x in range(w):
    for y in range(h):
      pixel = image[x, y]
      red, green, blue = pixel
      gray_value = int((0.299 * red) + (0.587 * green) + (0.114 * blue))
      image[x, y] = [gray_value, gray_value, gray_value]
  return image
      
# read an image
img = cv.imread("kakada.png")

# convert image to gray image
gray_img = convert_to_greyScale(img)

# show image
cv.imshow('My photo...', gray_img)
cv.waitKey(0)

