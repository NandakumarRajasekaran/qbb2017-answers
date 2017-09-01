#!/usr/bin/env python
 
"""
usage: question2.py <ctab-file> <file1> <file2> <file3> <file4>
""" 
import os
import sys
import numpy as np
import statsmodels.api as sm
import pandas as pd
from statsmodels.sandbox.regression.predstd import wls_prediction_std


#df=pd.DataFrame()
colno=5
df1=pd.read_csv(sys.argv[2],header=None,sep="\t").values
df1=list(map(float,df1[:,colno]))
#print df1
df2=pd.read_csv(sys.argv[3],header=None,sep="\t").values
df2=list(map(float,df2[:,colno]))
df3=pd.read_csv(sys.argv[4],header=None,sep="\t").values
df3=list(map(float,df3[:,colno]))
df4=pd.read_csv(sys.argv[5],header=None,sep="\t").values
df4=list(map(float,df4[:,colno]))

df=pd.read_csv(sys.argv[1],header=None,sep="\t")

df=df.values
df=df[1:,11]
df=np.asarray(list(map(float,df)))

df5=np.column_stack((df1,df2,df3,df4))

#print df5

df5=sm.add_constant(df5)
#print df5
#df=df[1:,11]
#print len(df)

#print df5
print type(df)

print df.shape
print type(df5)
print df5.shape

model=sm.OLS(df,df5)
results=model.fit()
print(results.summary())

#print df1





