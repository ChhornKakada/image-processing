import cv2 as cv
# import numpy as np
  
def inverse_img(image) :
  h, w, _ = image.shape
  for y in range(h):
    for x in range(w):
      # print(image[y, x, 0])
      blue = image[y, x, 0]
      green = image[y, x, 1]
      red = image[y, x, 2]
      image[y, x] = [255-blue, 255-green, 255-red]
      # image[x, y] = [blue, green, red]
  return image
      
# read an image
img = cv.imread("kakada.png")

# convert image to gray image
gray_img = inverse_img(img)

# show image
cv.imshow('Test Image', gray_img)
cv.waitKey(0)

