import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Datasets/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',')
print(f'DataFrame:\n{df}')

sns.set_theme(style='darkgrid')
sns.lineplot(x = 'Sale Amount', y = 'Sales Ratio',data= df)
plt.show()

sns.set_theme(style='darkgrid')
sns.lineplot(x='Sales Ratio', y='Sale Amount',data= df)
plt.show()

sns.set_theme(style= 'whitegrid')
sns.displot(x='Sales Ratio', y='Sale Amount',data= df)
plt.show()

sns.heatmap(x='Sales Ratio', y='Sale Amount',data= df)
plt.show()



