""" Solar surface 

Histogram and fourier space analysis

The lack of sharp features in fourier space shows the multiscale
properties of the convective islands on the sun ?

"""

import numpy as np
from imageio import imread
import matplotlib.pyplot as plt

image_rgb = imread('solar_surface.jpg')

image = np.sum(image_rgb, axis=-1)
image = image / float(image.max())

window = np.hanning(image.shape[-1])
window = window[:, None] * window[None, :]

shape = 2 * np.array(image.shape)
image_ft = np.abs(np.fft.fft2((image - image.mean()) * window, s=shape))
#image_ft = np.abs(np.fft.fft2((image - image.mean()), s=shape))
image_ft = np.fft.fftshift(image_ft)

N = int(0.5 * image_ft.shape[-1] - 100)
image_ft = image_ft[N:-N, N:-N]

# -- Plot

plt.figure(figsize=(10, 8))
subp = [2, 2, 1]

f = plt.subplot(*subp); subp[-1] += 1
plt.title('Solar surface')
plt.imshow(image_rgb)

plt.subplot(*subp, sharex=f, sharey=f); subp[-1] += 1
plt.title('Solar surface intensity')
plt.imshow(image, cmap='Greys_r')

plt.subplot(*subp); subp[-1] += 1
plt.title('Rescaled Intensity Histogram')
plt.hist(image.flatten(), bins=80, density=True)

plt.subplot(*subp); subp[-1] += 1
plt.title('Intensity frequency distribution')
plt.imshow(image_ft, cmap='Greys_r')

plt.show()
