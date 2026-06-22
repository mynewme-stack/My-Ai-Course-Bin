import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datasets/FastFoodRestaurants.csv', delimiter=',')
df = df.fillna('N/A')
print(df)

# 25.                                DISPLOT

sns.displot(data= df, x = 'longitude', hue= 'country', kind='ecdf', aspect=1.2, palette='Spectral')
plt.show()

# 26.                                 LMPLOT

df_better = df.query('`longitude` < 15.00 and `latitude` < 20.00')
sns.lmplot(data=df_better,
           x= 'longitude',
           y= 'latitude',
           hue= 'country',
           col='country',
           scatter_kws={'s': 15, 'alpha': 0.6},
           palette='Set1')
plt.show()

# 27.                                 PAIRGRID

cols = ['longitude','latitude']
my = sns.PairGrid(df, vars=cols,hue='country',palette='Set2')
my.map_offdiag(sns.scatterplot,s=20,alpha = 0.6)
my.map_diag(sns.kdeplot, fill= True,alpha=0.4)
my.add_legend()
plt.show()

# 28.                                PAIRGRID

sns.catplot(
    data=df_better,
    x="name", y="longitude",
    kind="point", join=True
)

plt.show()

# 29.                                PAIRGRID

col = ['city', 'country','province']
df_small = df.sample(20, random_state=1)
a = sns.PairGrid(df_small, x_vars= col, y_vars=['longitude'], height=4,aspect=0.7)
a.map(sns.stripplot, orient= 'h', size= 4, color= 'blue', jitter=True)
plt.show()

# 30.                                   BARPLOT

fig, axes = plt.subplots(1,2,figsize = (12,4))
df_few = df.sample(20, random_state=1)
sns.set_theme(style='ticks', rc= {'axes.facecolor':'white', 'grid.color': 'grey'})
sns.barplot(data=df_few, x = 'city', y= 'longitude',ax=axes[0])
plt.tight_layout()
plt.show()                
input('Enter Spacebar for Further Execution:')

# 31.                                   KDEPLOT

for c in cols:
    if c != 'latitude':
                sns.kdeplot(data = df_few,
                x = c, y = 'latitude',
                fill='True',
                cmap= 'Blues')
    plt.title(f'{c} VS Longitude')
    plt.show()

# 32.                                   BARPLOT

df_few = df.sample(10, random_state=1)
sns.kdeplot(data=df_better, x="longitude", y="latitude", fill=True, cmap="Blues")
plt.title("Longitude vs Latitude")
plt.show()

sns.barplot(data=df_few, x="city", y="longitude", hue="country", palette="Blues")
plt.title("City vs Longitude (Grouped by Country)")
plt.tight_layout()
plt.show()

# 33.                                   CATPLOT

df_small = df.sample(10, random_state=1)
sns.catplot(
        data=df_small,
        x='province',
        y= 'latitude',hue='country',
        kind='point',join = True, 
        palette='Set2', height=5, aspect=1.2
)
plt.tight_layout()
plt.show()

# 34.                                   FACETGRID
df_now =  df.query('`longitude` < 50.00 and `latitude` < 50.00')
g =sns.FacetGrid(data= df_now, col= 'name', col_wrap=3,
              subplot_kws=dict(projection= 'polar'), despine=False)
g.map(sns.scatterplot, 'longitude', 'latitude')
plt.tight_layout()
plt.show()

# 35.                                 JOINPLOT

t = sns.jointplot(x= 'longitude', y= 'latitude', data= df_better,kind='reg', truncate= False,xlim=(0, 60), ylim=(0,12),color = 'm', height=7)
plt.tight_layout()
plt.show()

# 36.                                RESIDPLOT

sns.residplot(data= df_few,x= 'latitude', y= 'longitude', color= "m")
plt.show()