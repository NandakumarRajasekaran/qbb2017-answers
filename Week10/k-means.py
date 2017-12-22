#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy.cluster.hierarchy as clst
import scipy.cluster.vq as vq

df=pd.read_csv(sys.argv[1],sep='\t',index_col=0)
coi=['CFU','poly']
data=df[coi].values
data_new=vq.whiten(data)
codebook,distortion=vq.kmeans(vq.whiten(data),5) #the top cluster in heat map is not very clear. I used approximately 2 or 5 clusters
code,dist=vq.vq(data_new,codebook)
print code
colors=np.asarray(['g','r','y','b','m'])
colorcode=colors[code]
print colorcode
#print codebook
np.save('code.npy',code)



plt.figure()

plt.scatter(data_new[:,0],data_new[:,1],c=np.ndarray.tolist(colorcode))
plt.scatter(codebook[:,0],codebook[:,1],color='k')
plt.savefig('kcluster5.png')
plt.close()
