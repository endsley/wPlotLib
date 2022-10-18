#!/usr/bin/env python
import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from wplotlib import heatMap
from sklearn.cluster import SpectralClustering

#	Heat Map ticker
K = np.array([[0.7, 0.7, 0, 0],[0.5,0.5,0,0],[0,0,0.4, 0.8], [0,0,0.4, 0.8]])
hMap = heatMap(K, title='Heat Map', xtick_locations=[0.5, 1.5, 2.5, 3.5], xtick_labels=['A', 'B', 'C','D'],
					ytick_locations=[0.5, 1.5, 2.5, 3.5], ytick_labels=['A', 'B', 'C','D'])

#	Heat Map Example
X1 = np.random.randn(100,2)
X2 = np.random.randn(100,2) + 5
X = np.vstack((X1,X2))
np.random.shuffle(X)		# randomly shuffle the rows of X

clf = SpectralClustering(n_clusters=2)
allocation = clf.fit_predict(X)
kernel = clf.affinity_matrix_
axis_label = range(kernel.shape[0])

hM = heatMap(kernel, title='Drawing Unsorted Heat Map', sort_kernel_based_on_label=False, subplot=121, figsize=(10,5))
heatMap(kernel, title='Samples of Same Labels sorted together', sort_kernel_based_on_label=True, label=allocation, subplot=122)
hM.show()



