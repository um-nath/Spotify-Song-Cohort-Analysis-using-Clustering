# Outlayer calculation
import numpy as np
import pandas as pd

def outlayer(df, column):
    
    Q1 = np.percentile(df[column], 25)
    Q3 = np.percentile(df[column], 75)

    print('Q1 =', Q1)
    print('Q3 =', Q3)

    IQR = Q3 - Q1
    print('IQR =', IQR)

    lower_lim = Q1 - 1.5 * IQR
    upper_lim = Q3 + 1.5 * IQR

    outlayers = len(df[df[column] < lower_lim]) + len(df[df[column] > upper_lim])

    percentage_of_outlayers = outlayers/len(df[column]) * 100
    print('percentage_of_outlayers = ',percentage_of_outlayers)
    
    return percentage_of_outlayers