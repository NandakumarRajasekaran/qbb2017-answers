#!/usr/bin/env python

"""
Find kmer matches in target and extend them for exact matches

usage: ./kmer_matcher.extender.py <target> <query> k
"""

import sys
import fasta
from operator import itemgetter
target =open(sys.argv[1])
query=open(sys.argv[2])
k=int(sys.argv[3])
o=open("extend.output",'w')

kmer_dict={}
#o=open("indextable.txt",'w')
targetseq={}

for ident, sequence in fasta.FASTAReader(target):
    
    sequence=sequence.upper()
    targetseq[ident]=sequence
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
qlen=len(seq_q)
output={}
for i in range(0,len(seq_q)-k):
    kmer_query=seq_q[i:i+k]
    if kmer_query in kmer_dict:
        kmer_list=kmer_dict[kmer_query]
        for item in kmer_list:
            targetseqid=item[0]
            targetpos=item[1]
            tarlen=len(targetseq)
            x=1
            y=1
            while True:
                if targetpos-x>=0 and i-x>=0 and targetseq[targetseqid][targetpos-y]==seq_q[i-x]:
                    kmer_query=seq_q[i-x]+kmer_query
                    x+=1
                else:
                    break
            while True:
                if targetpos+k-1+y<tarlen and i+k-1+y<qlen and targetseq[targetseqid][targetpos+k-1+y]==seq_q[i+k-1+y]:
                    kmer_query=kmer_query+seq_q[i+k-1+y]
                    y+=1
                else:
                    break
                
        
            #Sorting the output
            if item[0] not in output:
                
                output[item[0]]=[(item[1]-x+1,i-x+1,kmer_query)]
                
            else:
                output[item[0]].append((item[1]-x+1,i-x+1,kmer_query))

#Sorting the output
                
#print output
keylist=list(output.keys())
keylist=sorted(keylist,key=lambda x: float(x[5:]) ) 
print keylist    
   
#for key,value in output.iteritems():
 #   outlist=sorted(value,key=(itemgetter(2)))
    #for item in outlist:
       # print key,"\t",item[0],"\t",item[1],"\t",item[2]
        
for key in keylist:
    outlist=sorted(output[key],key=itemgetter(2))
    for item in outlist:
        #print key, item[2]
        o.write("%s \t %s \t %s \t %s \n" % (key,item[0],item[1],item[2]))
             
             
o.close()
target.close()
query.close()

        
            
        