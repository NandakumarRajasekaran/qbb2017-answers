#!/usr/bin/env python
"""
Convert mafft output to single line sequence format
Usage: ./FASTAParser.py  mafft_prot.out  mafft.fa
"""
import sys
import fasta
f=open(sys.argv[1])
o=open(sys.argv[2],'w')

for ident,sequence in fasta.FASTAReader(f):
    o.write('%s\n%s\n'%(ident,sequence))
    

