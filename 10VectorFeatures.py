
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy.spatial import distance
from numpy import linalg as L


# In[22]:


def d(x):
    data=pd.read_csv(x)
    p55=data[[' x55',' y55']]
    p49=data[[' x49',' y49']]
    p65=data[[' x65',' y65']]
    p61=data[[' x61',' y61']]
    p52=data[[' x52',' y52']]
    p58=data[[' x58',' y58']]
    p31=data[[' x31',' y31']]
    p25=data[[' x25',' y25']]
    p20=data[[' x20',' y20']]
    p22=data[[' x22',' y22']]
    p23=data[[' x23',' y23']]
    p27=data[[' x27',' y27']]
    p18=data[[' x18',' y18']]
    p2=data[[' x2',' y2']]
    p16=data[[' x16',' y16']]
    p4=data[[' x4',' y4']]
    p14=data[[' x14',' y14']]
    p8=data[[' x8',' y8']]
    p10=data[[' x10',' y10']]
    p37=data[[' x37',' y37']]
    p40=data[[' x40',' y40']]
    p38=data[[' x38',' y38']]
    p42=data[[' x42',' y42']]
    p43=data[[' x43',' y43']]
    p46=data[[' x46',' y46']]
    p44=data[[' x44',' y44']]
    p48=data[[' x48',' y48']]
    p55=np.array(p55)
    p49=np.array(p49)
    p65=np.array(p65)
    p61=np.array(p61)
    p52=np.array(p52)
    p58=np.array(p58)
    p31=np.array(p31)
    p25=np.array(p25)
    p20=np.array(p20)
    p22=np.array(p22)
    p23=np.array(p23)
    p27=np.array(p27)
    p18=np.array(p18)
    p2=np.array(p2)
    p16=np.array(p16)
    p4=np.array(p4)
    p14=np.array(p14)
    p8=np.array(p8)
    p10=np.array(p10)
    p37=np.array(p37)
    p40=np.array(p40)
    p38=np.array(p38)
    p8=np.array(p8)
    p10=np.array(p10)
    p37=np.array(p37)
    p40=np.array(p40)
    p38=np.array(p38)
    p42=np.array(p42)
    p43=np.array(p43)
    p46=np.array(p46)
    p44=np.array(p44)
    p48=np.array(p48)
    p55=p55[::3]
    p49=p49[::3]
    p65=p65[::3]
    p61=p61[::3]
    p52=p52[::3]
    p58=p58[::3]
    p31=p31[::3]
    p25=p25[::3]
    p20=p20[::3] 
    p22=p22[::3]
    p23=p23[::3]
    p27=p27[::3]
    p18=p18[::3]
    p2=p2[::3]
    p16=p16[::3]
    p4=p4[::3]
    p14=p14[::3]
    p8=p8[::3]
    p10=p10[::3]
    p37=p37[::3]
    p40=p40[::3]
    p38=p38[::3]
    p42=p42[::3]
    p43=p43[::3]
    p46=p46[::3]
    p44=p44[::3]
    p48=p48[::3]
    def dist(p1,p2):
        n=len(p1)
        dis=np.empty([n,1])
        for i in range(n):
            a=(p1[i,0],p1[i,1])
            b=(p2[i,0],p2[i,1])
            dis[i]=distance.euclidean(a,b)
        return dis
    #average of distances between 2 points
    def avg(d1,d2):
        n=len(d1)
        a=np.empty([n,1])
        for i in range(n):
            a[i]=(d1[i]+d2[i])/2
        return a
    dis5549=dist(p55,p49)
    dis6561=dist(p65,p61)
    horizontal_mouth=avg(dis5549,dis6561)
    vertical_mouth=dist(p52,p58)
    vertical_ibrows=avg(dist(p31,p25),dist(p31,p20))
    horizontal_ibrows=avg(dist(p22,p23),dist(p27,p18))
    horizontal_head=avg(dist(p2,p16),dist(p4,p14))
    vertical_head=avg(dist(p22,p8),dist(p23,p10))
    horizontal_lefti=dist(p37,p40)
    vertical_lefti=dist(p38,p42)
    horizontal_righti=dist(p43,p46)
    vertical_righti=dist(p44,p48)
    w=np.column_stack((horizontal_lefti,vertical_lefti,horizontal_righti,vertical_righti,horizontal_mouth,vertical_mouth,horizontal_ibrows,vertical_ibrows,horizontal_head,vertical_head))
    result=pd.DataFrame(w)
    return result


# In[23]:


print(d('481_CLNF_features.txt'))

