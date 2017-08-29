#!/usr/bin/env python

# Opening file with open
import sys
#f= open("/Users/cmdb/data/genomes/BDGP6.fa")
if len(sys.argv>1):
    
    f=open(sys.argv[1])
    firstline=f.readline()
    

#STDIN open
else:
    firstline=sys.stdin.readline()
print firstline