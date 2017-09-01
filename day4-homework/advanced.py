#!/usr/bin/env python

"""
Usage: ./advanced.py <ctab-dir> <gene> <samples.csv> <replicates.csv>

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
  #  print df[roi]["FPKM"].values
    
    
#print fpkms_f

soi=df_samples["sex"]=="male"

fpkms_m=[]
#df_gene=pd.DataFrame()

for sample in df_samples["sample"][soi]:
    
    fname=os.path.join(sys.argv[1],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["gene_name"]==gene
    fpkms_m.append(np.mean(df[roi]["FPKM"].values))
    
    
#print fpkms_m

df_rep=pd.read_csv(sys.argv[4]) 
 
fpkms_frep=[None,None,None,None]
soi=df_rep["sex"]=="female"

for sample in df_rep["sample"][soi]:
    
    fname=os.path.join(sys.argv[1],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["gene_name"]==gene
    fpkms_frep.append(np.mean((df[roi]["FPKM"]).values))
print fpkms_frep
fpkms_mrep=[None,None,None,None]
soi=df_rep["sex"]=="male"

for sample in df_rep["sample"][soi]:
    
    fname=os.path.join(sys.argv[1],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["gene_name"]==gene
    fpkms_mrep.append(np.mean((df[roi]["FPKM"]).values))
print fpkms_mrep   
plt.figure()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes',linewidth=3)
x=[0,1,2,3,4,5,6,7]
plt.plot(fpkms_f,c="red",linewidth=2)
plt.plot(fpkms_m,c='blue',linewidth=2)
plt.plot(fpkms_frep,'o',c="red",markersize=10)
plt.plot(fpkms_mrep,'o',c="blue",markersize=10)
plt.title("Sxl",size=20,style='italic',y=1.06)
plt.legend(['female','male','female replicates','male replicates'],bbox_to_anchor=(1.5,0.6),frameon=False,numpoints=1)
plt.axis(linewidth=20,size=20)
#plt.plot(fpkms_frep,'o',c="red")
#plt.plot(fpkms_mrep,'o',c="blue")
plt.xticks(x,["10","11","12","13","14A","14B","14C","14D"],rotation=90)
plt.tick_params(right='off',top='off',direction='out')
plt.xlabel("Developmental stage \n (in days)",size=20)
plt.ylabel("mRNA abundance (FPKM)",size=20)
plt.xlim([-0.5,7.5])
plt.ylim([-0.3,14])
#plt.legend(['female','male'],loc="upper center",frameon=False)
#plt.xticks(x,["10","11","12","13","14A","14B","14C","14D"])
#plt.xlabel("developmental stage")
#plt.ylabel("FPKM")
plt.savefig("genetimecourse.png",bbox_inches='tight')
plt.close
    
