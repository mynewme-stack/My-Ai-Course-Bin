import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# file

un_df= pd.read_csv('My Final Assessment\\Datasets_Used\\USA-Hospitals\\Hospitals.csv')

""" 
Small: < 100 beds
Medium: 100 – 299 beds
Large: 300+ beds
"""

# Missing vals

print('Missing values : ', un_df.isnull().sum())

# cz my target has a missing value i am deleting that row

un_df = un_df.dropna(subset=["ALT_NAME",'ST_FIPS','OWNER','TTL_STAFF','BEDS','TRAUMA','HELIPAD'])

# Missing vals now

print('Miss values now : ', un_df.isnull().sum())

# Check duplicates 

dupli_row = un_df.duplicated().sum()

print('Duplicate rows : ', dupli_row)

# Overview

print('Info: ',un_df.info)
print('Statistics: ',un_df.describe())
print('Summary: ',un_df.describe(include='all'))
print('Shape: ',un_df.shape)
print('Columns: ',un_df.columns)

# checking target 

#--- min beds

print('Minimum: ',un_df['BEDS'].values <= 0)

#--- max beds

print(un_df['BEDS']>= 1000)

