#!/usr/bin/env python

import numpy as np
from sklearn.cluster import SpectralClustering

import wplotlib

#from wplotlib import scatter
#from wplotlib import lines
from wplotlib import heatMap
#from wplotlib import cluster_plot
from wplotlib import histograms


##	Line and Scatter Plot Example
#textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
#x = np.linspace(0, 10, 40)
#y = np.sin(x)
#
#lp = wplotlib.lines(figsize=(10,5))		# (width, height)
#lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, ticker_fontsize=12, ticker_rotate=90)#, outpath)
#
#lp = wplotlib.scatter(figsize=(10,5))		# (width, height)
#lp.plot_scatter(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, ticker_fontsize=8 )#, outpath)


##	set ticks
#x = np.linspace(0, 10, 40)
#y = np.sin(x)
#
##lp = wplotlib.lines(figsize=(10,5))		# (width, height)
##lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=12, xticker_rotate=90, xtick_locations=[2,4,6], xtick_labels=['A','B','C'])
#lp = wplotlib.scatter(figsize=(10,5))		# (width, height)
#lp.plot_scatter(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=8 , xticker_rotate=90, xtick_locations=[2,4,6], xtick_labels=['A','B','C'])




###	Multiple Line subPlot Example
#textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
#x = np.linspace(0.1, 10, 1000)
#y = np.sin(x)
#y2 = np.log(x)
#
#lp = lines(figsize=(10,5))
#lp.plot_line(x, y, 'First Plot', 'X axis', 'Y axis', imgText=textstr, subplot=121, xlim=[0,3])
#lp.plot_line(x, y2, '2nd Plot', 'X axis', 'Y axis', imgText=textstr, subplot=122)
#lp.show(save_path='twoSubplots.png') # when making subplots, you have to call show explicitly after all the plots, if you include path, then it will save instead of show

##	Draw a histogram
#x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
#H = histograms()
#H.histogram(x, num_bins=10, title='Basic Histogram', xlabel='value', ylabel='count', facecolor='blue', α=0.5, path=None, normalize=True, ylogScale=True)


###	Draw two histograms, on of which is log scaled
#x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
#H = histograms(figsize=(10,5))
#H.histogram(x, num_bins=10, title='Basic Histogram', facecolor='blue', α=0.5, path=None, subplot=121)
#H.histogram(x, num_bins=10, title='Y Log Scaled Histogram', facecolor='blue', α=0.5, path=None, subplot=122, ylogScale=True)
#H.show()

#	Heat Map ticker
K = np.array([[0.7, 0.7, 0, 0],[0.5,0.5,0,0],[0,0,0.4, 0.8], [0,0,0.4, 0.8]])
hMap = heatMap()
hMap.draw_HeatMap(K, title='Heat Map', xtick_locations=[0.5, 1.5, 2.5, 3.5], xtick_labels=['A', 'B', 'C','D'],
					ytick_locations=[0.5, 1.5, 2.5, 3.5], ytick_labels=['A', 'B', 'C','D'])

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
