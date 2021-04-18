import os
import random
import numpy as np
from numpy import *

target_num = '4'  # tap=0 move=1 zoom=2 grab=3 turn=4
txtfilepath = r"C:\Users\atomicreactor\Desktop\aaa\data_labels\label_tap"
savetxtpath = r"C:\Users\atomicreactor\Desktop\aaa\data_labels\label_tap"
alltxt = os.listdir(txtfilepath)
txts = len(alltxt)
for i in alltxt:
    txtfile = open(txtfilepath + '/' + i, 'r')
    temp_arr = txtfile.readlines()
    temp_arr = target_num+temp_arr[0][1:]
    savefile = open(savetxtpath + '/' + i, 'w')
    savefile.write(temp_arr)
    temp_arr=[]
