import pandas as pd
p = pd.read_csv('RealEstate-USA.csv',delimiter=",")
p.fillna(0, inplace=True)
print(f'Uploading file:\n{p}')
# Data type 
print("Data type of file:\n",p.dtypes)
# Info
p.info()
# Displaying any part of rows
print("First four rows\n",p.head(4))
print("Last five rows\n", p.tail(5))
# Desciribe to describe stats
print("Summary of Statistics:\n",p.describe())
# shape
print("Shape of file:\n",p.shape)
# printing one column
status = p['status']
print("Only status of real us estates:\n",status)
# multiple columns
status_price = p[["status","price"]]
print("Status and price:\n",status_price)
# Now only i row
second = p.loc[2]
print("Selecting second row:\n",second)
# Multi rows
third_fourth = p.loc[[3,4]]
print("Selecting third and fourth rows:\n",third_fourth)
# slice of rows better way
slice_row = p.loc[0:4]
print("Row sliced from 0 to 4:\n", slice_row)
# conditional
available = p.loc[p['status']=='for_sale']
print("Available house:\n",available)
# Not avaiable
unavailable = p.loc[p['status']=='not_for_sale']
print("Not for sale:\n",unavailable)
# single column selection
column1= p.loc[:,'street']
print("Single column:\n", column1)
# multi colun
column2_3 = p.loc[:,['bed','bath']]
print("Bedrooms and bathrooms:\n", column2_3)
# slice column
slice_col = p.loc[:3, 'bed':'bath']
print("slice of column:\n", slice_col)
# combined rows and column combined
rows_column = p.loc[p['status']=='for_sale','brokered_by': 'acre_lot']
print("Now combined method trying:\n",rows_column)
# new index
pd_index = pd.read_csv("RealEstate-USA.csv",delimiter=",",index_col='street')
print(pd_index)
print(pd_index.dtypes)
print("Information:\n",pd_index.info())
# single row
fourth_row = pd_index.loc[1962661]
print("fourth row:", fourth_row)
# now 2 rows 
fifth = pd_index.loc[1404990]
print("Fifth row:\n",fifth)
# slice of row
pd_index.fillna(0, inplace=True)
both_sliced = pd_index.loc[1962661:1404990]
print("Now using slicing:\n",both_sliced)
# i loc
third_row = pd_index.iloc[0]
print("Using iloc:\n", third_row)
# multiple rows
three_four = pd_index.iloc[[2,3]]
print("Only three and four:\n", three_four)
# slice of columns
column = pd_index.iloc[:,2:3]
print("selecting columns:\n", column)
# combine rows and columns 
colrow = pd_index.iloc[[1,9],2:3] 
print("Now combined:\n", colrow)
 # how many columns exist
print(len(p.columns)) 
print(p.columns.tolist())
# adding 
p.loc[len(p.index)] = [52707,'not_for_sale',80000,4,2,0.08,1902874,'Adjuntas',"Puerto Rico",601,1527,000]
print('New row:\n',p.tail(1))
#removing
p.drop(1, axis=0, inplace= True)
p.drop(index = 2,inplace=True)
p.drop(3,axis = 0,inplace=True)
p.drop(4,axis = 0,inplace=True)
p.drop(5,axis = 0,inplace=True)
p.drop([198,197,199,200],axis = 0,inplace=True)
print("After removing:\n",p)
# delete column
p.drop('brokered_by',axis=1, inplace=True)
p.drop(columns='status', inplace=True)
p.drop(['bed','bath'], axis=1, inplace=True)
print("After removing:\n",p)
# rename columns
p.rename(columns={'acre_lot': 'acre_alot'}, inplace=True)
p.rename(mapper={'street': 'streets','city':'cities'},axis= 1, inplace=True)
print("after few changes:\n",p)
# rename rows
p.rename(index={6:1},inplace=True)
p.rename(mapper={7:2,8:3,9:4},axis=0,inplace=True)
print("after few changes:\n",p)
# selecting row with condition
select_row = p.query('price < 50000')
print(select_row.to_string)
print(len(select_row))
#all
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('final:',p)
# storing in ascending order
sorted = p.sort_values(by='price')
print(sorted.to_string(index=False))
# sorting columns 
df1 = p.sort_values(by =['price','zip_code'])
print(df1.to_string(index=False))
# groupby
grouped = p.groupby('acre_alot')['house_size'].sum()
print(grouped.to_string())
print('grouped:\n',len(grouped))
# MISSING VALUES
p_clean = p.dropna()
print(p_clean)
# filling nan
p.fillna(0, inplace= True)
print(p)
# data list
lists = [1,2,3,4]
array1 = pd.array(lists)
print(array1)
# now with data type
array2 = pd.array([1.45454,2.565,3.23,4.76],dtype='float')
print(array2)