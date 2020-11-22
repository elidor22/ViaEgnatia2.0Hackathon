import string
import random

import cv2
import os


def flip(filename='', input=''):
    img = cv2.imread('dataset/images/Church of Saint Mary in Apollonia/73f693ed86c29b602e5dc233d73c4921.jpg')

    def horizontal_flip(img, flag):
        if flag:
            return cv2.flip(img, 1)
        else:
            return img

    img = horizontal_flip(img, True)
    cv2.imwrite(filename, img)


directory = 'dataset/images'
filenames = []
images = []
for folder in os.listdir(directory):
    for image in os.listdir(directory + '/' + folder):
        filenames.append(directory + '/' + folder + '/' + image)
        images.append(image)
print(filenames)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str + '.jpg'


i = 0
for file in filenames:
    img = cv2.imread(file)
    img = cv2.flip(img, True)
    cv2.imwrite('images/augmented' + '/' + 'tst'+i+ '.jpg', img)
