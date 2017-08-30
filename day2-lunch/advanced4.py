#!/usr/bin/env python

import sys
import re
f=open(sys.argv[1])

count=0
insertion={'1':0,'2':0,'3':0,'4':0,'more':0}
deletion={'1':0,'2':0,'3':0,'4':0,'more':0}
for line in f:
    if line.startswith("@"):
        continue
    
    fields=line.rstrip("\r\n").split("\t")
    if '*' in fields[5]:
        continue
    
    cigarlist=re.split('(\d+)',fields[5])
    
    
    if 'I' in cigarlist:
        #print cigarlist
        ind=cigarlist.index('I')
       # print ind, ind-1
        if int(cigarlist[ind-1])==1:
            insertion['1']+=1
        elif int(cigarlist[ind-1])==2:
            insertion['2']+=1
        elif int(cigarlist[ind-1])==3:
            insertion['3']+=1
        elif int(cigarlist[ind-1])==4:
            insertion['4']+=1
        else:
            insertion['more']+=1
    if 'D' in cigarlist:
        #print cigarlist
        
        ind=cigarlist.index('D')
        #print ind,ind-1
        if int(cigarlist[ind-1])==1:
            deletion['1']+=1
        elif int(cigarlist[ind-1])==2:
            deletion['2']+=1
        elif int(cigarlist[ind-1])==3:
            deletion['3']+=1
        elif int(cigarlist[ind-1])==4:
            deletion['4']+=1
        else:
            deletion['more']+=1
        
        
    
    
    
    
print "insertion:"
print insertion
print "deletion:"
print deletion