import pandas as pd
p = pd.read_csv('Datasets/FastFoodRestaurants.csv', delimiter=',')

# Displaying 

print(f'File: {p}')

print('File Review:\n', p.to_string())            # all values 
print("Data Type of File:\n",p.dtypes)
p.info()
print('Only First Three Rows:\n',p.head(3))
print('Last Two Rows:\n',p.tail(2))
print('Some Statistics Functions Applied:\n',p.describe())
print('Shape of Datset:\n', p.shape)

# Access Column with name

column1 = p['address']
print('Address: ', column1.to_string())
# Multiple columns
column_2_3 = p[['city','country']]
print('City and Country: ', column_2_3)

# Only index used to show 

column_4 = p.loc[4]
print('Column 4: ', column_4)
# Multiple
column_5_6 = p.loc[[5,6]]
print('Column 5 and 6',column_5_6)

# Slice of rows

slice_row = p.loc[0:4]
print('Rows 1 to 4: ', slice_row)

# Slice with condtions 

restaurant = p.loc[p['name'] == 'McDonald\'s']
print('Only Residentials are:\n',restaurant.to_string())

# Only one column

only_column = p.loc[:,'address']
print('Only Address:\n',only_column)

# Multiple columns

multi_column = p.loc[:,'city':'country']
print("Only Two Columns:\n",multi_column)

# Slice of rows and columns

date_year = p.loc[:6,'city':'longitude']
print("First Seven Rows with city,country,keys,latitude and longitude:\n", date_year)

# Conditioning with slicing

property_type = p.loc[p['name'] == 'McDonald\'s','latitude':'longitude']
print("Only McDonald\'s:\n ",property_type)

# New indexing 

p_new = pd.read_csv('Datasets/FastFoodRestaurants.csv', index_col = 'keys')

# No nan problems

fill = {col: (0 if p_new[col].dtype != 'object' else 'N/A') for col in p_new.columns}
p_new = p_new.fillna(value=fill)

print('Only:\n',p_new)
fifth_row = p_new.loc['us/ny/massena/6098statehighway37/-1161002137']
print('Fifth: ',fifth_row)

# Slicing

nowslice = p_new.loc['us/ny/massena/6098statehighway37/-1161002137':'us/sc/batesburg/205wchurchst/-791445730']
print(f'Fifth to Fifteenth Row:\n{nowslice}')

# Now using .iloc

two = p_new.iloc[2]
print('Now with index two:\n',two)
# Multiple
two_three = p_new.iloc[[0,3]]
print('Only First Three Rows',two_three)

# Rows and column both specified 

my_selection = p_new.iloc[0:2,0:1]
print('Selected Square of data frame:\n',my_selection)
print(my_selection.shape)

# Adding Row

print(p.columns.tolist())
p.loc[len(p.index)] = ['139 Columbus Rd',"Athens","US","us/oh/athens/139columbuseffg/990890980",39.3324444,-82.097324,"OMG!! Rotisserie",4570431,'OH',"http://www.omgrotisserie.com,http://omgrotisserie.com"]
print('Addition of a row: ',p.tail(1))

# Removing row

p.drop(142, axis=0,inplace=True)
print('After Removal:\n',p.tail(1))

# Removing columns

p.drop(['websites','postalCode'], axis=1,inplace=True)
print(p.columns.tolist())
p.rename(columns={'country': 'Country'}, inplace=True)
p.rename(mapper={'province': 'Province','city':'City'},axis= 1, inplace=True)
print("Changed column names:\n",p)

# Rename rows

p.rename(index={0:10},inplace=True)
p.rename(mapper={1:20,2:30,3:40},axis=0,inplace=True)
print("Rows index Changed:\n",p)

# Selecting row with condition

select_row = p.query('latitude < 100')
print(select_row.to_string())
print(len(select_row))

# Display data

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Final Data:\n',p)

# Sorting by key address

sort_add = p.sort_values(by='address')
print('Sorting by Address:\n',sort_add.to_string(index=False))

# Sorting columns 

sort_1 = p.sort_values(by =['latitude','longitude'])
print('Sorting by Latitude and Longitude:\n',sort_1.to_string(index=False))

# using groupby

grouped = p.groupby('longitude')['latitude'].sum()
print(grouped.to_string())
print('Grouping:\n',len(grouped))

# Cleaning 

p_clean = p.dropna()
print(p_clean)

# Data list

lists = [6,8,9,10]
array1 = pd.array(lists)
print(array1)

# Now with data type

array2 = pd.array([1.56645454,2.55,7676.23,4.76],dtype='float')
print(array2)