#!/usr/bin/env python

"""
-Create single line DNA and protein sequence based on mafft output
-Insert dashes in DNA sequence
Usage: ./iter_DNDS.py blast_alignment.fa mafft.fa > mafftprot.fa
or, ./iter_DNDS.py blast_alignment.fa mafft.fa > dna_align.fa
"""

import sys
import itertools

f=open(sys.argv[1])
g=open(sys.argv[2])
qseq=''

for dna, prot in itertools.izip(f,g):
    dna=dna.rstrip("\t\n")
    prot=prot.rstrip("\t\n")
    
    if dna[0]=='>':
        continue
    dna_align=''
    dna_pos=0
    for i,c in enumerate(prot):
        if c=='-':
            dna_align=dna_align+'---'
        else:
            dna_align=dna_align+dna[dna_pos:dna_pos+3]
            dna_pos+=3

    print prot          #For protein
    #print dna_align    #For dna