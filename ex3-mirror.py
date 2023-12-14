import cv2 as cv
# import numpy as np
  
# reverse image from bottom or rotate to bottom
def reverse_y_axis(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  j = 0
  for y in reversed(range(h)) : 
    i = 0 
    for x in reversed(range(w)) :
      copy_img[j, i] = image[y, x]
      i += 1
    j += 1
  return copy_img

# reverse image from from left to right
def reverse_x_axis(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  
  j = 0
  for y in (range(h)) : 
    i = 0 
    for x in reversed(range(w)) :
      copy_img[j, i] = image[y, x]
      i += 1
    j += 1
  return copy_img


# rotate image to left 
def rotate_left(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  j = 0
  for x in reversed(range(w)) : 
    i = 0 
    for y in reversed(range(h)) :
      copy_img[j, i] = image[y, x]
      i += 1
    j += 1
  return copy_img


# rotate image to right 
def rotate_right(image) :
  h, w, _ = image.shape
  copy_img = image.copy()
  i = 0
  for x in reversed(range(w)) : 
    j = 0 
    for y in (range(h)) :
      copy_img[i, j] = image[y, x]
      j += 1
    i += 1
  return copy_img
      
# read an image
img = cv.imread("kakada.png")

# convert image to gray image
mirror_img = rotate_right(img)

# show image
cv.imshow('Test Image', mirror_img)
# cv.imshow('Test Image', img)
cv.waitKey(0)

