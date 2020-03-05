from skimage.io import imread, imsave


def downgrade(img, levels_n: int = 256):
    '''Уменьшение кол-ва уровней яркости изображения '''
    levels = []
    for i in range(levels_n + 1):
        levels.append(round(256 / levels_n * i))
    if 256 - levels[len(levels)-2] < 256 // levels_n * 2:
        levels[len(levels)-1] = 255
    print(levels)  # Debug
    rows = img.shape[0]
    cols = img.shape[1]
    for row in range(rows):
        for col in range(cols):
            for i in range(len(levels)):
                if img[row, col][0] < levels[i]:
                    if levels[i-1] == 0:
                        img[row, col] = [0, 0, 0]
                    elif levels[i] == 255:
                        img[row, col] = [255, 255, 255]
                    else:
                        value = (levels[i-1] + levels[i]) // 2
                        img[row, col] = [value, value, value]
                    break
    return img


if __name__ == '__main__':
    # img_name = input('Введите название файла с изображением: ')
    img_name = ('C:\cs173\lab1\eye.jpg')
    img = imread(img_name)
    levels_n = int(input('Введите желаемое кол-во уровней яркости: '))
    downgraded_img = downgrade(img, levels_n)
    imsave(f'downgraded_img_{levels_n}_levels.png', downgraded_img)
