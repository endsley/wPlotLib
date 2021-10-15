#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np


class scatter:
	"""A class that generates basic scatter plots"""
	def __init__(self, title_font=16, xfont=16, yfont=16, figsize=None):
		"""calculates the probability that "token" is found in spam emails
		
		:param token: (str)
		:return: (float) probability "token" is spam based on training emails
		"""
		self.title_font = title_font
		self.xfont = xfont
		self.yfont = yfont
		self.already_called_plot_line = False
		if figsize is not None: plt.figure(figsize=figsize)

	def plot_scatter(self, X, Y, title, xlabel, ylabel, imgText=None, outpath=None, 
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker='x',
					xticker_rotate=0, yticker_rotate=0,
					xtick_locations=None, xtick_labels=None, ytick_locations=None, ytick_labels=None):
		"""create a default 2D line plot
		
		: X: (float) the values for x-axis
		: Y: (float) the values for y-axis
		: xTextShift: (float) Uses the range of x values as total, sets a percentage of place the text
		: yTextShift: (float) Uses the range of y values as total, sets a percentage of place the text
		: xTextLoc: (float) Uses absolute value and overrides xTextShift
		: yTextLoc: (float) Uses absolute value and overrides yTextShift

		#color='blue'        # specify color by name
		#color='g'           # short color code (rgbcmyk)
		#color='0.75'        # Grayscale between 0 and 1
		#color='#FFDD44'     # Hex code (RRGGBB from 00 to FF)
		#color=(1.0,0.2,0.3) # RGB tuple, values 0 to 1
		#color='chartreuse'; # all HTML color names supported

		#Possible markers: https://matplotlib.org/stable/api/markers_api.html

		:return: None
		"""

		self.X = X
		self.Y = Y

		if X is None: X = np.arange(1, len(Y)+1)
		if subplot is not None: plt.subplot(subplot)

		self.add_plot(X,Y, color, marker)
		self.set_title(title, fontsize=self.title_font)
		self.set_xlabel(xlabel, fontsize=self.xfont)
		self.set_ylabel(ylabel, fontsize=self.yfont)
		self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		#plt.tick_params(axis='both', which='both', labelsize=ticker_fontsize)
		plt.xticks(ticks=xtick_locations, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)
		plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )





		if xlim is not None: plt.xlim(xlim)
		if ylim is not None: plt.ylim(ylim)
		
		if subplot is None:
			if outpath is None: plt.show()
			else: plt.savefig(outpath)

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

	def add_plot(self, X,Y, color='blue', marker='x'):
		#color='blue'        # specify color by name
		#color='g'           # short color code (rgbcmyk)
		#color='0.75'        # Grayscale between 0 and 1
		#color='#FFDD44'     # Hex code (RRGGBB from 00 to FF)
		#color=(1.0,0.2,0.3) # RGB tuple, values 0 to 1
		#color='chartreuse'; # all HTML color names supported

		#Possible markers: https://matplotlib.org/stable/api/markers_api.html

		self.X = X
		self.Y = Y

		plt.scatter(X, Y, color=color, marker=marker)

	def show(self, save_path=None, title='', xlabel='', ylabel='', imgText=None, 
					xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					xTextLoc=None, yTextLoc=None):


		self.set_title(title, fontsize=self.title_font)
		self.set_xlabel(xlabel, fontsize=self.xfont)
		self.set_ylabel(ylabel, fontsize=self.yfont)
		if imgText is not None:
			self.add_text(self.X, self.Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		if save_path is None: plt.show()
		else: plt.savefig(save_path)


	def plot_line_with_error_area(x, y, error, show=False):
		#x = np.linspace(0, 30, 30)
		#y = np.sin(x/6*np.pi)
		#error = np.random.normal(0.1, 0.02, size=y.shape)
		#y += np.random.normal(0, 0.1, size=y.shape)
		
		plt.plot(x, y, 'k-')
		plt.fill_between(x, y-error, y+error)
		if show: plt.show()


if __name__ == "__main__":
	textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
	x = np.linspace(0, 10, 1000)
	y = np.sin(x)

	lp = lines()
	lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)
