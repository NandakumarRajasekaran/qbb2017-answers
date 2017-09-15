#!/usr/bin/env python
"""
Convert tsv to fasta"""
import sys
import re
f=open(sys.argv[1])
o=open(sys.argv[2],'w')

for line in f:
    fields=line.split()
    o.write(">%s\n"%(fields[0]))
    line1=fields[1].replace('-','')
    o.write("%s\n"%(line1))
    
    
f.close()
o.close()
    