import numpy as np
import pandas as pd

def response_time(path):
    """
    path = exact path of transcript file ex : response_time('341_TRANSCRIPT.csv')
    returns single value which is average response time for each question in seconds
    """
    df = pd.read_csv(path,sep='\t')
    array = []
    for i in range(0,df.shape[0]-1):
        if(df.iloc[i,2]=='Ellie') and (df.iloc[i+1,2]=='Participant'):
            num = df.iloc[i+1,0]-df.iloc[i,1]
            array.append(num)
    np_array = np.array(array)
    return(np_array.mean())