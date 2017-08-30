#!/usr/bin/env python

import sys

count=0
mapq=0

for line in open(sys.argv[1]):
    if line.startswith("@"):
        continue
    cols=line.split()
    if cols[2]=="2L" and int(cols[3])<20000 and int(cols[3])>10000:
        count+=1
    
print count
    

        
    
    
    
        


