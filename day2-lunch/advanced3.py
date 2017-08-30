#!/usr/bin/env python

import sys
import numpy as np

f=open(sys.argv[1])
count=0
number=0
for line in f:
    
    if line.startswith("@"):
        continue
    fields=line.split("\t")
    
    quality=[ord(x)-33 for x in list(fields[10])]
    
    
    if np.mean(quality)>30:
        number+=1
        #print np.mean(quality)
        
    
print number