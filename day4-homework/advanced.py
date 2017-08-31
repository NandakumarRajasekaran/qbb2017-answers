#!/usr/bin/env python

"""
Usage: ./advanced.py <ctab-dir> <gene> <samples.csv>

"""

import sys
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

gene=sys.argv[2]

df_samples=pd.read_csv(sys.argv[3])



soi=df_samples["sex"]=="female"

fpkms_f=[]
#df_gene=pd.DataFrame()

for sample in df_samples["sample"][soi]:
    
    fname=os.path.join(sys.argv[1],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["gene_name"]==gene
    fpkms_f.append(np.mean(df[roi]["FPKM"].values))
    print df[roi]["FPKM"].values
    
    
print fpkms_f

soi=df_samples["sex"]=="male"

fpkms_m=[]
#df_gene=pd.DataFrame()

for sample in df_samples["sample"][soi]:
    
    fname=os.path.join(sys.argv[1],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["gene_name"]==gene
    fpkms_m.append(np.mean(df[roi]["FPKM"].values))
    
    
print fpkms_m
    
plt.figure()
x=[0,1,2,3,4,5,6,7]
plt.plot(fpkms_f,c="red",linewidth=2)
plt.plot(fpkms_m,c='blue',linewidth=2)
#plt.plot(fpkms_frep,'o',c="red")
#plt.plot(fpkms_mrep,'o',c="blue")
plt.legend(['female','male'],loc="upper center",frameon=False)
plt.xticks(x,["10","11","12","13","14A","14B","14C","14D"])
plt.xlabel("developmental stage")
plt.ylabel("FPKM")
plt.savefig("genetimecourse.png")
plt.close
    
