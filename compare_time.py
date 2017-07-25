# -*- coding: utf-8 -*-

import os
import time
from PIL import Image
from skimage import io
import cv2
import shutil
import numpy as np

def make_empty_dir(dir_path):
    if not os.path.isdir(dir_path):
        print("make dir")
        os.mkdir(dir_path)
    else:
        print("clear dir\n")
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)

def use_opencv(file_path, output):
    t_ = time.time()
    I = cv2.imread(file_path)
    tp = time.time()-t_
     
    t0 = time.time()
    cv2.imwrite(output, I)        
    ts = time.time()-t0
    
    #print (tp , ts)
    return tp, ts


def use_PIL(file_path, output):
    t_ = time.time()
    I = Image.open(file_path)
    tp = time.time()-t_
    #save_to= os.path.join(root_dir, "copy_%s" )
            
    t0 = time.time()
    I.save(output)        
    ts = time.time()-t0
    
    #print (tp , ts)
    return tp, ts

def use_skimage(file_path, output):
    t_ = time.time()
    I = io.imread(file_path)
    tp = time.time()-t_
    #save_to= os.path.join(root_dir, "copy_%s" )
            
    t0 = time.time()
    io.imsave(output, I)
    ts = time.time()-t0
    #print (tp , ts)
    return tp, ts


root_dir = r"H:\2017AIchallenge\DATA_v.2\2017PathologyAIchallenge\cancer_subset"
file_list = os.listdir(root_dir)
save_path = r"H:\2017AIchallenge\save_image"
make_empty_dir(save_path)

#==============================================================================
# openCV方法读取图片时间。
im_number = [1,10,100,500,560]
result = []
methods = ['opencv', 'PIL', 'skimage']


for method in methods[2:]:
    ts = 0
    tp = 0
    for n in im_number[2:3]:    
        t1 = time.time()  
        
        for f in file_list[0:n]:
            # read:
            f_name, ext = os.path.splitext(f)
            fp = os.path.join(root_dir, f)
            save_to = os.path.join(save_path, "%scopy_%s" %(method, f))
            
            if method == 'opencv':
                t_p, t_s = use_opencv(fp, save_to)

            elif method == 'PIL':
                t_p, t_s = use_PIL(fp, save_to)

            elif method == 'skimage':
                t_p, t_s = use_skimage(fp, save_to)

            tp = tp + t_p
            ts = ts + t_s  
           
        t = time.time()-t1
        print ("%s read %d images: total %.3f s\n read: %.3f\n save :%.3f" %(method, n, t, tp, ts))
        
        time_dict = {'method':method, 'file number':n, 'read':tp, 'save':ts}
        result.append(time_dict)
        
        make_empty_dir(save_path)

"""
import csv 
with open('compare.csv', 'w') as csvfile: 
    writer = csv.writer(csvfile,dialect='excel') 
    writer.writerow(['title', 'summary', 'year', 'id', 'count', 'link'])
    
with open('compare.txt', 'w') as f:
    f.write()
"""    

import json
jsObj = json.dumps(result)
with open('compare.json', 'w') as f:
    f.write(jsObj)
    
    
t = time.time()

I = Image.open(fp)
tr = time.time()
print (tr-t)

I = np.array(I)
tp = time.time()
print (tp-tr)

I.save(save_to)        
ts = time.time()-tps