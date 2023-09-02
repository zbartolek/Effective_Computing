#makes bubble plot of 16S data from G1_Rank5_3_latRX_top10_Chl.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importing data:
table = pd.read_csv (r'/Users/zinkabartolek/Desktop/CLASSES/Effective Computing /data/G1_Rank5_3_latRX_top10_Chl.csv')
print(table)

#normalizing data:
La = table['Lat']
Ch = table['Chl']

df = table
del df ["Lat"]
del df ["Chl"]

df = df.div(df.sum(axis=1),axis=0) #normalizing by row, so that sum of each row is 1
df = df *100 #muptiplying by 100 to get bigger numbers

df.insert(0,'Lat', La)
df.insert(1,'Chl', Ch)

#converting data table to long format:
df = pd.melt(df, id_vars=['Lat', 'Chl'], var_name='Taxonomy', value_name = 'Values')
print(df)

#plotting bubble plot:
plt.close('all') # always start by cleaning up

df.sort_values(by=['Lat'], inplace=True)
size = df ["Values"]


sc = plt.scatter('Lat', 'Taxonomy', s=size*30, c= 'Chl', alpha = 0.8, data=df, cmap = 'Greens', edgecolors='grey')
plt.xlabel("Latitude", size=12, fontweight='bold')
plt.xticks(rotation=90)
plt.ylabel("Taxa at Family Level", size=12, fontweight='bold')
plt.title("Bacterial abundance across transition zone", size=14, fontweight='bold')

#legends:
legend1 = plt.legend(*sc.legend_elements("sizes", num=5), labelspacing = 3, title='Relative Abundance', bbox_to_anchor=(1.35,1.0), frameon=False)
ax = plt.gca().add_artist(legend1)
#legend2 = plt.legend(*sc.legend_elements("colors", num=3), title='Chl (mg/L)', bbox_to_anchor=(1.1,0.5), frameon=False)

cbar = plt.colorbar()
cbar.ax.set_xlabel( 'Chl (mg/L)', rotation=0)

plt.show()
