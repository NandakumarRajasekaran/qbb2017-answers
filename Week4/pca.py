#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv(sys.argv[1],delim_whitespace=True)
plt.figure()
plt.scatter(df.values[:,2],df.values[:,3])
plt.savefig('pca.png')
plt.close()

