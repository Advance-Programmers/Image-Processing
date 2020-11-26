import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/Mohammad/Desktop/python project/image procses/image/me.jpg",0)
cv2.imshow("Sample Gray",img)
plt.hist(img.ravel(),256,[0,256])
plt.show()
