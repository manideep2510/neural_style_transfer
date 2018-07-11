import os
import numpy as np
import glob
from scipy.misc import imresize
from scipy.misc import imsave
import matplotlib.pyplot as plt
from PIL import Image



imgsx2 = plt.imread("images/manideep.jpg")
imgsx2_resize = imresize(imgsx2, (512, 512))

imx2 = Image.fromarray(imgsx2_resize)
imx2.save("images/manideep11.jpg")


