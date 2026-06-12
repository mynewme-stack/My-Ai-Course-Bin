import pandas as pd
p = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',',parse_dates=['Date Recorded'], date_format={'date_added': '%m/%d/%Y'} )
fill_values = {col: (0 if p[col].dtype != 'object' else 'N/A') for col in p.columns}
p = p.fillna(value=fill_values)
print('File review:\n', p.to_string())
































