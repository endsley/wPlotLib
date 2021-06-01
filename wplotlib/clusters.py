#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import normalize			# version : 0.17
import matplotlib.pyplot as plt




def cluster_plot(X, allocation, title='', xlabel='X', ylabel='y', fsize=14, useGrid=True):
	cmap = ['b', 'g', 'r', 'c', 'm', 'y','k']

	labels = np.unique(allocation)
	n = labels.shape[0]

	plt.style.use('default')
	#plt.style.use('seaborn')
	#plt.style.use("ggplot")
	#plt.rcParams['axes.edgecolor'] = "#777777"
	#plt.rcParams['axes.facecolor'] = '#FFFFFF'

	#ax = plt.axes()
	#plt.axis([xmin, xmax, ymin, ymax])
	#ax.set_aspect('equal')
	#ax.grid(True, which='both')

	#ax.set(facecolor = 'white')
	#ax.axhline(y=0, color='k')
	#ax.axvline(x=0, color='k')

	for i, j in enumerate(labels):
		subX = X[allocation == labels[i]]
		plt.plot(subX[:,0], subX[:,1], cmap[i] + '.')

	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title, fontsize=fsize)
	plt.tight_layout()
	if useGrid: plt.grid(linestyle='dotted')
	plt.show()

if __name__ == "__main__":
	n = 100
	x1 = np.random.randn(n,2) + np.array([4,4])
	x2 = np.random.randn(n,2) + np.array([-4,-4])
	X = np.vstack((x1,x2))
	
	Y = np.concatenate([np.zeros(n), np.ones(n)])
	
	cluster_plot(X, Y, title='Clustering Results')
