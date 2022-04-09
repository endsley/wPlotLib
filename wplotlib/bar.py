#!/usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np


class bar:
	"""A class that generates basic bar plots"""
	def __init__(self, X, Y, title='', xlabel='', ylabel='', imgText=None, outpath=None, horizontal=False,
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker=',', show=True, 
					xtick_labels=None, xticker_rotate=0, yticker_rotate=0,
					ytick_locations=None, ytick_labels=None, 
					title_font=16, xfont=16, yfont=16, figsize=None):

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
	
		self.plot_bar(X=X, Y=Y, title=title, xlabel=xlabel, ylabel=ylabel, imgText=imgText, outpath=outpath, horizontal=horizontal,
					subplot=subplot, xlim=xlim, ylim=ylim, xTextShift=xTextShift, yTextShift=yTextShift,
					ticker_fontsize=ticker_fontsize, xTextLoc=xTextLoc, yTextLoc=yTextLoc, color=color, marker=marker, show=show, 
					xtick_labels=None, xticker_rotate=xticker_rotate, yticker_rotate=0,
					ytick_locations=None, ytick_labels=None)

	def plot_bar(self, X, Y, title, xlabel, ylabel, imgText=None, outpath=None, horizontal=False,
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker=',', show=True, 
					xtick_labels=None, xticker_rotate=0, yticker_rotate=0,
					ytick_locations=None, ytick_labels=None):

		if subplot is not None: plt.subplot(subplot)
		x_pos = [i for i, _ in enumerate(X)]
		if horizontal:
			plt.barh(x_pos, Y, color=color)

			self.set_ylabel(xlabel, fontsize=self.xfont)
			self.set_xlabel(ylabel, fontsize=self.yfont)
			if imgText is not None: 
				self.add_text(Y, x_pos, imgText, α=yTextShift, β=xTextShift, xTextLoc=yTextLoc, yTextLoc=xTextLoc)
	
			if xtick_labels is None: plt.yticks(ticks=x_pos, labels=X, fontsize=ticker_fontsize, rotation=xticker_rotate)
			else: plt.yticks(ticks=x_pos, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)

			plt.xticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )

		else:
			plt.bar(x_pos, Y, color=color)

			self.set_xlabel(xlabel, fontsize=self.xfont)
			self.set_ylabel(ylabel, fontsize=self.yfont)
			if imgText is not None: 
				self.add_text(x_pos, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

			if xtick_labels is None: plt.xticks(ticks=x_pos, labels=X, fontsize=ticker_fontsize, rotation=xticker_rotate)
			else: plt.xticks(ticks=x_pos, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)
			plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )

		self.set_title(title, fontsize=self.title_font)
		plt.tight_layout()
		if subplot is None:
			if outpath is not None: plt.savefig(outpath)
			if show: plt.show()

	def add_text(self, X, Y, textstr, α=0.05, β=0.95, xTextLoc=None, yTextLoc=None):
		if textstr is None: return
		mX = np.min(X)
		maX = np.max(X)

		mY = np.min(Y)
		maY = np.max(Y)

		if xTextLoc is None: xLoc = α*(maX - mX) + mX
		else: xLoc = xTextLoc

		if yTextLoc is None: yLoc = β*(maY - mY) + mY
		else: yLoc = yTextLoc

		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		plt.text(xLoc, yLoc, textstr, fontsize=14, verticalalignment='top', bbox=props)

	def set_title(self, title, fontsize=16):
		plt.title(title, fontsize=fontsize)


	def set_xlabel(self, xlabel, fontsize=16):
		plt.xlabel(xlabel, fontsize=fontsize)

	def set_ylabel(self, ylabel, fontsize=16):
		plt.ylabel(ylabel, fontsize=fontsize)

	def show(self, save_path=None, title=None, xlabel=None, ylabel=None, imgText=None, 
					xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					xTextLoc=None, yTextLoc=None):

		if title is not None: self.set_title(title, fontsize=self.title_font)
		if xlabel is not None: self.set_xlabel(xlabel, fontsize=self.xfont)
		if ylabel is not None: self.set_ylabel(ylabel, fontsize=self.yfont)
		if imgText is not None: 
			self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		if save_path is None: plt.show()
		else: plt.savefig(save_path)


