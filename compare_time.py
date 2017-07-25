# -*- coding: utf-8 -*-

import os
import numpy as np
import time
from PIL import Image
from skimage import io
import cv2

root_dir = r"H:\2017AIchallenge\DATA_v.2\2017PathologyAIchallenge\cancer_subset"
file_list = os.listdir(root_dir)

# add a line for difference
"""
# average size of files: 
size = []
for f in file_list:
    fp = os.path.join(root_dir, f)
    s = os.path.getsize(fp)
    size.append(s)
print (np.mean(size))
"""   
 
# openCV方法读取图片时间。
im_number = [1,10,100,500,560]

method = 'opencv'
for n in im_number:
    t1 = time.time()
    for f in file_list[0:n]:
        I = cv2.imread(os.path.join(root_dir, f))
    t2 = time.time()
    tp = t2-t1
    print ("%s read %d images: %.3f s" %(method, n, tp))

# PIL
method = 'PIL'
for n in im_number:
    t1 = time.time()
    for f in file_list[0:n]:
        I = Image.open(os.path.join(root_dir, f))
    t2 = time.time()
    tp = t2-t1
    print ("%s read %d images: %.3f s" %(method, n, tp))


# skimage 
method = 'skimage'
for n in im_number:
    t1 = time.time()
    for f in file_list[0:n]:
        I = io.imread(os.path.join(root_dir, f)) # array
    t2 = time.time()
    tp = t2-t1
    print ("%s read %d images: %.3f s" %(method, n, tp))

# VIPS:
#from gi.repository import Vips    

# save image
    