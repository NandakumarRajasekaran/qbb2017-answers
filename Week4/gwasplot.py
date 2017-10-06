#!/usr/bin/env python
"""
usage:
"""
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fname=sys.argv[1]
oname=sys.argv[2]
phenNo=int(sys.argv[3])

prestr=fname+'.P'
poststr='.assoc.linear'
for i in range (1,phenNo+1):
    filename=prestr+str(i)+poststr
    df=pd.read_csv(filename,delim_whitespace=True)
    print df.columns
    coi=['P']
    Pval=df[coi].values
    plt.figure()
    a,b=df.shape
    plt.scatter(range(1,a+1),-np.log10(Pval))
    plt.xlabel('Variant Number')
    plt.ylabel(r'$-log_{10} (P)$')
    plt.savefig(oname+'.'+str(i)+'.manhat.png')
    plt.close()
