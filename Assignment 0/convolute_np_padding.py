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

# The following function computes the resulting reduced image
# obtained from convoluting a square kernel across a rectangular image
# Stride is supposed to be equal across dimensions. No padding

def calculate_target_size(img: np.array, kernel_size: int, stride: int) -> tuple:
    img_heigth, img_length = img.shape[0], img.shape[1],
    output_height = int((img_heigth - kernel_size)/stride + 1)
    output_length = int((img_length - kernel_size)/stride + 1)
    return (output_height, output_length)
        

# The following function creates a 2D array of zeros
# then iterates over rows and columns of the target image.
# The following method is highly impractical and takes
# O(img_height * img_length * kernel_height * kernel_length)

def convolve(img: np.array, kernel: np.array, stride: int) -> np.array:
    k = kernel.shape[0]
    output_height, output_length = calculate_target_size(img, k, stride)

    convolved_img = np.zeros(shape=(output_height, output_length))
    
    for i in range(output_height):
        for j in range(output_length):
            # img[i, j] = individual pixel value
            # Get the current matrix
            mat = img[i:i+k, j:j+k]
            
            # Apply the convolution - element-wise multiplication and summation of the result
            convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
            
    return convolved_img


# Function to calculate needed padding size

def get_padding_width_per_side(kernel_size: int) -> int:
    return kernel_size // 2


def add_padding_to_image(img: np.array, padding_width: int) -> np.array:
    # Array of zeros of shape (img + padding_width)
    img_with_padding = np.zeros(shape=(
        img.shape[0] + padding_width * 2,  # Multiply with two because padding needed on all sides
        img.shape[1] + padding_width * 2
    ))

    # Keep the pixel wide padding on all sides but change the inner values to be the same as input
    img_with_padding[padding_width:-padding_width, padding_width:-padding_width] = img
    return img_with_padding

img = cv2.imread('/Users/marco/Documents/KU Leuven/Computer Vision/Assignment 0/sample.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

gaussian_blur = np.random.rand(11, 11)
sum_blur = np.sum(gaussian_blur)
gaussian_blur = gaussian_blur/sum_blur

img = convolve(img, gaussian_blur, 1)
pad = get_padding_width_per_side(11)
img = add_padding_to_image(img, pad)
plot_img(img)
