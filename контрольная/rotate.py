from math import cos, sin, radians
from skimage.io import imread


def rotate(img, angle: int = 0, rad: bool = False):
    x = img.shape[0]
    y = img.shape[1]
    if not rad:
        a = radians(angle)
    new_x = int(x * abs(sin(a)) + y * abs(cos(a))) + 1
    new_y = int(x * abs(cos(a)) + y * abs(sin(a))) + 1
    return (new_x, new_y)


if __name__ == "__main__":
    img = imread('test_image.png')
    print(rotate(img, 200))
