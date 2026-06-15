import pandas as pd
p = pd.read_csv('Datasets/startup_growth_investment_data.csv', delimiter=',')

# Display .csv file

print(f'File .csv:\n{p}')

p.info()
print(f'File Overview:\n{p.to_string()}')
print(f'File Data Type:\n{p.dtypes}')
print('First Row:\n',p.head(1))
print('Last Row:\n',p.tail(1) )
print('Statistic Functions:\n',p.describe())
print('Shape of Dataframe:\n',p.shape)

# Search column with name without .iloc

row_5 = p['Valuation (USD)']
print('USD:\n',row_5.to_string()) 
# Search multiple columns
row_3_4 = p[['Funding Rounds','Investment Amount (USD)']]
print('Funding and Investment Ammount:\n', row_3_4.to_string())

# Using .loc 

row_6 = p.loc[6]
print('Sixth Row:\n',row_6)
# Multiple 
row_7_8 = p.loc[[7,8]]
print('Seventh and Eighth Rows:\n', row_7_8)

# Slicing

row_1_to_4 = p.loc[0:4]
print('Slicing of rows using .loc:\n', row_1_to_4)

# Slicing with condition 

usa = p.loc[p['Country'] == 'USA','Number of Investors':'Growth Rate (%)']
print('Number of investors in USA and their Growth Rate (%):\n',usa)

# Only one columns using .loc

only_col = p.loc[:,'Startup Name']
print('All rows with One Column:\n', only_col)

# Multiple columns

mul_col = p.loc[:, 'Startup Name':'Funding Rounds']
print('Multiple columns and all rows:\n', mul_col)

# Specify rows and column for slicing 

slice_1 = p.loc[:5,'Funding Rounds':'Year Founded'] 
print('\t\t\tSlicing using .loc:\n',slice_1)

# New Indexing

p_new = pd.read_csv('Datasets/startup_growth_investment_data.csv', delimiter=',',index_col='Startup Name')
filled = {i:(0 if p_new[i].dtype != 'object' else 'N/A') for i in p_new.columns}
p_new = p_new.fillna(value=filled)
print('Now:\n', p_new)

# Slicing this series

slice_2 = p_new.loc['Startup_20']
print('Startup 20th Row:\n',slice_2)

# using .iloc

row1 = p_new.iloc[0]
print('\nFirst row with iloc:\n', row1)
# Multiple 
row2_3 = p_new.iloc[1,2]
print('Second and Third row using:\n', row2_3)

# Slicing

my_slice = p_new.iloc[0:,:1]
print('All rows and One column',my_slice)

# Addition of row 

print(p.columns.to_list())
p.loc[len(p.index)] = ['Startup_5001','Fintech',4548,455554391702.87,5133024657475240.6776569563,24,'Singapore',2013,167575609.08]
print(f'\n\n\n\nIts added in the last:\n{p.tail(1)}')

# Now Removing

p.drop(len(p.index)-1, axis = 0, inplace= True)
print('After Removing Tail will be:\n', p.tail(1))

# Now columns removal

p.drop(['Investment Amount (USD)','Year Founded'], axis=1, inplace= True)
print(p.columns.to_list())

# Rename column

p.rename(columns={'Startup Name':'startupname'}, inplace=True)
# Multiple
p.rename(mapper={'Industry': 'industry','Funding Rounds':'fundingrounds'}, axis=1, inplace= True)

# Renaming rows index

p.rename(index={0:10}, inplace=True)
# Multiples
p.rename(index={1:20,2:40,3:60},inplace=True)

# Displaying changes

print('\nChanges:\n\n\n',p)

# Condition

sel_row = p.query('`Growth Rate (%)` < 50.00')
print('Less than 50(%) growth rate:\n', sel_row.to_string())

# Displaying 

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Final:\n',p)

# Sorting by key

sorting = p.sort_values(by='Funding Rounds')
print('Sorting by Funding Rounds:\n', sorting)

# Sorting columns

sorting2 = p.sort_values(by =['Number of Investors','Growth Rate (%)'])
print('Sorting by Investors and Growth Rate (%):\n',sorting2.to_string(index=False))

# Using groupby

grouped = p.groupby('Number of Investors')['Growth Rate (%)'].sum()
print(grouped.to_string())
print('Grouping:\n',len(grouped))

# Cleaning 

p_clean = p.dropna()
print(p_clean)

# Data list

lists = [16,81,92,100]
array1 = pd.array(lists)
print(array1)

# Now with data type

array2 = pd.array([123232.52454,232.535,7637236.23,564.76],dtype='float')
print(array2)