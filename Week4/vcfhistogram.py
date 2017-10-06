#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

f=open(sys.argv[1])

allele_freq=[]
for line in f:
    if line.startswith("#"):
        continue
    line=line.rstrip("\t\n").split()
    
    af=line[7].split(";")
    
    af1=af[0][3:]
    if "," in af1:
        af1=af1.split(",")
        for i in af1:
            allele_freq.append(float(i))
    else:
        allele_freq.append(float(af1))
    
plt.figure()
plt.hist(allele_freq,bins=20)
plt.savefig(sys.argv[2])    
plt.close()    
    