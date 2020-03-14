from numpy import clip, dstack
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte, img_as_float


def rgb_to_yuv(img):
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    y_channel = 0.299 * r + 0.587 * g + 0.114 * b

    '''Decimation for U and V '''
    u = []
    for x in range(img.shape[0]):
        if x % 2 != 0:
            u.append([])
        for y in range(img.shape[1]):
            if x % 2 != 0 and y % 2 != 0:
                average = img[x-1: x, y-1: y] / 4
                average_r = average[:, :, 0]
                average_g = average[:, :, 1]
                average_b = average[:, :, 2]
                u[x // 2].append(clip((-0.147 * average_r - 0.289 * average_g +
                                 0.436 * average_b), 0, 1))

    v = []
    for x in range(img.shape[0]):
        if x % 2 != 0:
            v.append([])
        for y in range(img.shape[1]):
            if x % 2 != 0 and y % 2 != 0:
                average = img[x-1: x, y-1: y] / 4
                average_r = average[:, :, 0]
                average_g = average[:, :, 1]
                average_b = average[:, :, 2]
                v[x // 2].append(clip((0.615 * average_r - 0.515 * average_g -
                                 0.100 * average_b), 0, 1))

    return (y_channel, u, v)


def yuv_to_rgb(yuv_img: tuple):
    y_channel = yuv_img[0]
    u = yuv_img[1]
    v = yuv_img[2]
    r = y_channel.copy()
    g = y_channel.copy()
    b = y_channel.copy()
    for x in range(y_channel.shape[0]):
        for y in range(y_channel.shape[1]):
            x_for_uv = x - 1 if x > len(u) // 2 else x
            y_for_uv = y - 1 if y > len(u[0]) // 2 else y
            u_channel = u[x_for_uv // 2][y_for_uv // 2]
            v_channel = v[x_for_uv // 2][y_for_uv // 2]
            r[x, y] = clip((y_channel[x, y] + 1.14 * v_channel), 0, 1)
            g[x, y] = clip((y_channel[x, y] - 0.395 * u_channel -
                           0.581 * v_channel), 0, 1)
            b[x, y] = clip((y_channel[x, y] + 2.032 * u_channel), 0, 1)

    rgb_img = dstack((r, g, b))
    return rgb_img


if __name__ == '__main__':
    img = imread('C:\cs173\\test_image.png')
    img_f = img_as_float(img)
    yuv_img = rgb_to_yuv(img_f)
    rgb_img = yuv_to_rgb(yuv_img)
    rgb_img = img_as_ubyte(rgb_img)
    imsave('rgb_to_yuv.png', rgb_img)
