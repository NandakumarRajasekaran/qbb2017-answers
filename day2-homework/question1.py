#!/usr/bin/env python

import sys

f=open(sys.argv[1])
o=open('index_gene.txt','w')
count=0
for line in f:
    line=line.rstrip("\n\r")
    if "DROME" in line and "FB" in line:
        count+=1
        #The lines are in a specific format. Columns 41 to 46 correspond to AC no and 
        #columns 53 to 63 are FB numbers
        o.write("%s\t %s\n"%(line[40:46:1],line[52:63:1]))
    
f.close()
o.close()
        