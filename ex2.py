import cv2 as cv
# import numpy as np
  
def topRight_noRedGreen(image) :
  h, w, _ = image.shape
  
  # no red and green
  for x in range(int(w/2), w) :
    for y in range(int(h/2)) : 
      pixel = image[y, x]
      red, green, blue = pixel
      image[y, x] = [blue, 0, 0]
      # image[x, y] = [blue, green, red]
      
  # no red and blue
  for x in range(int(w/2), w) :
    for y in range(int(h/2), h) : 
      pixel = image[y, x]
      red, green, blue = pixel
      image[y, x] = [0, 0, red]
      
  # no red and blue
  for x in range(int(w/2)) :
    for y in range(int(h/2), h) : 
      pixel = image[y, x]
      red, green, blue = pixel
      image[y, x] = [0, green, 0]
      
  return image

      
# read an image
img = cv.imread("kakada.png")

# convert image to gray image
gray_img = topRight_noRedGreen(img)

# show image
cv.imshow('Result of exercise 3', gray_img)
cv.waitKey(0)

