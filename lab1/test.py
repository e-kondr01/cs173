from skimage.io import imread, imshow, imsave


def compare_colour(pixel, border_colour):
    return True if (pixel[0] == border_colour[0] and
                    pixel[1] == border_colour[1] and
                    pixel[2] == border_colour[2]) else False


img = imread('C:\cs173\lab1\\tiger-border.png')
red, green, blue = img[0, 0]
border_colour = [red, green, blue]
x, y = img.shape[0], img.shape[1]
start_left = 0
count_left = 1
while compare_colour(img[x//2, start_left + 1], border_colour):
    count_left += 1
    start_left += 1
start_top = 0
count_top = 1
while compare_colour(img[start_top + 1, y//2], border_colour):
    count_top += 1
    start_top += 1
start_right = y
count_right = 0
while compare_colour(img[x//2, start_right - 1], border_colour):
    count_right += 1
    start_right -= 1
start_bot = x
count_bot = 0
while compare_colour(img[start_bot - 1, y//2], border_colour):
    count_bot += 1
    start_bot -= 1
print(count_left, count_top, count_right, count_bot)
