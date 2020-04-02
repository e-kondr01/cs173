from numpy import histogram
from skimage.io import imread, imshow, imsave
from skimage.util import img_as_float, img_as_ubyte
from numpy import dstack


img = imread('.\\module2\landscape.png')
values, bin_edges = histogram(img, bins=range(257))
values_list = list(values)
x = img.shape[0]
y = img.shape[1]
size = x * y


def cdf(values_list, bright_num: int):
    """
    функция распределения
    bright_num:  кол-во уровей яркости"""
    return sum(values_list[:bright_num])


for value in values_list:
    if value:
        cdf_min = value

for i in range(x):
    for j in range(y):
        img[i][j] = round((cdf(values_list, img[i][j]) - cdf_min) * 255 / (size - 1))

imsave('cdf.png', img)
