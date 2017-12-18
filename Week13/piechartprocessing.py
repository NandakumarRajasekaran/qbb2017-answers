#!/usr/bin/env  python

import sys
import os

fname=open(sys.argv[1])
dict1={}
for line in fname:
    temp1=line.rstrip("\r\n").split("\t")
    temp2=temp1[1]
    temp2=temp2.replace(";","\t")
    if temp2 not in dict1:
        dict1[temp2]=1
        
    else:
        dict1[temp2]+=1
        
print  len(dict1.keys())     
for key,value in dict1.iteritems():
    print str(value)+"\t"+str(key)+"\n"
    
    
    
    
    