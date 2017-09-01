#!/usr/bin/env python
 
"""
usage: question2.py <ctab-file> 
"""

import sys
import pandas as pd

df=pd.read_csv(sys.argv[1],sep="\t")

roi=df["strand"]=="+"

#df_gene_plus=pd.DataFrame()
coi=["chr","start","t_name"]


df_gene_plus=df[coi][roi]
#df_gene_plus.rename(columns[1]="promend")
df_gene_plus["out_start"]=df_gene_plus["start"]-500
df_gene_plus["out_end"]=df_gene_plus["start"]+500


#roi=df["out_start"]<0
#df[roi]["out_start"]=1

#df_gene_plus["out_start"]=df_gene_plus[df_gene_plus["out_start"]<0]["out_start"]
df_gene_plus["out_start"][df_gene_plus["out_start"]<0]=1
#pcol=["chr","out_start","out_end","t_name"]



roi=df["strand"]=="-"
coi=["chr","end","t_name"]
df_gene_minus=df[coi][roi]
#df_gene_plus.rename(columns[1]="promend")
df_gene_minus["promstart"]=df_gene_minus["end"]-500

df_gene_minus["out_end"]=df_gene_minus["end"]+500
df_gene_minus["out_start"]=df_gene_minus["end"]-500
df_gene_minus["out_start"][df_gene_minus["out_start"]<0]=1
#print df_gene_minus

cp=["chr","out_start","out_end","t_name"]
cm=["chr","out_start","out_end","t_name"]
frames=[df_gene_plus[cp],df_gene_minus[cm]]
result=pd.concat(frames)

result.to_csv("data.bed",sep="\t",header=None,index=False)