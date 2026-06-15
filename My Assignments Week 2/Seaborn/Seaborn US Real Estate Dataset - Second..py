import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Datasets/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',')
print(f'DataFrame:\n{df}')

# Data for graph
new_df = df.query('`Sale Amount` < 1000000 and `Sales Ratio` < 10')

# Lineplot with darkgrid
sns.set_theme(style='darkgrid')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.show()

# Lineplot with whitegrid
sns.set_theme(style='whitegrid')
sns.lmplot(x='Sales Ratio', y='Sale Amount',data= new_df)
plt.show()

# Lineplot with dark
sns.set_theme(style= 'dark')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.show()

# Lineplot with white
sns.set_theme(style= 'white')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.show()

# Lineplot with ticks
sns.set_theme(style= 'ticks')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.show()




