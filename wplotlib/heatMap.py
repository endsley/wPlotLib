#! /usr/bin/env python


import numpy as np; np.random.seed(0)
import seaborn as sns
from matplotlib import pyplot as plt
from numpy import genfromtxt
from sklearn.cluster import SpectralClustering
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle

import warnings
warnings.filterwarnings("ignore")

import matplotlib


class heatMap:
	def __init__(self, kernel, title='', xlabel='Features', ylabel='Samples', ticker_fontsize=9,
						fsize=14, use_seaborn=False, vmin=0, vmax=1, show=True,
						center=None, linewidths=0, cmap=None, outpath='', subplot=None,
						xticker_rotate=0, yticker_rotate=0, sort_kernel_based_on_label=False, label=None, 
						xtick_locations=None, xtick_labels=None, ytick_locations=None, ytick_labels=None, figsize=None):

		self.plot_font_size = 4
		font_family = matplotlib.rcParams['font.family']
		font = {'family' : font_family[0], 'weight' : 'bold', 'size'   : self.plot_font_size}
		matplotlib.rc('font', **font)
		self.cluster_by_id = {}
		self.cluster_by_name = {}

		if figsize is not None: plt.figure(figsize=figsize)


		if sort_kernel_based_on_label:
			kernel = self.sort_kernel(kernel, label)

		self.draw_HeatMap(kernel, title=title, xlabel=xlabel, ylabel=ylabel, ticker_fontsize=ticker_fontsize,
						fsize=fsize, use_seaborn=use_seaborn, vmin=vmin, vmax=vmax, show=show,
						center=center, linewidths=linewidths, cmap=cmap, outpath=outpath, subplot=subplot,
						xticker_rotate=xticker_rotate, yticker_rotate=yticker_rotate,
						xtick_locations=xtick_locations, xtick_labels=xtick_labels, 
						ytick_locations=ytick_locations, ytick_labels=ytick_labels)




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

	def draw_HeatMap(self, kernel, title='', 
						xlabel='Features', ylabel='Samples', ticker_fontsize=9,
						fsize=14, use_seaborn=False, vmin=0, vmax=1, 
						center=None, linewidths=0, cmap=None, outpath=None, subplot=None,
						xticker_rotate=0, yticker_rotate=0, show=False,
						xtick_locations=None, xtick_labels=None, ytick_locations=None, ytick_labels=None):

		if use_seaborn:
			ax = sns.heatmap(kernel, vmin=vmin, vmax=vmax, center=center, linewidths=linewidths, cmap=cmap)
			plt.title(title, fontsize=fsize)
			plt.xticks(fontsize=ticker_fontsize, rotation=xticker_rotate)
			plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate)
		
			plt.tight_layout()
			plt.show() 
		else:
			
			kernel = np.flipud(kernel)
			#fig, ax = plt.subplots()
			#plt.subplots(2,1)
			#if subplot is None: fig, ax = plt.subplots()
			#else: fig, ax = plt.subplots(subplot)
			#fig.set_size_inches(13,13)

			if subplot is not None: plt.subplot(subplot)
			heatmap = plt.pcolor(kernel, cmap=matplotlib.cm.Blues, alpha=0.8)

			#yTicklabel = list(reversed(yTicklabel))
			#if len(yTicklabel) > 0:
			#	ax.set_yticks(np.arange(kernel.shape[0]) + 0.5, minor=False)
			#	ax.set_yticklabels(yTicklabel, rotation='horizontal', minor=False, size=fsize)
			
			#if len(xTicklabel) > 0:
			#	ax.set_xticks(np.arange(kernel.shape[1]) + 0.5, minor=False)
			#	ax.set_xticklabels(xTicklabel, rotation='vertical', minor=False, size=fsize)
		 
			plt.title(title, fontsize=fsize)
			plt.xticks(ticks=xtick_locations, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)
			plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )

			#ax.tick_params(axis='both', which='major', labelsize=ticker_fontsize)
			#ax.tick_params(axis='both', which='minor', labelsize=ticker_fontsize)
			#plt.xticks(fontsize=ticker_fontsize, rotation=ticker_rotate)
			#plt.yticks(fontsize=ticker_fontsize, rotation=ticker_rotate)

			if xlabel != '': plt.xlabel(xlabel, fontsize=fsize)
			if ylabel != '': plt.ylabel(ylabel, fontsize=fsize)
		

			plt.tight_layout()
			if subplot is None and show == True: plt.show()
			if outpath is not None: plt.savefig(outpath)

		return plt

	def show(self):
		plt.tight_layout()
		plt.show()

if __name__ == "__main__":
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
	heatMap(kernel, title='Drawing Sorted Heat Map', sort_kernel_based_on_label=True, label=allocation, subplot=122)
	hM.show()

	#cmap types: "Blues", "YlGnBu", "BuPu", "Greens", None
