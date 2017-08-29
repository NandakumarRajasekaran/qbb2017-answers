#!/usr/bin/env python

"""
Syntax: ./question2.py <ctab-file> <mapping-file> {0 | randomstring}
0 for ignoring the line
randomstring will be appended if given
If there is no third argument 0 is default 
"""
import sys

ctab_file=open(sys.argv[1])

map_file=open(sys.argv[2])
o=open('ctab_uniprot_map.txt','w')
ctab_map={}

#Create a dictionary with FB as key and AC as value
for line in map_file:
    #print line
    fields=line.rstrip("\t\n").split("\t")
   # print fields[0]
    #print fields
    ctab_map[fields[0]]=fields[1]
    

count=0   
for line in ctab_file:
    if line.startswith("t_id"):
        continue;
    fields=line.rstrip("\t\n").split("\t")
    count+=1
    
    if fields[8] in ctab_map:
        newline=line+str((ctab_map[fields[8]]))
        
        
    else:
        if sys.argv[3]!='0':
            newline=line+str(sys.argv[3])
        elif sys.argv[3]=='0':
            continue
        else:
            continue
    
    o.write(newline+"\n")
    
    
ctab_file.close()
map_file.close()
o.close()
            
    
    

