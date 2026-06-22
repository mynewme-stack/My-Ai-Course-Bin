import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Datasets/RealEstate-USA.csv',delimiter=',')
fill = {col:(0 if df[col].dtype != 'object' else 'N/A') for col in df.columns}
df.fillna(fill, inplace=True)
print(f'Data frame:\n{df}')

df_melt = df[['price','house_size','bed','bath','status']].melt(id_vars='status', var_name= 'measurement', value_name='value')

# 13.                                  STRIPPLOT

sns.set_theme(style='whitegrid')
fig, ax = plt.subplots(figsize=(13,7))
sns.stripplot(x= 'value', y= 'measurement', hue= 'status', palette='Set2', size=4, alpha=0.7 , data=df_melt,jitter=True,dodge= True,ax= ax)
ax.set_xscale('log')
plt.tight_layout()
plt.title('Status VS Price')
plt.show()

# 14.                                 JOINPLOT

sns.set_theme(style='ticks')
g = sns.JointGrid(data=df, x= 'brokered_by',y= 'price',marginal_ticks=True )
g.ax_joint.set(xscale= 'log',yscale='log')
cax = g.figure.add_axes([.15,.55,.02,.2])
g.plot_joint(sns.histplot,discrete= (True,False),
             cmap="light:#03012d", pmax= .8, cbar= True, cbar_ax=cax )
g.plot_marginals(sns.histplot, element = 'step',color="#03012d")
plt.show()

# 15.                                 JOINPLOT

g = sns.jointplot(data=df, x= 'brokered_by', y= 'street', hue= 'status', kind='kde')
plt.show()

# 16.                                 FACETGRID   

sns.set_theme(style='white',rc={'axes.facecolor': (0,0,0,0)})
g = sns.FacetGrid(data=df, row='bed', hue='bed',aspect=12, height=6, palette='crest')
g.map(sns.kdeplot, 'price', fill= True, alpha=0.8, bw_adjust= 0.6)
g.figure.subplots_adjust(hspace=-0.4)
g.set(yticks=[],ylabel='',title='')
g.despine(left=True,bottom=True)
plt.show()

# 17.                                 BOXENPLOT

sns.set_theme(style='whitegrid')
sns.boxenplot(x='status', y='price', palette='Set2', color='b', data=df)
plt.show()

# 18.                                SCATTERPLOT

sns.set_theme(style= 'whitegrid')
sns.kdeplot(x= 'price', y= 'brokered_by', data=df, fill= True, cmap= 'Blues',hue='status', levels = 20, alpha= 0.3 )
sns.scatterplot(data= df, x= 'price', y= 'brokered_by', hue= 'status',s=15)
plt.show()

# 19.                                LMPLOT

sns.lmplot(data=df, x= 'price', y= 'house_size', hue= 'status',scatter_kws={'s':15, 'alpha':0.6}, palette= 'Set1')
plt.show()

# 20.                               FACETGRID

df_less = df.head(30)
g= sns.FacetGrid(data=df_less, col= 'city', col_wrap=4, height=2)
g.map_dataframe(sns.scatterplot, x= 'price', y= 'house_size', hue='status', s=15, annot=True, fmt='.2f', cmap='coolwarm', center=0, linewidths=0.5)
g.set_axis_labels('Price','House Size')
g.add_legend()
plt.show()

# 21.                              HEATMAP

df_more = df[["price","house_size","bed","bath","acre_lot"]].corr()
sns.heatmap(df_more)
plt.show()

# 22.                              JOINGRID

mine = sns.jointplot(data=df, x = 'price', y= 'house_size', kind='kde')
mine.plot(sns.scatterplot, sns.histplot)
plt.show()

# 23.                              KDEPLOT

sns.kdeplot(data=df, x= 'price', y= 'street', hue='status')
plt.show()

# 24.                              DISPLOT

sns.displot(data= df, x = 'price', hue='status', kind='kde', multiple= 'stack', fill= True, palette='Blues')
plt.show()