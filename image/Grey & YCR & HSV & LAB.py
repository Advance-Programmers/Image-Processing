import cv2
image = cv2.imread("C:/Users/Mohammad/Desktop/python project/image procses/image/me.jpg")
Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
YCR = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
LAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow("image", image)
cv2.imshow("gray", Gray)
cv2.imshow("YCR", YCR)
cv2.imshow("HCV", HSV)
cv2.imshow("LAB", LAB)
cv2.waitKey(0)
