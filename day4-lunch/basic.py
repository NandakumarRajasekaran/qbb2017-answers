#!/usr/bin/env python


"""
usage: ./basic.py <file1.ctab> <file2.ctab> 
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1= pd.read_csv(sys.argv[1],sep="\t")
df2= pd.read_csv(sys.argv[2],sep="\t")

#FPKM1=df1.set_index('t_name')['FPKM'].to_dict()
coi=["t_name","FPKM"]
df1=df1[coi]
df2=df2[coi]
#file2_FPKM=df2[coi]

df3=pd.merge(df1,df2,on=["t_name"],how="inner")
roi=df3!=0 
#=df3["FPKM_y"]!=0
#roi=roi1 and roi2
df3=df3[~(df3==0).any(axis=1)]
#print df3.head()
df3["FPKM_x"]=np.log(df3["FPKM_x"])
df3["FPKM_y"]=np.log(df3["FPKM_y"])

plt.figure()
plt.scatter(df3["FPKM_x"],df3["FPKM_y"],alpha=0.3,s=10)
plt.title("FPKM Comparison of \n 893 and 915",alpha=0.3)
plt.legend(loc='upper left')
plt.xlabel("893 FPKM")
plt.ylabel("915 FPKM")

fit = np.polyfit(x=df3["FPKM_x"],y=df3["FPKM_y"],deg=1)
plt.plot(df3["FPKM_x"],fit[0]*df3["FPKM_x"]+fit[1],'-')
print fit
plt.savefig(sys.argv[3])
plt.close()

#print FPKM1


