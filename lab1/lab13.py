from math import log
from skimage.color import rgb2gray
from skimage.io import imread
from skimage.util import img_as_ubyte, img_as_uint, img_as_float


def count_entropy(img):
    '''Считаем кол-во возможных вероятностей '''
    p = set()
    try:
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                p.add(img[x, y][0])
                p.add(img[x, y][1])
                p.add(img[x, y][2])
    except IndexError:
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                p.add(img[x, y])
    '''Пусть вероятности равновозможны '''
    V = img.shape[0] * img.shape[1]
    H = - (V * (1 / len(p)) * log((1 / len(p)), 2))
    return H


def count_standard_deviation(img1, img2):
    '''params:
    img1 - original image
    img2 - image after decoding '''

    deviation_sum = 0
    try:
        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):
                deviation_sum += (img1[x, y][0] + img1[x, y][1] +
                                  img1[x, y][2] - img2[x, y][0] -
                                  img2[x, y][1] - img2[x, y][2]) ** 2
    except IndexError:
        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):
                deviation_sum += (img1[x, y] - img2[x, y]) ** 2
    standard_deviation = deviation_sum / (img1.shape[0] * img1.shape[1])
    return standard_deviation


if __name__ == '__main__':
    img1 = imread('C:\cs173\lab1\eye.jpg')
    img1 = rgb2gray(img1)
    img1 = img_as_ubyte(img1)
    img2 = imread('C:\cs173\lab1\\restored_img_16_levels.png')
    print('Уменьшение уровней яркости:')
    print(count_entropy(img1), count_entropy(img2))
    print(count_standard_deviation(img1, img2))

    img3 = imread('C:\cs173\\test_image.png')
    img3 = img_as_float(img3)
    img4 = imread('C:\cs173\\rbg_to_yuv.png')
    img4 = img_as_float(img4)
    print('Из RGB в YUV: ')
    print(count_entropy(img3), count_entropy(img4))
    print(count_standard_deviation(img3, img4))
