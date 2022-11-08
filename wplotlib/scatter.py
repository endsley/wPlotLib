#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np


class scatter:
	"""A class that generates basic scatter plots"""
	def __init__(self, X, Y, title='title', xlabel='xlable', ylabel='ylable', imgText=None, outpath=None, 
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker='x',
					xticker_rotate=0, yticker_rotate=0,
					vertical_axis_loc=None, horizontal_axis_loc=None,
					vertical_axis_color='k', horizontal_axis_color='k',
					xtick_locations=None, xtick_labels=None, ytick_locations=None, ytick_labels=None, 
					title_font=16, xfont=16, yfont=16, figsize=None, show=True, grid=False):
		"""calculates the probability that "token" is found in spam emails
		:param token: (str)
		vertical_axis_color	: 'k' is default black, or 'red'
		y_origin_axis_color
		:return: (float) probability "token" is spam based on training emails
		"""
		self.title_font = title_font
		self.xfont = xfont
		self.yfont = yfont
		self.already_called_plot_line = False
		if figsize is not None: plt.figure(figsize=figsize)


		self.add_scatter(X=X, Y=Y, title=title, xlabel=xlabel, ylabel=ylabel, imgText=imgText, outpath=outpath, 
					subplot=subplot, xlim=xlim, ylim=ylim, xTextShift=xTextShift, yTextShift=yTextShift,
					ticker_fontsize=ticker_fontsize, xTextLoc=xTextLoc, yTextLoc=yTextLoc, 
					color=color, marker=marker, xticker_rotate=xticker_rotate, yticker_rotate=yticker_rotate,
					xtick_locations=xtick_locations, xtick_labels=xtick_labels, grid=grid,
					vertical_axis_loc=vertical_axis_loc, horizontal_axis_loc=horizontal_axis_loc,
					vertical_axis_color=vertical_axis_color, horizontal_axis_color=horizontal_axis_color,
					ytick_locations=ytick_locations, ytick_labels=ytick_labels, show=show)

	def add_scatter(self, X, Y, title, xlabel, ylabel, imgText=None, outpath=None, 
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker='x',
					vertical_axis_loc=None, horizontal_axis_loc=None,
					vertical_axis_color='k', horizontal_axis_color='k',
					xticker_rotate=0, yticker_rotate=0, show=True, grid=False,
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


		if vertical_axis_loc is not None:
			plt.axvline(x=vertical_axis_loc, color=vertical_axis_color)
		if horizontal_axis_loc is not None:
			plt.axhline(y=horizontal_axis_loc, color=horizontal_axis_color)

		self.add_plot(X,Y, color, marker)
		self.set_title(title, fontsize=self.title_font)
		self.set_xlabel(xlabel, fontsize=self.xfont)
		self.set_ylabel(ylabel, fontsize=self.yfont)
		self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		#plt.tick_params(axis='both', which='both', labelsize=ticker_fontsize)
		plt.xticks(ticks=xtick_locations, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)
		plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )

		plt.grid(grid)
		if xlim is not None: plt.xlim(xlim)
		if ylim is not None: plt.ylim(ylim)
		
		if subplot is None and outpath is None and show: 
			plt.tight_layout()
			plt.show()
		elif outpath is not None: plt.savefig(outpath)

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

	def show(self, save_path=None, title=None, xlabel=None, ylabel=None, imgText=None, 
					xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					xTextLoc=None, yTextLoc=None):

		if title is not None: self.set_title(title, fontsize=self.title_font)
		if xlabel is not None: self.set_xlabel(xlabel, fontsize=self.xfont)
		if ylabel is not None: self.set_ylabel(ylabel, fontsize=self.yfont)
		if imgText is not None: 
			self.add_text(self.X, self.Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		plt.tight_layout()
		if save_path is None: 
			plt.tight_layout()
			plt.show()
		else: plt.savefig(save_path)


	def plot_line_with_error_area(x, y, error, show=False):
		#x = np.linspace(0, 30, 30)
		#y = np.sin(x/6*np.pi)
		#error = np.random.normal(0.1, 0.02, size=y.shape)
		#y += np.random.normal(0, 0.1, size=y.shape)
		
		plt.plot(x, y, 'k-')
		plt.fill_between(x, y-error, y+error)
		if show: 
			plt.tight_layout()
			plt.show()


if __name__ == "__main__":
##	Example 1	
#	textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
#	x = np.linspace(0, 10, 1000)
#	y = np.sin(x)
#
#	lp = lines()
#	lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)

#	Example 2
	textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
	x = np.array([0,1,2])
	y = np.array([1,2,3])
	textstr = 'X   Y\n-----\n0   1\n1   2\n2   3'
	pt = scatter(x, y, 'Mysterious Data We Want to Model', 'X axis', 'Y axis', xlim=[-2,6], ylim=[-2,6], imgText=textstr, xTextLoc=-1.5, yTextLoc=5.5)
