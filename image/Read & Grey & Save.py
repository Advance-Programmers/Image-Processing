import cv2
image = cv2.imread("C:/Users/Mohammad/Desktop/python project/image procses/image/me.jpg")
Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)
cv2.imshow("gray", Gray)
cv2.imwrite("C:/Users/Mohammad/Desktop/python project/image procses/image/me gray.jpg", Gray)
cv2.waitkey(0)
