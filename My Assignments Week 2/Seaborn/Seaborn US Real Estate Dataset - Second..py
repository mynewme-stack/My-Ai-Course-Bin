import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Datasets/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',')
print(f'DataFrame:\n{df}')

# 1.                                                LINEPLOT

# Data for graph
new_df = df.query('`Sale Amount` < 100000 and `Sales Ratio` < 100')

# Lineplot with darkgrid
sns.set_theme(style='darkgrid')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.title('Sale Amount VS Sales Ratio')
plt.tight_layout()
plt.show()

# Lineplot with whitegrid
sns.set_theme(style='whitegrid')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.title('Sale Amount VS Sales Ratio')
plt.show()

# Lineplot with dark
sns.set_theme(style= 'dark')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.title('Sale Amount VS Sales Ratio')
plt.show()

# Lineplot with white
sns.set_theme(style= 'white')
sns.lmplot(x = 'Sale Amount', y = 'Sales Ratio',data= new_df)
plt.title('Sale Amount VS Sales Ratio')
plt.show()

# New Indexing

data = pd.read_csv('Datasets/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', index_col= 'Serial Number')
print(data.dtypes)
dfillter = df.head(50)

# 2.                                              SCATTERPLOT

sns.set_theme(style='darkgrid')
sns.scatterplot(x = 'Sale Amount', y = 'Sales Ratio', data = dfillter)
plt.title('Sale Amount (USD) and Sales Ratio')
plt.show()

# Ticks theme

sns.set_theme(style='ticks')
sns.scatterplot(x='Sale Amount', y = 'Sales Ratio', data= dfillter)
plt.title('Sale Amount (USD) VS Sales Ratio')
plt.show()

# 3.                                     LINEPLOT

new_dff = df.query('`Sale Amount` < 100000 and `Sales Ratio` < 2')

sns.set_theme(style='darkgrid')
sns.lineplot(x = 'Sale Amount' , y= 'Sales Ratio', data= new_dff,  hue='List Year')
plt.title('Sales Ratio VS Sale Amount')
plt.show()

# 4.                                     DISPLOT

# hist
sns.set_theme(style='ticks', rc= {'axes.facecolor':'white', 'grid.color': 'grey'})                 
sns.displot(x = 'Sales Ratio', data= new_df, kind='hist')    # For vertical bars                                 
plt.tight_layout()
plt.show()

sns.set_theme(style='darkgrid', rc={'grid.color': 'grey'} )
sns.displot(y = 'Sale Amount', data= new_df, kind='hist')     # For horizontal   
plt.tight_layout()
plt.show()

# 5.                                     REPLOT

new_dfff = df.sort_values(by='Date Recorded')
sns.set_theme(style='ticks', rc = {'axes.facecolor': 'white'})
sns.relplot(x= 'Date Recorded', y='Sales Ratio',hue='List Year', data= new_df, kind='line')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()

# 6.                                    CATPLOT

sns.set_theme(style='darkgrid')
sns.catplot(x='Property Type', y='Sales Ratio',hue='List Year', kind='bar', data= new_df,height=6)
plt.tight_layout()
plt.xticks(rotation= 10)
plt.show()

# 7.                                    BOXPLOT                             

sns.set_theme(style='darkgrid')
sns.boxplot(x='Property Type', y='Sales Ratio',hue='List Year', data= new_df)
plt.tight_layout()
plt.show()

# 8.                                   VIOLINPLOT

sns.set_theme(style='dark')
sns.violinplot(x='Property Type', y='Sales Ratio',hue='List Year', data= new_df)
plt.tight_layout()
plt.show()

# 9.                                   RELPLOT

sns.set_theme(style='ticks')
sns.relplot(x='Sale Amount', y='Sales Ratio', data= new_df, color= 'blue')
plt.tight_layout()
plt.show()

# 10.                                  JOINPLOT

sns.set_theme(style='ticks')
sns.jointplot(x='Sale Amount', y='Sales Ratio',kind='hex', data= new_df)
plt.show()

# 11.                                 HISTPLOT

sns.set_theme(style='ticks')
sns.histplot(x = 'Sales Ratio', data= df,multiple='stack', hue= 'Residential Type')   
plt.show()

# 12.                                  BOXPLOT                               

sns.set_theme(style='ticks')
sns.boxplot(x = 'Sales Ratio', data= df, hue= 'Residential Type')
plt.show()