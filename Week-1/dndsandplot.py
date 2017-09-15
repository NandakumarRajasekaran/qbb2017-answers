#!/usr/bin/env python

"""
Count number of dN and dS, calculate z-scores for each codon and plot thhem

Usage: ./dndsandplot.py <dna-aligned-converted> <protein-aligned>

In this case, ./dndsandplot.py  dna_align.fa mafftprot.fa 
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

fname=sys.argv[1]
gname=sys.argv[2]

df=pd.read_fwf(fname,widths=[3]*4872,index_col=False,header=None)
dfp=pd.read_fwf(gname,widths=[1]*4872,index_col=False,header=None)

arr=df.values
parr=dfp.values
allmut=np.equal(arr,arr[0,:])
#dash=np.equal(arr,'---')          #Uncomment if you want dash as no mutation 
#allmut=np.logical_or(allmut,dash) #If commented, dash is counted as non-synonymous mutation
allmut=np.logical_not(allmut)
protcmp=np.equal(parr,parr[0,:])
syn=np.logical_and(allmut,protcmp)
nonsyn=np.logical_and(allmut,np.logical_not(protcmp))
ind=np.where(parr[0,:]!='-')        #Consider only non-dash indices in query seq i.e. ignore the columns if dash is present in query sequence.
syn_all=syn.sum(axis=0)
syn_all=syn_all[ind]
nonsyn_all=nonsyn.sum(axis=0)
nonsyn_all=nonsyn_all[ind]
diff=syn_all-nonsyn_all
zscore=stats.zscore(diff)
redind=np.where(zscore<=-2.326) # one -tailed , 0.01 p value

plt.figure()
plt.scatter(range(0,len(diff)),stats.zscore(diff))
plt.scatter(redind,zscore[redind],c='red')
plt.title('Z-score vs codon position')
plt.xlabel('Codon position')
plt.ylabel('Z-score')
plt.savefig('Z-score (dash as nonsyn).png')
plt.close()

plt.figure()
plt.scatter(range(0,len(diff)),np.log2((nonsyn_all+0.1)/(syn_all+1))) #To not divide by zero, add 1 to the denominator
plt.scatter(redind,np.log2(nonsyn_all[redind]/(syn_all[redind]+1)),c='red')
plt.title('dNdS Ratio')
plt.xlabel('Codon Position')
plt.ylabel('log2(dN/dS) Ratio')
plt.savefig('dNdS Ratio (dash as nonsyn).png')
plt.close()