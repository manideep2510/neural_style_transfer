import os
import numpy as np
import glob
from scipy.misc import imresize
from scipy.misc import imsave
import matplotlib.pyplot as plt
from PIL import Image

imgsx1 = plt.imread("images/stary_night.jpg")
imgsx1_resize = imresize(imgsx1, (512, 512))

imx1 = Image.fromarray(imgsx1_resize)
imx1.save("images/stary_night1.jpg")

imgsx2 = plt.imread("images/Red_vineyards.jpg")
imgsx2_resize = imresize(imgsx2, (512, 512))

imx2 = Image.fromarray(imgsx2_resize)
imx2.save("images/Red_vineyards1.jpg")

imgsx2 = plt.imread("images/irises.jpg")
imgsx2_resize = imresize(imgsx2, (512, 512))

imx2 = Image.fromarray(imgsx2_resize)
imx2.save("images/irises1.jpg")

