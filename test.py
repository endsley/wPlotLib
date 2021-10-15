#!/usr/bin/env python

import numpy as np
from sklearn.cluster import SpectralClustering

import wplotlib

#from wplotlib import scatter
#from wplotlib import lines
from wplotlib import heatMap
#from wplotlib import cluster_plot
from wplotlib import histograms




##	Plot cluster example
#n = 100
#x1 = np.random.randn(n,2) + np.array([4,4])
#x2 = np.random.randn(n,2) + np.array([-4,-4])
#X = np.vstack((x1,x2))
#Y = np.concatenate([np.zeros(n), np.ones(n)])
#
#cluster_plot(X, Y, title='Clustering Results')
