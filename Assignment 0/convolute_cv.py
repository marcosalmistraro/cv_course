import matplotlib.pyplot as plt
import numpy as np
import cv2

array = np.zeros((100, 100))
array1 = np.full((100, 100), 100)
array2 = np.full((100, 100), 200)
print(array)
print(array1)
print(array2)

concatenated = np.concatenate((array, array1, array2), axis = 1)
print(concatenated)
plt.imshow(concatenated)
plt.show()

image_with_noise = concatenated + 50 * (np.random.rand(100, 300) - 0.5)
plt.imshow(image_with_noise)
plt.show()

my_img = cv2.imread('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 0/sample.jpg')
cv2.imshow("image", my_img)
# instruct openCV to let image visible until key is pressed
cv2.waitKey()

# create Gaussian kernel to convolute over the image
# kernel needs to have odd dimensions
blurred = cv2.GaussianBlur(my_img, (51,51), sigmaX=0)
cv2.imshow('blurred', blurred)
cv2.waitKey()

# create Gaussian kernel by using matrix operations in np
g_kernel = np.random.rand(51, 51)
sum = np.sum(g_kernel)
normalized_kernel = g_kernel/sum
blurred2 = cv2.filter2D(my_img, -1, normalized_kernel)
cv2.imshow('blurred2', blurred2)
cv2.waitKey()