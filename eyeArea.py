import tensorflow as tf
import pandas as pd
import numpy as np
from scipy import stats

#this funtion returns a pandas dataframe comsisting of area of the eye at different frames
def eyeArea(path,r): #path is the path to clnf_features.txt and r is the frame rate
    data=pd.read_csv(path)
    X=data[[' x0',' x38',' x39',' x40',' x41',' x42']]
    Y=data[[' y37',' y38',' y39',' y40',' y41',' y42']]
    X=np.array(X)
    Y=np.array(Y) 
    xn=X[::r]
    yn=Y[::r]
    def polygonArea(x,y,n):
        area = 0.0
        j = n - 1
        for i in range(0,n): 
            area += (x[j] + x[i]) * (y[j] - y[i]) 
            j = i  
        return int(abs(area / 2.0)) 
    n=int(np.size(xn)/len(xn))
    area=np.empty([len(xn),1])
    for i in range(len(xn)):
        area[i]=polygonArea(xn[i],yn[i],n)
    area=pd.DataFrame(area)
    area.columns = ['Area']
    return area
