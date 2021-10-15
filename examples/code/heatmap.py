#!/usr/bin/env python

import numpy as np
from wplotlib import heatMap
from sklearn.cluster import SpectralClustering

#	Heat Map ticker
K = np.array([[0.7, 0.7, 0, 0],[0.5,0.5,0,0],[0,0,0.4, 0.8], [0,0,0.4, 0.8]])
hMap = heatMap()
hMap.draw_HeatMap(K, title='Heat Map', xtick_locations=[0.5, 1.5, 2.5, 3.5], xtick_labels=['A', 'B', 'C','D'],
					ytick_locations=[0.5, 1.5, 2.5, 3.5], ytick_labels=['A', 'B', 'C','D'])


#	Heat Map Example
X1 = np.random.randn(100,2)
X2 = np.random.randn(100,2) + 5
X = np.vstack((X1,X2))

Y1 = np.ones(100)
Y2 = np.zeros(100)
Y = np.hstack((Y1,Y2))

clf = SpectralClustering(n_clusters=2)
allocation = clf.fit_predict(X)
kernel = clf.affinity_matrix_
axis_label = range(kernel.shape[0])
hMap = heatMap()
sorted_kernel = hMap.sort_kernel(kernel, allocation)

hMap.draw_HeatMap(kernel, title='Drawing Unsorted Heat Map', subplot=121)
hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map')



