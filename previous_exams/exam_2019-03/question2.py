from imageio import imread
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

# Image from pexels.com, free to use!
FILENAME = "animal.jpg"

# A
img0 = imread(FILENAME)
img0 = np.mean(img0, axis=-1)

# D
for sigma in [0, 8, 16, 32]:
    # D
    img = ndimage.gaussian_filter(img0, sigma=sigma)
    plt.subplot(2,2,1)
    plt.imshow(img, cmap=plt.cm.gray)

    # B
    sx = ndimage.sobel(img, axis=0)
    plt.subplot(2,2,2)
    plt.imshow(sx, cmap=plt.cm.gray)
    sy = ndimage.sobel(img, axis=1)
    plt.subplot(2,2,3)
    plt.imshow(sy, cmap=plt.cm.gray)

    # C
    sob = np.hypot(sx, sy)
    plt.subplot(2,2,4)
    plt.imshow(sob.astype(np.float), cmap=plt.cm.gray)
    plt.show()
