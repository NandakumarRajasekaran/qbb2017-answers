#!/usr/bin/env python

"""
Count kmers in a fasta file
"""

import sys
import fasta

target =open(sys.argv[1])
query=open(sys.argv[2])
k=int(sys.argv[3])


kmer_dict={}
o=open("indextable.txt",'w')


for ident, sequence in fasta.FASTAReader(target):
    sequence=sequence.upper()
    for i in range(0,len(sequence)-k):
        kmer=sequence[i:i+k]
        
        
        if kmer not in kmer_dict:
            kmer_dict[kmer]=[(ident,i)]
        else:
            kmer_dict[kmer].append((ident,i))

#for kmer, count in kmer_dict.iteritems():
#    print kmer, count
    
ident_q,seq_q=fasta.FASTAReader(query).next()
seq_q=seq_q.upper()

for i in range(0,len(seq_q)-k):
    kmer_query=seq_q[i:i+k]
    if kmer_query in kmer_dict:
        kmer_list=kmer_dict[kmer_query]
        for item in kmer_list:
            print item[0],"\t",item[1],"\t",i,"\t",kmer_query

        
            
        