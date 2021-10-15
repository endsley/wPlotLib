#!/usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np


class bar:
	"""A class that generates basic bar plots"""
	def __init__(self, title_font=16, xfont=16, yfont=16, figsize=None):
		"""calculates the probability that "token" is found in spam emails
		
		:param token: (str)
		:return: (float) probability "token" is spam based on training emails
		"""
		self.title_font = title_font
		self.xfont = xfont
		self.yfont = yfont
		self.already_called_plot_line = False
		plt.style.use('ggplot')
		if figsize is not None: plt.figure(figsize=figsize)

	def plot_bar(self, X, Y, title, xlabel, ylabel, imgText=None, outpath=None, 
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker=',', showImg=True, 
					xticker_rotate=0, yticker_rotate=0,
					ytick_locations=None, ytick_labels=None):



		x_pos = [i for i, _ in enumerate(X)]
		plt.bar(x_pos, Y, color=color)

		self.set_title(title, fontsize=self.title_font)
		self.set_xlabel(xlabel, fontsize=self.xfont)
		self.set_ylabel(ylabel, fontsize=self.yfont)
		if imgText is not None: 
			self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		plt.xticks(ticks=x_pos, labels=X, fontsize=ticker_fontsize, rotation=xticker_rotate)
		plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )

		plt.tight_layout()
		if subplot is None:
			if outpath is not None: plt.savefig(outpath)
			if showImg: plt.show()

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

	def set_title(self, title, fontsize=16):
		plt.title(title, fontsize=fontsize)


	def set_xlabel(self, xlabel, fontsize=16):
		plt.xlabel(xlabel, fontsize=fontsize)

	def set_ylabel(self, ylabel, fontsize=16):
		plt.ylabel(ylabel, fontsize=fontsize)

