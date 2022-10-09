# importing librarys
import cv2
import numpy as np
from matplotlib import pyplot as plt

# importing image
img = cv2.imread("lena.jpg") # images name

# making readable for OpenCV
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# smoothing and blurring
kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

# preparing titles and images
titles = ["Image", "2D Convolution", "Blur", "GaussianBlur", "Median", "BilateralFilter"]
images = [img, dst, blur, gblur, median, bilateralFilter]

# showing images
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
