import numpy as np
import pandas as pd

def words_per_minute_feature(path):
    """
    path = exact path of transcript file ex : words_per_minute_feature('300_TRANSCRIPT.csv')
    returns single value which is words per minute spoken by the subject
    """
    df = pd.read_csv(path,sep='\t')
    word_count = 0
    time_count = 0
    for i in range(0,df.shape[0]):
        if(df.iloc[i,2]=='Participant'):
            word_count = word_count + len(df.iloc[i,3].split())
            time_count = time_count + (df.iloc[i,1]-df.iloc[i,0])
    return (word_count/(time_count/60))
