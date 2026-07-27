# 6. Percentage Change and Cumulative Return
import numpy as np 
price = np.array([100,105,110,120,125])
daily = np.diff(price)/ price[:-1]
cumulative = (price[-1]-price[0])/price[0]
print(f'Daily: {daily}\nCumulative: {cumulative}')