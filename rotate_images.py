import pandas as pd
import numpy as np
from skimage import io
from skimage.transform import rotate
import cv2
import os
import time
import random



def pre_images(file_path):
    '''
    Rotates image based on a specified amount of degrees

    INPUT
        file_path: file path to the folder containing images.
        degrees_of_rotation: Integer, specifying degrees to rotate the
        image. Set number from 1 to 360.
        lst_imgs: list of image strings.

    OUTPUT
        Images rotated by the degrees of rotation specififed.
    '''
    pathdir=os.listdir(file_path)
    for l in pathdir:
        img = io.imread(file_path + l)
        ran=random.randint(1,6)
        if ran == 4:
            img = rotate(img, 90)
        elif ran ==5:
            img =rotate(img,270)
        else:
            img = cv2.flip(img, ran-2)
        io.imsave(file_path + str(l) + '_' + str(ran) + '.jpeg', img)


def pre_images1(file_path):
    '''
    Rotates image based on a specified amount of degrees

    INPUT
        file_path: file path to the folder containing images.
        degrees_of_rotation: Integer, specifying degrees to rotate the
        image. Set number from 1 to 360.
        lst_imgs: list of image strings.

    OUTPUT
        Images rotated by the degrees of rotation specififed.
    '''
    pathdir=os.listdir(file_path)
    for l in pathdir:
        img = io.imread(file_path + l)
        for ran in range(1,6):
            if ran == 4:
                img = rotate(img, 90)
            elif ran ==5:
                img =rotate(img,270)
            else:
                img = cv2.flip(img, ran-2)
            io.imsave(file_path + str(l) + '_' + str(ran) + '.jpeg', img)


if __name__ == '__main__':
    start_time = time.time()


    # Mirror Images with no DR one time
    print("Mirroring Non-DR Images")
    pre_images('G:/data/DM/')


    # Rotate all images that have any level of DR
    print("Rotating 90 Degrees")
    pre_images1('G:/data/DR/')

    print("Completed")
    print("--- %s seconds ---" % (time.time() - start_time))
