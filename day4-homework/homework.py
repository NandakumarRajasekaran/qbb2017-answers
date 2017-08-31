#!/usr/bin/env python
"""
usage: ./01-timecourse.py <samples.csv> <ctab-dir> <replicates.csv> 

-Plot timecourse of FBtr0331261 for females
"""



import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

transcript="FBtr0331261"

df_samples=pd.read_csv(sys.argv[1])

soi=df_samples["sex"]=="female"

fpkms=[]

for sample in df_samples["sample"][soi]:
    
    fname=os.path.join(sys.argv[2],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["t_name"]==transcript
    fpkms.append((df[roi]["FPKM"]).values)

#print fpkms

soi=df_samples["sex"]=="male"
fpkms_male=[]

for sample in df_samples["sample"][soi]:
    
    fname=os.path.join(sys.argv[2],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["t_name"]==transcript
    fpkms_male.append((df[roi]["FPKM"]).values)
df_rep=pd.read_csv(sys.argv[3]) 
 
fpkms_frep=[0,0,0,0]
soi=df_rep["sex"]=="female"

for sample in df_rep["sample"][soi]:
    
    fname=os.path.join(sys.argv[2],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["t_name"]==transcript
    fpkms_frep.append((df[roi]["FPKM"]).values)

fpkms_mrep=[0,0,0,0]
soi=df_rep["sex"]=="male"

for sample in df_rep["sample"][soi]:
    
    fname=os.path.join(sys.argv[2],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["t_name"]==transcript
    fpkms_mrep.append((df[roi]["FPKM"]).values)



plt.figure()
x=[0,1,2,3,4,5,6,7]
plt.plot(fpkms,c="red",linewidth=2)
plt.plot(fpkms_male,c='blue',linewidth=2)
plt.plot(fpkms_frep,'o',c="red")
plt.plot(fpkms_mrep,'o',c="blue")
plt.legend(['female','male'],loc="upper center",frameon=False)
plt.xticks(x,["10","11","12","13","14A","14B","14C","14D"])
plt.xlabel("developmental stage")
plt.ylabel("FPKM")
plt.savefig("timecourse.png")
plt.close