import cv2 as cv
import cv2 as cv
img = cv.imread("sreynith.jpg")
#img1 = cv.imread("TP4-Demo-Edge-Sobel.png", cv.IMREAD_GRAYSCALE)
#img1 = cv.imread("D:/Phut/ITC/Courses/AI/UP/AI-Cover.jpg")
#img1 = cv.imread("D:\\Phut\\ITC\\Courses\\AI\\UP\\AI-Cover.jpg")
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Test Image', img)
# cv.imshow('Image 1', img1)
cv.waitKey(0)

