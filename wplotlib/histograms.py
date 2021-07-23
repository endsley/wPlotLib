#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class histograms:
	def __init__(self, title_font=12, xfont=12, yfont=12, figsize=(6, 6)):
		self.title_font = title_font
		self.xfont = xfont
		self.yfont = yfont
		self.already_called_plot_line = False
		plt.figure(figsize=figsize)

	def histogram(self, x, num_bins=10, title='', fontsize=12, facecolor='blue', α=0.5, path=None, subplot=None, ylogScale=False):
		if subplot is not None: plt.subplot(subplot)
	
		plt.title(title, fontsize=fontsize)
		n, bins, patches = plt.hist(x, num_bins, facecolor=facecolor, alpha=α)
		if ylogScale: plt.yscale('log', nonposy='clip')

		#hist, bins = np.histogram(x, bins=num_bins)
		#logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
		#plt.hist(x, bins=logbins)
		#plt.yscale('log')

		#logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
		#plt.hist(x, bins=logbins)
		#plt.xscale('log')
	
		if subplot is None:
			if path is None: plt.show()
			else: plt.savefig(outpath)

	def show(self, save_path=None):
		if save_path is None: plt.show()
		else: plt.savefig(save_path)

