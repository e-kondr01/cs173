from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte


def downgrade(img, levels_n: int = 256):
    '''Уменьшение кол-ва уровней яркости изображения'''
    downgraded_img = img // (256 // levels_n)
    return downgraded_img


def restore(img, levels_n: int = 256):
    '''восстановление изображения для просмотра'''
    restored_img = img * (256 // levels_n)
    return restored_img


if __name__ == '__main__':
    # img_name = input('Введите название файла с изображением: ')
    img_name = ('C:\cs173\lab1\eye.jpg')
    img = imread(img_name)
    img_gray = rgb2gray(img)
    img_one_channel = img_as_ubyte(img_gray)
    levels_n = int(input('Введите желаемое кол-во уровней яркости: '))
    downgraded_img = downgrade(img_one_channel, levels_n)
    restored_img = restore(downgraded_img, levels_n)
    imsave(f'restored_img_{levels_n}_levels.png', restored_img)
