import pandas as pd
p = pd.read_csv('Datasets/FastFoodRestaurants.csv', delimiter=',')

# Displaying 

print(f'File: {p}')

print('File Review:\n', p.to_string())            # all values 
print("Data Type of File:\n",p.dtypes)
print('Information:\n',p.info)
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

# New 

p_new = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',index_col = 'Sale Amount')
fill = {col: (0 if p_new[col].dtype != 'object' else 'N/A') for col in p_new.columns}
p_new=p_new.fillna(value=fill)
print('Only:\n',p_new)
fifth_row = p_new.loc[248400.00]
print('fifth: ',fifth_row)
#slice
nowslice = p_new.loc[248400.00:775000.00]
print(nowslice)
# i loc
two = p_new.iloc[2]
print('Now with index:\n',two)
two_three = p_new.iloc[[0,3]]
print('Only two',two_three)
my_selection = p_new.iloc[0:2,0:2]
print('selected square:\n',my_selection)
print(my_selection.shape)
print(p.columns.tolist())
p.loc[len(p.index)] = [2020177,2020,'04/14/2021','Ansonia','323 BEAVER ST',133000.00,248400.00,0.5354,'Residential','Single Family',None,None,None,'POINT (-73.06822 41.3504)']
print('addition: ',p.tail(1))
# removing
p.drop(142, axis=0,inplace=True)
print('After removal:\n',p.tail(1))
p.drop(['OPM remarks','Location'], axis=1,inplace=True)
print(p.columns.tolist())
p.rename(columns={'Serial Number': 'serial Number'}, inplace=True)
p.rename(mapper={'List Year': 'list year','Date Recorded':'date recorded'},axis= 1, inplace=True)
print("after few changes:\n",p)
# rename rows
p.rename(index={0:1},inplace=True)
p.rename(mapper={1:2,3:1,2:1000000000},axis=0,inplace=True)
print("after few changes:\n",p)
# selecting row with condition
select_row = p.query('`Sale Amount` < 50000')
print(select_row.to_string())
print(len(select_row))
