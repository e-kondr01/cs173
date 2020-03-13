from numpy import dstack, roll
from skimage.io import imread, imsave
from skimage.util import img_as_float, img_as_ubyte


def reduce(img, p: float = 0.05):
    '''Cutting off edges '''
    rows = img.shape[0]
    cols = img.shape[1]
    img = img[round(rows * p): round(rows * (1-p)),
              round(cols * p): round(cols * (1-p))]
    return img


def find_optimal_shift(img1, img2, px_shift: int = 15):
    '''Находим оптимальный сдвиг
    params: img1 - фиксированное изображение
    img2 - изображение, которое двигаем
    px_shift - модуль максимального отклонения сдвига'''
    max_correlation = 0
    for x in range(-px_shift, px_shift + 1):
        for y in range(-px_shift, px_shift + 1):
            shifted_x_img2 = roll(img2, x, axis=0)
            shifted_img2 = roll(shifted_x_img2, y, axis=1)
            correlation = (img1 * shifted_img2).sum()
            if correlation > max_correlation:
                max_correlation = correlation
                optimal_shift_x = x
                optimal_shift_y = y
                that_image = shifted_img2
    print(optimal_shift_x, optimal_shift_y)
    return (optimal_shift_x, optimal_shift_y, that_image)


def align(img, g_coord):
    row_g, col_g = g_coord

    '''getting separate r, g, b channels '''
    rows = img.shape[0]
    cols = img.shape[1]
    end_correct = img.shape[0] % 3  # for same height
    img = img_as_float(img)
    uncut_b = img[0: rows // 3, :]
    uncut_g = img[rows // 3: rows // 3 * 2, :]
    uncut_r = img[rows // 3 * 2: img.shape[0] - end_correct, :]
    r = reduce(uncut_r)
    g = reduce(uncut_g)
    b = reduce(uncut_b)

    '''moving channels '''
    blue_on_green = find_optimal_shift(img1=g, img2=b)
    red_on_green = find_optimal_shift(img1=g, img2=r)

    '''finding coordinates '''
    row_b = row_g + blue_on_green[0] - rows // 3
    col_b = col_g + blue_on_green[1]
    row_r = row_g + red_on_green[0] + rows // 3
    col_r = col_g + red_on_green[1]

    '''testing visuals '''
    shifted_b = blue_on_green[2]
    shifted_r = red_on_green[2]
    test_image = dstack((shifted_r, g, shifted_b))
    test_image = img_as_ubyte(test_image)
    imsave('test_image.png', test_image)

    return (row_b, col_b), (row_r, col_r)


if __name__ == '__main__':
    img = imread("C:\cs173\module1\\00.png")
    print(align(img, (508, 237)))
