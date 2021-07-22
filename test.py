#!/usr/bin/env python

import numpy as np
from sklearn.cluster import SpectralClustering

from wplotlib import lines
from wplotlib import heatMap
from wplotlib import cluster_plot


##	Line Plot Example
#textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
#x = np.linspace(0, 10, 1000)
#y = np.sin(x)
#
#lp = lines(figsize=(10,5))		# (width, height)
#lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)


##	Multiple Line subPlot Example
textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0.1, 10, 1000)
y = np.sin(x)
y2 = np.log(x)

lp = lines(figsize=(10,5))
lp.plot_line(x, y, 'First Plot', 'X axis', 'Y axis', imgText=textstr, subplot=121, xlim=[0,3])
lp.plot_line(x, y2, '2nd Plot', 'X axis', 'Y axis', imgText=textstr, subplot=122)
lp.show(save_path='twoSubplots.png') # when making subplots, you have to call show explicitly after all the plots, if you include path, then it will save instead of show



##	Heat Map Example
#X1 = np.random.randn(100,2)
#X2 = np.random.randn(100,2) + 5
#X = np.vstack((X1,X2))
#
#Y1 = np.ones(100)
#Y2 = np.zeros(100)
#Y = np.hstack((Y1,Y2))
#
#clf = SpectralClustering(n_clusters=2)
#allocation = clf.fit_predict(X)
#kernel = clf.affinity_matrix_
#axis_label = range(kernel.shape[0])
#hMap = heatMap()
#sorted_kernel = hMap.sort_kernel(kernel, allocation)
#
#hMap.draw_HeatMap(kernel, title='Drawing Unsorted Heat Map', subplot=121)
#hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map')





##	Plot cluster example
#n = 100
#x1 = np.random.randn(n,2) + np.array([4,4])
#x2 = np.random.randn(n,2) + np.array([-4,-4])
#X = np.vstack((x1,x2))
#Y = np.concatenate([np.zeros(n), np.ones(n)])
#
#cluster_plot(X, Y, title='Clustering Results')
