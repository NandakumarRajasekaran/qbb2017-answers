#!/usr/bin/env python

import sys

f=open(sys.argv[1])
count =0

for line in f:
    if line.startswith("@"):
        continue
    cols=line.split("\t")
    flag=(int(cols[1]))
    
    mask=16
    if mask & flag >0:
        count+=1
    
    
print count
    
   
    