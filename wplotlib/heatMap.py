#! /usr/bin/env python


import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
from matplotlib import pyplot as plt
import matplotlib
from numpy import genfromtxt
from sklearn.cluster import SpectralClustering
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle


class heatMap:
	def __init__(self):
		self.plot_font_size = 4
		font = {'family' : 'normal', 'weight' : 'bold', 'size'   : self.plot_font_size}
		matplotlib.rc('font', **font)
		self.cluster_by_id = {}
		self.cluster_by_name = {}

	def sort_kernel(self, kernel, allocation, item_labels=[] ):
		alloc_list = np.unique(allocation) 
		ksize = kernel.shape[0]
		self.rearrangement = []

		sorted_kernel = np.empty((0, ksize))
		for m in alloc_list:
			new_list = np.where(allocation == m)[0].tolist()
			self.cluster_by_id[m] = new_list
			self.rearrangement.extend(new_list)

			if len(item_labels) > 0:
				self.cluster_by_name[m] = []
				for q in new_list:
					self.cluster_by_name[m].append( item_labels[q] )


			f = kernel[allocation == m, :]
			sorted_kernel = np.vstack((sorted_kernel, f))
			
		H_sorted_kernel = np.empty((ksize,0))
		for m in alloc_list:
			f = sorted_kernel[:,allocation == m]
			H_sorted_kernel = np.hstack((H_sorted_kernel, f))

		self.sorted_kernel = H_sorted_kernel


		#	Sort the labels if they exist
		if len(item_labels) > 0:
			self.sorted_labels = []
			for m in self.rearrangement:
				self.sorted_labels.append( item_labels[m] )

		return H_sorted_kernel

	def draw_HeatMap(self, kernel, xlabel=[], ylabel=[], title='', fsize=14, use_seaborn=False, vmin=0, vmax=1, center=None, linewidths=0, cmap=None, path=''):
		if use_seaborn:
			ax = sns.heatmap(kernel, vmin=vmin, vmax=vmax, center=center, linewidths=linewidths, cmap=cmap)
			plt.title(title, fontsize=fsize)
			plt.tight_layout()
			plt.show() 
		else:
			ylabel = list(reversed(ylabel))
			
			kernel = np.flipud(kernel)
			fig, ax = plt.subplots()
			#fig.set_size_inches(13,13)
			heatmap = plt.pcolor(kernel, cmap=matplotlib.cm.Blues, alpha=0.8)
	
			if len(ylabel) > 0:
				ax.set_yticks(np.arange(kernel.shape[0]) + 0.5, minor=False)
				ax.set_yticklabels(ylabel, rotation='horizontal', minor=False, size=fsize)
			
			if len(xlabel) > 0:
				ax.set_xticks(np.arange(kernel.shape[1]) + 0.5, minor=False)
				ax.set_xticklabels(xlabel, rotation='vertical', minor=False, size=fsize)
		 
			plt.title(title, fontsize=fsize)

			if path == '':
				plt.show() 
			else:
				plt.draw()	
				fig.savefig(path, dpi=500)

		return plt

	def save_HeatMap(self, path, kernel, xlabel=[], ylabel=[], title='',fsize=14):
		#xlabel = list(reversed(xlabel))
		ylabel = list(reversed(ylabel))
	
		kernel = np.flipud(kernel)
		fig, ax = plt.subplots()
		#fig.set_size_inches(13,13)
		heatmap = plt.pcolor(kernel, cmap=matplotlib.cm.Blues, alpha=0.8)

		if len(ylabel) > 0:
			ax.set_yticks(np.arange(kernel.shape[0]) + 0.5, minor=False)
			ax.set_yticklabels(ylabel, rotation='horizontal', minor=False, fsize=fsize)
		
		if len(xlabel) > 0:
			ax.set_xticks(np.arange(kernel.shape[1]) + 0.5, minor=False)
			ax.set_xticklabels(xlabel, rotation='vertical', minor=False, fsize=fsize)
	 
		plt.title(title,fsize=14)
		plt.draw()	
		fig.savefig(path, dpi=500)
		return plt


if __name__ == "__main__":
	X1 = np.random.randn(100,2)
	X2 = np.random.randn(100,2) + 5
	X = np.vstack((X1,X2))

	Y1 = np.ones(100)
	Y2 = np.zeros(100)
	Y = np.hstack((Y1,Y2))

	X_sparse = coo_matrix(X)
	X, X_sparse, y = shuffle(X, X_sparse, Y, random_state=0) 


	clf = SpectralClustering(n_clusters=2)
	allocation = clf.fit_predict(X)
	kernel = clf.affinity_matrix_
	axis_label = range(kernel.shape[0])
	hMap = heatMap()
	sorted_kernel = hMap.sort_kernel(kernel, allocation)

	hMap.draw_HeatMap(kernel, title='Drawing Unsorted Heat Map', fsize=14)
	hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map', fsize=14)
	hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map', use_seaborn=True, vmin=0, vmax=1, center=None, linewidths=0, cmap=None, fsize=14)
	#cmap types: "Blues", "YlGnBu", "BuPu", "Greens", None
