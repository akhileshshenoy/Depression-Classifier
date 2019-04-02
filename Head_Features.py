
# coding: utf-8

# In[7]:

import numpy as np
import pandas as pd
from scipy.spatial import distance
from numpy import linalg as L
import math
from scipy import stats


# In[8]:

def HeadMotion(X,Y,ti):
    x = X[::ti]
    y = Y[::ti]
    vertical = []
    horizontal = []
    net = []
    for i in range(len(x)-1):
        dy = y[i+1] - y[i]
        dx = x[i+1] - x[i]
        vertical.append(abs(dy))
        horizontal.append(abs(dx))
        net.append(math.sqrt((dy)**2 + (dx)**2))
    params = {'vertical' : vertical , 'horizontal' : horizontal , 'net' : net}
    return params


# In[9]:

def head(path,rate):
    data = pd.read_csv("path")
    X2 = data[[' x2']]
    Y2 = data[[' y2']]
    X4 = data[[' x4']]
    Y4 = data[[' y4']]
    X14 = data[[' x14']]
    Y14 = data[[' y14']]
    X16 = data[[' x16']]
    Y16 = data[[' y16']]
    X2 = np.array(X2)
    X4 = np.array(X4)
    X14 = np.array(X14)
    X16 = np.array(X16)
    Y2 = np.array(Y2)
    Y4 = np.array(Y4)
    Y14 = np.array(Y14)
    Y16 = np.array(Y16)
    p2 = HeadMotion(X2,Y2,rate)
    p4 = HeadMotion(X4,Y4,rate)
    p14 = HeadMotion(X14,Y14,rate)
    p16 = HeadMotion(X16,Y16,rate)
    data['P2_mean_horiz'] = np.mean(p2['horizontal'])
    data['P2_median_horiz'] = np.median(p2['horizontal'])
    data['P2_mode_horiz'] = stats.mode(p2['horizontal'])
    data['P2_mean_vert']= np.mean(p2['vertical'])
    data['P2_median_vert'] = np.median(p2['vertical'])
    data['P2_mode_vert'] = stats.mode(p2['vertical'])
    data['P2_mean_net'] = np.mean(p2['net'])
    data['P2_median_net'] = np.median(p2['net'])
    data['P2_mode_net'] = stats.mode(p2['net'])

    data['P4_mean_horiz'] = np.mean(p4['horizontal'])
    data['P4_median_horiz'] = np.median(p4['horizontal'])
    data['P4_mode_horiz'] = stats.mode(p4['horizontal'])
    data['P4_mean_vert']= np.mean(p4['vertical'])
    data['P4_median_vert'] = np.median(p4['vertical'])
    data['P4_mode_vert'] = stats.mode(p4['vertical'])
    data['P4_mean_net'] = np.mean(p4['net'])
    data['P4_median_net'] = np.median(p4['net'])
    data['P4_mode_net'] = stats.mode(p4['net'])
    
    data['P14_mean_horiz'] = np.mean(p14['horizontal'])
    data['P14_median_horiz'] = np.median(p14['horizontal'])
    data['P14_mode_horiz'] = stats.mode(p14['horizontal'])
    data['P14_mean_vert']= np.mean(p14['vertical'])
    data['P14_median_vert'] = np.median(p14['vertical'])
    data['P14_mode_vert'] = stats.mode(p14['vertical'])
    data['P14_mean_net'] = np.mean(p14['net'])
    data['P14_median_net'] = np.median(p14['net'])
    data['P14_mode_net'] = stats.mode(p14['net'])
    
    data['P16_mean_horiz'] = np.mean(p16['horizontal'])
    data['P16_median_horiz'] = np.median(p16['horizontal'])
    data['P16_mode_horiz'] = stats.mode(p16['horizontal'])
    data['P16_mean_vert']= np.mean(p16['vertical'])
    data['P16_median_vert'] = np.median(p16['vertical'])
    data['P16_mode_vert'] = stats.mode(p16['vertical'])
    data['P16_mean_net'] = np.mean(p16['net'])
    data['P16_median_net'] = np.median(p16['net'])
    data['P16_mode_net'] = stats.mode(p16['net'])
    

# In[10]:

head("341")


# In[ ]:




# In[ ]:




# In[ ]:



