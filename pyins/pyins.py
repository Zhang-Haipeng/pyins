# Python3 
# Author: roc_zhang@hotmail.com

import os
from os import listdir, getcwd
import matplotlib.pyplot as plt
import numpy as np


def land_split(pic_name, color='b'):
    """
    docstring to be added.
    """
    root_path = os.getcwd()
    print("Splitting: {}".format(pic_name))
    pic_org = plt.imread(root_path+'/'+pic_name)
    ins_hight = 2560
    ins_width = 2048
    ratio = ins_width * 2 / ins_hight
    l = round(pic_org.shape[0] * ratio)
    l_half = round(l/2)
    fill_color = 255 if color=='w' else 0
    canvas_left = np.full((pic_org.shape[0], l_half, 3), fill_color)
    canvas_right = np.full((pic_org.shape[0], l_half, 3), fill_color)
    split = round(pic_org.shape[1] / 2)
    canvas_left[:, -split:, :] = pic_org[:, :split, :]

    if pic_org.shape[1] % 2 == 0:
        canvas_right[:, :split, :] = pic_org[:, split:, :]
    else:
        try:
            canvas_right[:, :split-1, :] = pic_org[:, split:, :]
        except:
            canvas_right[:, :split+1, :] = pic_org[:, split:, :]

    canvas_left = canvas_left.astype(float) / 255
    canvas_right = canvas_right.astype(float) / 255
    # make the 3rd pic
    width_3 = pic_org.shape[1]
    hight_3 = round(width_3 * (ins_hight / ins_width))
    canvas_3 = np.full((hight_3, width_3, 3), fill_color)

    split_2 = round((hight_3 - pic_org.shape[0])/2)
    canvas_3[split_2:(split_2 + pic_org.shape[0]),:,:] = pic_org
    canvas_3 = canvas_3.astype(float) / 255

    output_path = root_path + "/output/"
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    plt.imsave((output_path + pic_name[:-4] + '_left.jpg'), canvas_left)
    plt.imsave((output_path + pic_name[:-4] + '_right.jpg'), canvas_right)
    plt.imsave((output_path + pic_name[:-4] + '_centered.jpg'), canvas_3)
    print("Done.")
    
    return 


def split_black_all():
    """
    docstring to be added.
    """
    pic_list = [x for x in os.listdir() if x[-4:] in [".jpg" or ".JPG"]]
    for pic_name in pic_list:
        land_split(pic_name=pic_name)
    print("All done.")

def split_white_all():
    """
    docstring to be added.
    """
    pic_list = [x for x in os.listdir() if x[-4:] in [".jpg" or ".JPG"]]
    for pic_name in pic_list:
        land_split(pic_name=pic_name, color='w')
    print("All done.")

