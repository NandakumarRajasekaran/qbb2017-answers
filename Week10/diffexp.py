#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy.cluster.hierarchy as clst
import scipy.cluster.vq as vq
import scipy.stats as ss
df=pd.read_csv(sys.argv[1],sep='\t',index_col=0)
data=df.values
data=vq.whiten(data)
ttest_sig=[]
for i,val in  enumerate(data):
    a=ss.ttest_rel([val[0],val[1]],[val[4],val[5]])
    ttest_sig.append(a[1])  #p-values of ttest

ttest_sig=np.array(list(ttest_sig))
print '\nPvalues, up/down regulated genes, maximum upregulated gene, its cluster genes:\n\n'
print 'P-values from ttest:'
print ttest_sig
ratio=data[:,5]/data[:,0]  

index_up=np.where((ratio>0) & (ttest_sig<0.05))
print '\nupregulated genes are:'
print df.index[index_up].astype(str).values
index_down=np.where((ratio<0.5) & (ttest_sig<0.05))
print '\n downregulated genes are'
print df.index[index_down].astype(str).values
index_max=np.where(ratio==np.max(ratio[index_up]))
print '\n most upregulated gene is '
print df.index[index_max].astype(str).values


#finding the genes belonging to same cluster as max gene
code=np.load('code.npy') #contains cluster labels 
cluster_id=code[index_max]
genes=np.where(code==cluster_id)
print '\n genes belonging to the max gene cluster are:'
print df.index[genes].astype(str).values

