#!/usr/bin/env python

import wuml
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import normalize			# version : 0.17
import matplotlib.pyplot as plt


class plot_clusters:
	def __init__(self, X, allocation, title='', xlabel='', ylabel='', 
					figsize=None, fsize=14, useGrid=True, subplot=None, imgText=None, 
					xTextShift=0.05, yTextShift=0.95, xTextLoc=None, yTextLoc=None):
		X = wuml.ensure_numpy(X)

		cmap = ['b', 'g', 'r', 'c', 'm', 'y','k']
		labels = np.unique(allocation)
		n = labels.shape[0]
	
		if figsize is not None: plt.figure(figsize=figsize) # figsize=(3,2)
		#f, axs = plt.subplots(2,2,figsize=(15,15))

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
	
		if subplot is not None: plt.subplot(subplot)
		for i, j in enumerate(labels):
			subX = X[allocation == labels[i]]
			plt.plot(subX[:,0], subX[:,1], cmap[i] + '.')
	
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title, fontsize=fsize)
		self.add_text(X[:,0], X[:,1], imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)
		if useGrid: plt.grid(linestyle='dotted')
		if subplot is None: 
			plt.tight_layout()
			plt.show()

	def add_text(self, X, Y, textstr, α=0.05, β=0.95, xTextLoc=None, yTextLoc=None):
		if textstr is None: return
		mX = np.min(X)
		mY = np.min(Y)

		if xTextLoc is None: xLoc = α*(np.max(X) - mX) + mX
		else: xLoc = xTextLoc

		if yTextLoc is None: yLoc = β*(np.max(Y) - mY) + mY
		else: yLoc = yTextLoc

		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		plt.text(xLoc, yLoc, textstr, fontsize=14, verticalalignment='top', bbox=props)


	def show(self):
		#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
		#plt.subplots_adjust(hspace=1.0, wspace=1.0)
		plt.tight_layout()
		plt.show()

if __name__ == "__main__":
	n = 100
	x1 = np.random.randn(n,2) + np.array([4,4])
	x2 = np.random.randn(n,2) + np.array([-4,-4])
	X = np.vstack((x1,x2))
	
	Y = np.concatenate([np.zeros(n), np.ones(n)])
	
	cluster_plot(X, Y, title='Clustering Results')
