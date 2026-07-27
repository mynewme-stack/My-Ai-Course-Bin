import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datasets/startup_growth_investment_data.csv', delimiter= ',')
df.fillna('N/A')
print(df)

# 37.                                               RELPLOT

df_small = df.head(100)
sns.set_theme(style='white')
sns.relplot(data=df_small ,x= 'Startup Name', y= 'Industry', hue='Country', size='Funding Rounds', 
            sizes=(10,500), alpha=.5,palette='muted',height=6, aspect=6)
plt.xticks(rotation=90) 
plt.show()

# 38.                                              SWARMPLOT

sns.set_theme(style='whitegrid',palette='muted')
a = sns.swarmplot(data=df_small, x= 'Industry', y= 'Valuation (USD)', hue='Country')
a.set(ylabel='')
plt.tight_layout()
plt.show()

# 39.                                              PAIRPLOT

sns.set_theme(style='ticks')
sns.pairplot(df_small, hue='Country')
plt.show()

# 40.                                              RELPOT

cmap= sns.cubehelix_palette(rot=-.2,as_cmap=True)
b = sns.relplot(data=df_small,
                x='Startup Name', y='Industry',
                hue='Country', size='Funding Rounds', sizes=(10,200),)
b.set(xscale='log', yscale='log')
b.ax.xaxis.grid(True, 'minor', linewidth=.25)
b.ax.yaxis.grid(True, 'minor', linewidth=.25)
b.despine(left=True, bottom=True)
plt.show()

# 41.                                             VIOLINPLOTS

df_more_small = df.head(30)
sns.violinplot(data=df_small, x= 'Startup Name', y= 'Industry', orient='y', fill=False)
plt.xticks(rotation=90) 
plt.show()

# 42.                                            JOINTGRID

c = sns.JointGrid(data= df_small, x= 'Funding Rounds', y= 'Number of Investors', space=0)
c.plot_joint(sns.kdeplot,fill=True, thresh=0, levels =100, cmap='rocket')
c.plot_marginals(sns.histplot, color="#182185", alpha=1, bins= 25)
plt.tight_layout()
plt.show()

# 43.                                              HEATMAP

f , ax = plt.subplots(figsize=(12,8))
numeric_col = ['Funding Rounds','Number of Investors','Investment Amount (USD)','Valuation (USD)','Year Founded','Growth Rate (%)']
sns.heatmap(data=df_small[numeric_col].corr(), annot=True, fmt='.2f', linewidths=.5, ax=ax)
plt.show()

# 44.                                              CATPLOT

sns.catplot(data=df_small, x= 'Funding Rounds', y= 'Valuation (USD)', hue='Country', native_scale=True, zorder=1)
sns.regplot(data=df_small, x= 'Funding Rounds', y= 'Valuation (USD)', scatter=False, truncate=False, order=2,color='.2')
plt.tight_layout()
plt.show()

# 45.                                             CLUSTERMAP

numeric_col = ['Funding Rounds','Number of Investors','Investment Amount (USD)','Valuation (USD)','Year Founded','Growth Rate (%)']
sns.clustermap(df[numeric_col].corr(), cmap='vlag', figsize=(10,8))
plt.show()

# 46.                                             DISPLOT

sns.displot(data=df_small, x= 'Number of Investors',y='Industry', col='Country', log_scale=(True, False), col_wrap=4, height=4,aspect=.7)
plt.show()

# 47.                                            RELPLOT
 
sns.relplot(data=df_small, x= 'Number of Investors',y='Industry', col='Country', kind='line',hue = 'Country', col_wrap=3, height=2, palette='crest', linewidth=2,errorbar='sd' )
plt.tight_layout()
plt.show()

# 48.                                           LINEPLOT

sns.set_theme(style='whitegrid')
sns.lineplot(data=df_small, palette='tab10', linewidth=2.5)
plt.tight_layout()
plt.show()

# 49.                                           VIOLPLOT

sns.violinplot(data=df_more_small, palette='Set3', bw_adjust=.5, cut=1 , linewidth=1)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()