#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(sys.argv[1],sep="\t")

df.sort_values(['#zstart1'])
df['size2']=df['size2'].cumsum()-df['size2'][0] #cumulative size of seq as start point in plot 
df['zstart2']=df['zstart2']+df['size2']
df['end2']=df['end2']+df['size2']
a,b=df.shape
print a, b
plt.figure()
coi1=["#zstart1","end1"]
coi2=['zstart2','end2']
print df.loc[0:2,coi1].values
for i in range(0,a):
   # print df[coi1][i]
    #print df.loc[i,coi1].values
    #print df.loc[i,coi2].values
    plt.plot(df.loc[i,coi1].values,df.loc[i,coi2].values)
    

plt.savefig(sys.argv[2])
plt.close()


