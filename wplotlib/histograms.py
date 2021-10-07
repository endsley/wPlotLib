#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class histograms:
	def __init__(self, title_font=12, xfont=12, yfont=12, figsize=None):
		self.title_font = title_font
		self.xfont = xfont
		self.yfont = yfont
		self.already_called_plot_line = False
		if figsize is not None: plt.figure(figsize=figsize)

	def histogram(self, x, num_bins=10, title='', fontsize=12, facecolor='blue', α=0.5, 
			xlabel='', ylabel='', ticker_fontsize=9, ticker_rotate=0,
			path=None, subplot=None, ylogScale=False, showImg=True, normalize=False):
		'''
			normalize 	: Show the probability instead of count
			showImg		: Calls the show function at the end
		'''

		if subplot is not None: plt.subplot(subplot)


		plt.tick_params(axis='both', which='both', labelsize=ticker_fontsize)
		plt.xticks(fontsize=ticker_fontsize, rotation=ticker_rotate)
		#plt.yticks(fontsize=ticker_fontsize, rotation=ticker_rotate)

		plt.xlabel(xlabel, fontsize=fontsize)
		plt.ylabel(ylabel, fontsize=fontsize)
		plt.title(title, fontsize=fontsize)
		n, bins, patches = plt.hist(x, num_bins, facecolor=facecolor, alpha=α, density=normalize)
		if ylogScale: plt.yscale('log', nonpositive='clip')
		plt.tight_layout()

		#hist, bins = np.histogram(x, bins=num_bins)
		#logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
		#plt.hist(x, bins=logbins)
		#plt.yscale('log')

		#logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
		#plt.hist(x, bins=logbins)
		#plt.xscale('log')
	
		if subplot is None:
			if path is not None: plt.savefig(path)
			if showImg: plt.show()

	def show(self, save_path=None):
		if save_path is None: plt.show()
		else: plt.savefig(save_path)

