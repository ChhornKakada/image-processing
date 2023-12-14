import cv2 as cv
# import numpy as np
  
def show_red_on_leftTop(image) :
  h, w, _ = image.shape
  for x in range(int(w/2)):
    for y in range(int(h/2)):
      image[x, y] = [0, 0, 255]
      # image[x, y] = [blue, green, red]
  return image
      
# read an image
img = cv.imread("kakada.png")

# convert image to gray image
gray_img = show_red_on_leftTop(img)

# show image
cv.imshow('Test Image', gray_img)
cv.waitKey(0)

