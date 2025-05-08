import cv2
import numpy as np

img = cv2.imread("hoadao.jpg")

#define 4 corner point, use any photo edittor
pts1 = np.float32([[795, 35], [1600, 0], [815, 202], [1600, 207]])

#define location of the points
width, height = 450, 250
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2);

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)

