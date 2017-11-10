#!/usr/bin/env python 
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.load("Nora_enrichment.out.npz")

ctcf=pd.read_csv("CTCF_Xonly.bed",sep='\t').values
ctcf=ctcf[:,1]
enrichment=data["0.enrichment"]
#print ctcf

forward=data["0.forward"]
reverse=data["0.reverse"]
f_index=[]
r_index=[]
for i,frag in enumerate(forward):
    for j,pos in enumerate(ctcf):
        if frag[0]<=pos and frag[1]>=pos:
            f_index.append(i)

f_index=list(set(f_index))
f_index.sort()
#print f_index
            
for i,frag in enumerate(reverse):
    for j,pos in enumerate(ctcf):
        if frag[0]<=pos and frag[1]>=pos:
            r_index.append(i)
r_index=(list(set(r_index)))
r_index.sort()
#print type(data)
#print r_index
#print enrichment.shape

#print forward.shape
#print reverse.shape          
ctcf_enrich=enrichment[f_index,:][:,r_index]

print ctcf_enrich

max_row=list(np.argmax(ctcf_enrich,axis=1))
max_col=list(np.argmax(ctcf_enrich,axis=0))
max_rowval=np.amax(ctcf_enrich,axis=1)
max_colval=np.amax(ctcf_enrich,axis=0)
#print forward[1,:]
#print reverse[1,:]
#print type(max_col)
#print max_rowval    
#print max_row

print 'CTCF forward primers are' 
print  f_index
print 'They strongly interact with corresponding reverse primers:' 
print [r_index[i] for i in max_row]
print '\n\n'
print 'CTCF reverse primers are' 
print r_index
print 'They strongly interact with corresponding forward primers:' 
print [f_index[i] for i in max_col]
#print forward[f_index[i] for i in max_row,:]
#print forward[f_index[max_col],:]

#fname=open('Nora_primers.bed')
fctcf_primers=forward[f_index,:]
#fctcf_primers=forward[[f_index[i] for i in max_col],:]
#rctcf_primers=reverse[[r_index[i] for i in max_row],:]
rctcf_primers=reverse[r_index,:]
#print rctcf_primers
#print fctcf_primers
#print fctcf_primers[np.where(fctcf_primers[:,0]==99253548),:]
#fctcf_names=[0]*len(f_index)
#rctcf_names=[0]*len(r_index)
fctcf_names=[]
rctcf_names=[]
'''dfprimer=pd.read_csv('Nora_primers.bed',sep='\t')
coi=['start','name']
dfprimer=dfprimer[coi]
merged=
'''
fname=open('Nora_Primers.bed')
for line in fname:
    if line.startswith('#'):
        continue
    l=line.split()
    if int(l[1]) in fctcf_primers[:,0]:
        #print int(np.where(fctcf_primers[:,0]==int(l[1])))
        #fctcf_names[list(np.where(fctcf_primers[:,0]==int(l[1])))]=l[3]
        fctcf_names.append(l[3])
    if int(l[1]) in rctcf_primers[:,0]:
        rctcf_names.append(l[3])
        

#print fctcf_names
#print rctcf_names
print '\n\n'
print 'CTCF forward primers are' 
print  fctcf_names
print 'They strongly interact with corresponding reverse primers:' 
print [rctcf_names[i] for i in max_row]
print '\n\n'
print 'CTCF reverse primers are' 
print rctcf_names
print 'They strongly interact with corresponding forward primers:' 
print [fctcf_names[i] for i in max_col]
        
       
 

plt.figure()
plt.pcolor(ctcf_enrich,cmap='hot')
plt.xlabel(r_index)
plt.ylabel(f_index)
plt.savefig('heatmap.png')
plt.close()