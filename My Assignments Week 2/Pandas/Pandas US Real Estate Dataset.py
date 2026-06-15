import pandas as pd
p = pd.read_csv('Datasets/RealEstate-USA.csv',delimiter=",")

p.fillna(0, inplace=True)
print(f'Uploading File:\n{p}')

# Data type 

print("Data Type of File:\n",p.dtypes)

# Information

p.info()

# Displaying any part of rows

print("First Four Rows\n",p.head(4))
print("Last Five Rows\n", p.tail(5))

# Using describe() to show statistics

print("Summary of Statistics:\n",p.describe())

# Shape

print("Shape of File:\n",p.shape)

# Printing only one column

status = p['status']
print("Only Status of RealEstate USA :\n",status)

# Multiple columns

status_price = p[["status","price"]]
print("Status and Price:\n",status_price)

# Now only i row

second = p.loc[2]
print("Selecting Second Row:\n",second)

# Multiple rows

third_fourth = p.loc[[3,4]]
print("Selecting Third and Fourth rows:\n",third_fourth)

# Slice of Rows 

slice_row = p.loc[0:4]
print("First Five Rows:\n", slice_row)

# Conditional

available = p.loc[p['status']=='for_sale']
print("Houses for sales:\n",available)

# Not avaiable
unavailable = p.loc[p['status']=='not_for_sale']
print("Houses Not for sale:\n",unavailable)

# Single column selected

column1= p.loc[:,'street']
print("Single column:\n", column1)

# Multiple columns

column2_3 = p.loc[:,['bed','bath']]
print("Bedrooms and Bathrooms:\n", column2_3)

# Slice columns

slice_col = p.loc[:3, 'bed':'bath']
print("Slice of columns:\n", slice_col)

# Condition with coulumns specified

rows_column = p.loc[p['status']=='for_sale','brokered_by': 'acre_lot']
print("Houses for sale with Acre lot:\n",rows_column)

# With new unique Identifier

pd_index = pd.read_csv("Datasets/RealEstate-USA.csv",delimiter=",",index_col='street')
pd_index.fillna(0, inplace=True)
print(pd_index)
print(pd_index.dtypes)
pd_index.info()

# Single row with loc

fourth_row = pd_index.loc[1962661]
print("Fourth Row:", fourth_row)

# Now multiple rows or slice of rows

fifth = pd_index.loc[1404990:1048466]
print("Fifth to Tenth row:\n",fifth)

both_sliced = pd_index.loc[1962661:1404990]
print("Slicing:\n",both_sliced)

# Using .iloc

third_row = pd_index.iloc[0]
print("Using iloc:\n", third_row)

# Multiple rows

three_four = pd_index.iloc[[2,3]]
print("Only Third and Fourth:\n", three_four)

# Slice of columns

column = pd_index.iloc[:,2:3]
print("Selecting Columns:\n", column)

# Combine rows and columns 

col_row = pd_index.iloc[[1,9],2:3] 
print("Now combined:\n", col_row)

# Length 

print(len(p.columns)) 
print(p.columns.tolist())

# Adding a row

p.loc[len(p.index)] = [52707,'not_for_sale',80000,4,2,0.08,1902874,'Adjuntas',"Puerto Rico",601,1527,0]
print('New row:\n',p.tail(1))

# Removing rows and columns

p.drop(1, axis=0, inplace= True)
p.drop(index = 2,inplace=True)
p.drop(3,axis = 0,inplace=True)
p.drop(4,axis = 0,inplace=True)
p.drop(5,axis = 0,inplace=True)
p.drop([198,197,199,200],axis = 0,inplace=True)
print("After Removing:\n",p)

# Delete columns

p.drop('brokered_by',axis=1, inplace=True)
p.drop(columns='status', inplace=True)
p.drop(['bed','bath'], axis=1, inplace=True)
print("After Removing:\n",p)

# Rename columns

p.rename(columns={'acre_lot': 'Acre_lot'}, inplace=True)
p.rename(mapper={'street': 'streets','city':'cities'},axis= 1, inplace=True)
print("After Few Changes:\n",p.to_string())

# Rename rows

p.rename(index={0:1},inplace=True)
p.rename(mapper={2:5,3:10,4:15,5:20},axis=0,inplace=True)
print("Some Few Changes:\n",p.to_string())

# Selecting row with condition

select_row = p.query('`price` < 50000')
print(select_row.to_string())
print(len(select_row))

# Displaying full data

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Final Changes:\n',p)

# Sorting in ascending order

sort0 = p.sort_values(by='price')
print(sort0.to_string(index=False))

# Sorting columns 

sort1 = p.sort_values(by =['price','zip_code'])
print(sort1.to_string(index=False))

# groupby

grouped = p.groupby('Acre_lot')['house_size'].sum()
print(grouped.to_string())
print('Grouped:\n',len(grouped))

# Cleaning 

p_clean = p.dropna()
print(p_clean)

# Filling nan

p.fillna(0, inplace= True)
print(p)

# Data list

lists = [1,2,3,4]
array1 = pd.array(lists)
print(array1)

# Now with data type

array2 = pd.array([1.45454,2.565,3.23,4.76],dtype='float')
print(array2)