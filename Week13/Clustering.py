#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy.cluster.hierarchy as clst
import scipy.cluster.vq as kmeans

df=pd.read_csv(sys.argv[1],sep='\t',index_col=0)

linkage_rows=clst.linkage(df.values)
leaves_rows=clst.leaves_list(linkage_rows)
print leaves_rows
linkage_cols=clst.linkage(pd.DataFrame.transpose(df).values)
leaves_cols=clst.leaves_list(linkage_cols)
print leaves_cols

X=df.values
X=X[leaves_rows,:][:,leaves_cols]
plt.figure()
#labels=df.rows
#labels=leaves_cols
stagenames=list(df)
print stagenames
labels=[]
for i in leaves_cols:
    labels.append(stagenames[i])

stagenames1=df.index
print stagenames1
labels1=[]
for i in leaves_rows:
    labels1.append(stagenames1[i])
#labels=labels[leaves_cols]
m = np.max(np.abs(X))
mini=np.min(np.abs(X))
plt.title("Heatmap of Gene Expression") # Add a title to the top
plt.imshow(                                  # Treat the values like pixel intensities in a picture
	X,                                       # ... Using X as the values
	aspect='auto',                           # ... 'Stretch' the image to fit the canvas, so you don't get a skinny strip that is 4x150 pixels
	interpolation='nearest',                 # ... Don't use any blending between pixel values
	cmap="cool",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
	vmin=mini,                               # ... Set the lowest value to show on the scale
	vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
	)
plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
plt.xticks(            # Edit the xticks being shown
	range(X.shape[1]), # ... use the values centered on each column of pixels
	labels,            # ... which corresponds to the indices of our labels
	rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
	)
plt.yticks(            # Edit the xticks being shown
	range(X.shape[0]), # ... use the values centered on each column of pixels
	labels1,            # ... which corresponds to the indices of our labels
	rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
	)
#plt.yticks([])         # Edit the ticks on the y-axis to show....NOTHING
plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values
#clst.dendrogram(linkage_cols,no_plot=False)
plt.tight_layout()
plt.savefig("clean_heatmap.png") # Save the image
plt.tight_layout()
plt.close() # Close the canvas 

plt.figure()
clst.dendrogram(linkage_cols)
plt.savefig('dendro.png',box='tight')

plt.close()



