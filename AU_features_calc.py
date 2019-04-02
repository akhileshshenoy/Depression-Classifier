import numpy as np
import pandas as pd
def AU_features(path,step):
    """
    path = file path of a single AU file for a single subject example : AU_features('300_CLNF_AUs.txt')
    returns pandas dataframe with the following info :
    Data columns (total 25 columns):
     AU01_r      6486 non-null float64
     AU02_r      6486 non-null float64
     AU04_r      6486 non-null float64
     AU05_r      6486 non-null float64
     AU06_r      6486 non-null float64
     AU09_r      6486 non-null float64
     AU10_r      6486 non-null float64
     AU12_r      6486 non-null float64
     AU14_r      6486 non-null float64
     AU15_r      6486 non-null float64
     AU17_r      6486 non-null float64
     AU20_r      6486 non-null float64
     AU25_r      6486 non-null float64
     AU26_r      6486 non-null float64
     AU04_c      6486 non-null int64
     AU12_c      6486 non-null int64
     AU15_c      6486 non-null int64
     AU23_c      6486 non-null int64
     AU28_c      6486 non-null int64
     AU45_c      6486 non-null int64
    Happiness    6486 non-null float64
    Sadness      6486 non-null float64
    Fear         6486 non-null float64
    Anger        6486 non-null float64
    Disgust      6486 non-null float64
    dtypes: float64(19), int64(6) 
    """
    data = pd.read_csv(path)                                                                         #path = '300_CLNF_AUs.txt' 
    df = data.iloc[::step,4:]
    df['Happiness'] = df[" AU06_r"]+df[' AU12_r']
    df['Sadness'] = df[" AU01_r"]+df[' AU02_r']+df[" AU05_r"]+df[' AU26_r']
    df['Fear'] = df[" AU01_r"]+df[' AU02_r']+df[" AU04_r"]+df[' AU05_r']+df[" AU20_r"]+df[' AU26_r'] #7
    df['Anger'] = df[" AU04_r"]+df[' AU05_r']                                                        #7+23
    df['Disgust'] = df[" AU09_r"]+df[' AU15_r']                                                      #16
    #print(df.info())
    return df