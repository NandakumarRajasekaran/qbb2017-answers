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
 
fpkms_frep=[None,None,None,None]
soi=df_rep["sex"]=="female"

for sample in df_rep["sample"][soi]:
    
    fname=os.path.join(sys.argv[2],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["t_name"]==transcript
    fpkms_frep.append((df[roi]["FPKM"]).values)

fpkms_mrep=[None,None,None,None]
soi=df_rep["sex"]=="male"

for sample in df_rep["sample"][soi]:
    
    fname=os.path.join(sys.argv[2],sample,"t_data.ctab")
    df = pd.read_csv(fname,sep="\t")
    roi=df["t_name"]==transcript
    fpkms_mrep.append((df[roi]["FPKM"]).values)



plt.figure()
x=[0,1,2,3,4,5,6,7]
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes',linewidth=3)
plt.plot(fpkms,c="red",linewidth=2)
plt.plot(fpkms_male,c='blue',linewidth=2)
plt.plot(fpkms_frep,'o',c="red",markersize=10)
plt.plot(fpkms_mrep,'o',c="blue",markersize=10)
plt.title("FBtr0331261",size=20,style='italic',y=1.06)
plt.legend(['female','male','female replicates','male replicates'],bbox_to_anchor=(1.5,0.6),frameon=False,numpoints=1)
plt.axis(linewidth=20,size=20)
plt.xticks(x,["10","11","12","13","14A","14B","14C","14D"],rotation=90)
plt.tick_params(right='off',top='off',direction='out')
plt.xlabel("Developmental stage \n (in days)",size=20)
plt.ylabel("Transcript abundance (FPKM)",size=20)
plt.xlim([-0.5,7.5])
plt.ylim([-3,200])
plt.savefig("timecourse.png",bbox_inches='tight')
plt.close