from numpy import dstack, histogram
from skimage.io import imread, imsave


img = imread('./module2/landscape.png')
values, bin_edges = histogram(img, bins=range(257))
values_list = list(values)
x = img.shape[0]
y = img.shape[1]
size = x * y

for value in values_list:
    if value:
        cdf_min = value
        break

for i in range(x):
    for j in range(y):
        img[i][j] = round((sum(values_list[:img[i][j]+1]) - cdf_min) * 255 / (size - 1))

imsave('out_img.png', img)
