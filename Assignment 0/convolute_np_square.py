import matplotlib.pyplot as plt
import numpy as np
import cv2


def plot_img(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray')
    plt.show()
    

def plot_two_images(img1: np.array, img2: np.array):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(img1, cmap='gray')
    plt.show()
    ax[1].imshow(img2, cmap='gray')
    plt.show()


# The following function computes the resulting size-reduced image
# obtained from convoluting a square kernel across a squared image.
# Stride is supposed to be equal to 1 and no padding is employed.


def calculate_target_size(img_size: int, kernel_size: int) -> int:
    num_pixels = 0 
    for i in range(img_size):
        added = i + kernel_size
        if added <= img_size:
            num_pixels += 1        
    return num_pixels
    
        
# The following function creates a 2D array of zeros (a black image);
# then iterates over rows and columns of the target image to apply convolution results


def convolve(img: np.array, kernel: np.array) -> np.array:
    
    tgt_size = calculate_target_size(
        img_size=img.shape[0],
        kernel_size=kernel.shape[0]
    )
    
    k = kernel.shape[0]
    
    convolved_img = np.zeros(shape=(tgt_size, tgt_size))
    
    for i in range(tgt_size):
        for j in range(tgt_size):
            # img[i, j] = individual pixel value
            # get the current matrix
            mat = img[i:i+k, j:j+k]
            
            # apply the convolution - element-wise multiplication and summation of the result
            convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
            
    return convolved_img


img = cv2.imread('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 0/sample.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

gaussian_blur = np.random.rand(21, 21)
sum_blur = np.sum(gaussian_blur)
gaussian_blur = gaussian_blur/sum_blur

img = cv2.resize(img, dsize=(1000, 1000), interpolation=cv2.INTER_CUBIC)

img = convolve(img, gaussian_blur)
plot_img(img)
