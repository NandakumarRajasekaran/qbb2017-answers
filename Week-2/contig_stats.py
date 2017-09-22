#!/usr/bin/env python
"""
Get stats about contigs like min,max,avg, N50.

usage: ./contig_stats.py <contigs.fa>
"""


import sys
import fasta
#import pandas as pd
import numpy as np

f=open(sys.argv[1])

lencontig=[]
for ident,sequence in fasta.FASTAReader(f):
    length=len(sequence)
    lencontig.append(length)
    
lencontig.sort()
print "total contigs is", len(lencontig)
print "mean is", np.mean(lencontig)
print "max is", max(lencontig)
print "min is", min(lencontig)
print "median is", np.median(lencontig)

totl=sum(lencontig)
l=0
i=0
while l<totl/2:
    l=l+lencontig[i]
    i+=1

N50=lencontig[i-1]
print "N50 is", N50


    