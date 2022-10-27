#!/usr/bin/env python

import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from wplotlib import plot_clusters

#	Plot cluster example
n = 100
x1 = np.random.randn(n,2) + np.array([4,4])
x2 = np.random.randn(n,2) + np.array([-4,-4])
X = np.vstack((x1,x2))
Y = np.concatenate([np.zeros(n), np.ones(n)])

plot_clusters(X, Y, title='Clustering Results')
