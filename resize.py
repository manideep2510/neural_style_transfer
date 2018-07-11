import os
import numpy as np
import glob
from scipy.misc import imresize
from scipy.misc import imsave
import matplotlib.pyplot as plt
from PIL import Image

imgsx1 = plt.imread("images/style_night.jpg")
imgsx1_resize = imresize(imgsx1, (512, 512))

imx1 = Image.fromarray(imgsx1_resize)
imx1.save("images/style_night1.jpg")

imgsx2 = plt.imread("images/manideep.jpg")
imgsx2_resize = imresize(imgsx2, (512, 512))

imx2 = Image.fromarray(imgsx2_resize)
imx2.save("images/manideep1.jpg")

imgsx2 = plt.imread("images/style1.jpg")
imgsx2_resize = imresize(imgsx2, (512, 512))

imx2 = Image.fromarray(imgsx2_resize)
imx2.save("images/style_11.jpg")
