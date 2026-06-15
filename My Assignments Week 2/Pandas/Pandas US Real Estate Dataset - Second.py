import pandas as pd
p = pd.read_csv('Datasets/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',',parse_dates=['Date Recorded'], date_format={'date_added': '%m/%d/%Y'} )

# Removing Nan 

fill = {i: (0 if p[i].dtype != 'object' else 'N/A') for i in p.columns} # If data type = int, float than 0 else String than also 0  
p = p.fillna(value=fill)                                          

# Displaying 

print('\nFile Review:\n', p.to_string())            # all values 
print("\nData Type of File:\n",p.dtypes)
print('\nInformation:\n',p.info)

print('\nOnly First Three Rows:\n',p.head(3))
print('\nLast Two Rows:\n',p.tail(2))
print('\nStatistics:\n',p.describe())

print('\nShape:\t', p.shape)

# Accessing Specific Columns

column1 = p['Serial Number']
print('Serial:\n', column1.to_string())

# Two Columns

column_2_3 = p[['List Year','Date Recorded']]
print('Column List Year and Date:\n\n', column_2_3)

# Only index used to show columns 

column_4 = p.loc[4]
print('Column 4:\n', column_4)

# Multiple columns with just index

column_5_6 = p.loc[[5,6]]
print('Fifth and Sixth Row:\n',column_5_6.to_string())

# Slice of rows while using index

slice_row = p.loc[0:4]
print('First Five Rows:\n', slice_row.to_string())

# slice with condtions 

residential = p.loc[p['Property Type'] == 'Residential']
print('Only residentials are:\n',residential.to_string())

# only one column
only_column = p.loc[:,'Serial Number']
print('only serial numbers',only_column)
#multi
multi_column = p.loc[:,'Serial Number':'List Year']
print("only 2 columns",multi_column)
# slice of columns
date_year = p.loc[:5,'List Year':'Date Recorded']
print("First five dates and years:\n", date_year)
# more than one with a condtion
property_type = p.loc[p['Property Type']=='Commercial','Serial Number':'List Year']
print("Commercial:\n ",property_type)
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
#all
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('final:',p)
# storing in ascending order
sorted_p= p.sort_values(by='Sale Amount')
print(sorted_p.to_string(index=False))
# sorting columns 
df1 = p.sort_values(by =['serial Number','Sale Amount'])
print(df1.to_string(index=False))
# groupby
grouped = p.groupby('Property Type')['Sale Amount'].sum()
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
array2 = pd.array([2020177],dtype='float')
print(array2)