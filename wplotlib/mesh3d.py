#!/usr/bin/env python

#import os
#import sys
#if os.path.exists('/home/chieh/code/wuML'):
#	sys.path.insert(0,'/home/chieh/code/wuML')
#import wuml
#%matplotlib notebook

from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib
import numpy as np


class mesh3d:
	"""A class that generates 3d mesh plots"""
	def __init__(self, X, Y, Z, title='title', xlabel='xlable', ylabel='ylable', zlabel='zlable', meshType='level', imgText=None, outpath=None, 
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker=',', show=True, 
					xticker_rotate=0, yticker_rotate=0, zticker_rotate=0,
					xtick_locations=None, xtick_labels=None, ytick_locations=None, ztick_locations=None, ytick_labels=None, ztick_labels=None,
					title_font=13, xfont=10, yfont=10, zfont=10, figsize=None):
		"""calculates the probability that "token" is found in spam emails
		: meshType: 'level', 'scatter', 'wire'
		:param token: (str)
		:return: (float) probability "token" is spam based on training emails
		"""
		font = {'family' : 'normal', 'weight' : 'bold', 'size'   : title_font}
		matplotlib.rc('font', **font)

		self.title_font = title_font
		self.xfont = xfont
		self.yfont = yfont
		self.zfont = zfont
		self.already_called_plot_line = False

		if figsize is not None: plt.figure(figsize=figsize)

		fig = plt.figure()
		ax = plt.axes(projection='3d')

		if meshType == 'wire':
			ax.plot_wireframe(X, Y, Z, color='blue')
		elif meshType == 'level':
			ax.contour3D(X, Y, Z, 50, cmap='binary')
		elif meshType == 'scatter':
			ax.scatter3D(X, Y, Z, c=Z, cmap='Greens');
		elif meshType == 'surface':
			ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
		else:
			raise

		ax.set_xlabel(xlabel, fontsize=self.xfont)
		ax.set_ylabel(ylabel, fontsize=self.yfont)
		ax.set_zlabel(zlabel, fontsize=self.zfont)
		ax.set_title(title, fontsize=self.title_font)

		plt.xticks(ticks=xtick_locations, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)
		plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )
		plt.tick_params(axis='z', which='major', labelsize=ticker_fontsize, rotation=zticker_rotate)

		plt.tight_layout()
		plt.show()




	def plot_line(self, X, Y, title, xlabel, ylabel, imgText=None, outpath=None, 
					subplot=None, xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					ticker_fontsize=9, xTextLoc=None, yTextLoc=None, color='blue', marker=',', show=True, 
					xticker_rotate=0, yticker_rotate=0,
					xtick_locations=None, xtick_labels=None, ytick_locations=None, ytick_labels=None):
		"""create a default 2D line plot
		
		: X: (float) the values for x-axis
		: Y: (float) the values for y-axis
		: xTextShift: (float) Uses the range of x values as total, sets a percentage of place the text
		: yTextShift: (float) Uses the range of y values as total, sets a percentage of place the text
		: xTextLoc: (float) Uses absolute value and overrides xTextShift
		: yTextLoc: (float) Uses absolute value and overrides yTextShift
		: marker types 		".": point		https://www.w3schools.com/python/matplotlib_markers.asp
							"o": circle
							",": just a pixel size
							"s": square
							"d": dimond
							"^": triangle
							"v": upside down triangle
							"+": plus
							"x": X
		:return: None
		"""

		if X is None: X = np.arange(1, len(Y)+1)
		if subplot is not None: plt.subplot(subplot)

		self.add_plot(X,Y, color, marker)

		#plt.tick_params(axis='both', which='both', labelsize=ticker_fontsize)
		plt.xticks(ticks=xtick_locations, labels=xtick_labels, fontsize=ticker_fontsize, rotation=xticker_rotate)
		plt.yticks(fontsize=ticker_fontsize, rotation=yticker_rotate, ticks=ytick_locations, labels=ytick_labels )

		self.set_title(title, fontsize=self.title_font)
		self.set_xlabel(xlabel, fontsize=self.xfont)
		self.set_ylabel(ylabel, fontsize=self.yfont)
		self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		if xlim is not None: plt.xlim(xlim)
		if ylim is not None: plt.ylim(ylim)
		
		plt.tight_layout()
		if subplot is None:
			if outpath is not None: plt.savefig(outpath)
			if show: plt.show()


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

	def add_plot(self, X,Y, color='blue', marker=','):
		#color='blue'        # specify color by name
		#color='g'           # short color code (rgbcmyk)
		#color='0.75'        # Grayscale between 0 and 1
		#color='#FFDD44'     # Hex code (RRGGBB from 00 to FF)
		#color=(1.0,0.2,0.3) # RGB tuple, values 0 to 1
		#color='chartreuse'; # all HTML color names supported

		plt.plot(X,Y, color=color, marker=marker)

	def show(self, save_path=None, title=None, xlabel=None, ylabel=None, imgText=None, 
					xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					xTextLoc=None, yTextLoc=None):

		if title is not None: self.set_title(title, fontsize=self.title_font)
		if xlabel is not None: self.set_xlabel(xlabel, fontsize=self.xfont)
		if ylabel is not None: self.set_ylabel(ylabel, fontsize=self.yfont)
		if imgText is not None: 
			self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

		plt.tight_layout()
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
#	# Example 1
#	def f(x, y):
#		return np.sin(np.sqrt(x ** 2 + y ** 2))
#
#	x = np.linspace(-6, 6, 30)
#	y = np.linspace(-6, 6, 30)
#	
#	X, Y = np.meshgrid(x, y)
#	Z = f(X, Y)
#
#	mesh3d(X, Y, Z, title='Set Title Here', xlabel='xlable', ylabel='ylable', zlabel='zlable', meshType='wire')
#	import pdb; pdb.set_trace()

	# Example 2
	def f(x, y):
		loss = 5* x**2 + 6*x*y - 16*x + 3*y**2 - 12*y + 14
		return loss

	x = np.linspace(-5, 5, 10)
	y = np.linspace(-5, 5, 10)
	
	X, Y = np.meshgrid(x, y)
	Z = f(X, Y)

	mesh3d(X, Y, Z, title='Error at different α,β', xlabel='α', ylabel='β', zlabel='error', meshType='wire')
	import pdb; pdb.set_trace()
