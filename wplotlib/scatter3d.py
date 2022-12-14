#!/usr/bin/env python

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np



class scatter3d:
	"""A class that generates basic scatter plots"""
	def __init__(self, X=None, Y=None, Z=None, dataMatrix=None, title='title', xlabel='xlable', ylabel='ylable', zlabel='zlabel', subplot=None, 
					title_font=12, xfont=10, yfont=10, zfont=10, marker='x', color='blue', add_horizontal_surface_at=None,
					xlim=None, ylim=None, zlim=None, outpath=None, show=True, ticker_fontsize=9, figsize=None):
		"""
		vertical_axis_color	: 'k' is default black, or 'red'
		y_origin_axis_color
		:return: (float) probability "token" is spam based on training emails
		"""
		
		self.xfont = xfont
		self.yfont = yfont
		self.zfont = zfont
#		self.already_called_plot_line = False
		if figsize is not None: 
			fig = plt.figure(figsize=figsize)
		else:
			fig = plt.figure()

		if subplot is not None: 
			self.ax = ax = fig.add_subplot(subplot, projection='3d')
		else:
			self.ax = ax = fig.add_subplot(projection='3d')


		self.add_scatter(X=X, Y=Y, Z=Z, dataMatrix=dataMatrix, title=title, xlabel=xlabel, ylabel=ylabel, zlabel=zlabel, 
						subplot=subplot, marker=marker,color=color, add_horizontal_surface_at=add_horizontal_surface_at,
						xlim=xlim, ylim=ylim, zlim=zlim, outpath=outpath, show=show, ticker_fontsize=ticker_fontsize, title_font=title_font)

					#(X=X, Y=Y, title=title, xlabel=xlabel, ylabel=ylabel, imgText=imgText, outpath=outpath, 
#					subplot=subplot, xlim=xlim, ylim=ylim, xTextShift=xTextShift, yTextShift=yTextShift,
#					ticker_fontsize=ticker_fontsize, xTextLoc=xTextLoc, yTextLoc=yTextLoc, 
#					color=color, marker=marker, xticker_rotate=xticker_rotate, yticker_rotate=yticker_rotate,
#					xtick_locations=xtick_locations, xtick_labels=xtick_labels, grid=grid,
#					vertical_axis_loc=vertical_axis_loc, horizontal_axis_loc=horizontal_axis_loc,
#					vertical_axis_color=vertical_axis_color, horizontal_axis_color=horizontal_axis_color,
#					ytick_locations=ytick_locations, ytick_labels=ytick_labels, show=show)

	def add_scatter(self, X=None, Y=None, Z=None, dataMatrix=None, title='title', xlabel='xlable', ylabel='ylable', zlabel='zlabel',
						subplot=None, color='blue', marker='x', add_horizontal_surface_at=None, xlim=None, ylim=None, zlim=None, outpath=None, show=True,
						ticker_fontsize=9, title_font=12):
		"""
#		: X: (float) the values for x-axis
#		: Y: (float) the values for y-axis
#		: xTextShift: (float) Uses the range of x values as total, sets a percentage of place the text
#		: yTextShift: (float) Uses the range of y values as total, sets a percentage of place the text
#		: xTextLoc: (float) Uses absolute value and overrides xTextShift
#		: yTextLoc: (float) Uses absolute value and overrides yTextShift
#
		#color='blue'        # specify color by name
		#color='g'           # short color code (rgbcmyk)
		#color='0.75'        # Grayscale between 0 and 1
		#color='#FFDD44'     # Hex code (RRGGBB from 00 to FF)
		#color=(1.0,0.2,0.3) # RGB tuple, values 0 to 1
		#color='chartreuse'; # all HTML color names supported

		#Possible markers: https://matplotlib.org/stable/api/markers_api.html

		:return: None
		"""
		ax = self.ax
		if X is None:
			X = list(dataMatrix[:,0])
			Y = list(dataMatrix[:,1])
			Z = list(dataMatrix[:,2])
			

		if add_horizontal_surface_at is not None: self.add_horizontal_surface_at(add_horizontal_surface_at, xlim=xlim, ylim=ylim)

		ax.scatter(X, Y, Z, c=color, marker=marker)

		ax.set_title(title, fontsize=title_font)
		ax.tick_params(axis='both', which='both', labelsize=ticker_fontsize)
		ax.set_xlabel(xlabel, fontsize=self.xfont)
		ax.set_ylabel(ylabel, fontsize=self.yfont)
		ax.set_zlabel(zlabel, fontsize=self.zfont)

		if xlim is not None: ax.axes.set_xlim3d(left=xlim[0], right=xlim[1])
		if ylim is not None: ax.axes.set_ylim3d(bottom=ylim[0], top=ylim[1]) 
		if zlim is not None: ax.axes.set_zlim3d(bottom=zlim[0], top=zlim[1]) 
	
		
		if subplot is None and outpath is None and show: 
			plt.tight_layout()
			plt.show()
		elif outpath is not None: plt.savefig(outpath)


	def add_horizontal_surface_at(self, zloc, xlim=None, ylim=None):
		def f(x, y, zloc):
			loss = (5* x**2 + 6*x*y - 16*x + 3*y**2 - 12*y + 14)*0 + zloc
			return loss
	
		if xlim is not None: x = np.linspace(xlim[0], xlim[1], 10)
		else: x = np.linspace(-1, 1, 10)

		if ylim is not None: y = np.linspace(ylim[0], ylim[1], 10)
		else: y = np.linspace(-1, 1, 10)

		X, Y = np.meshgrid(x, y)
		Z = f(X, Y, zloc)

		self.ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.2)
		#ax.plot_surface(X2, Z2, Y2, rstride=8, cstride=8, alpha=0.2)



#		self.add_text(X, Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)

#	def add_text(self, X, Y, textstr, α=0.05, β=0.95, xTextLoc=None, yTextLoc=None):
#		if textstr is None: return
#		mX = np.min(X)
#		mY = np.min(Y)
#
#		if xTextLoc is None: xLoc = α*(np.max(X) - mX) + mX
#		else: xLoc = xTextLoc
#
#		if yTextLoc is None: yLoc = β*(np.max(Y) - mY) + mY
#		else: yLoc = yTextLoc
#
#		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#		plt.text(xLoc, yLoc, textstr, fontsize=14, verticalalignment='top', bbox=props)
#
#
#
#	def set_title(self, title, fontsize=16):
#		plt.title(title, fontsize=fontsize)
#
#	def set_xlabel(self, xlabel, fontsize=16):
#		plt.xlabel(xlabel, fontsize=fontsize)
#
#	def set_ylabel(self, ylabel, fontsize=16):
#		plt.ylabel(ylabel, fontsize=fontsize)
#
#	def add_plot(self, X,Y, color='blue', marker='x'):
#		#color='blue'        # specify color by name
#		#color='g'           # short color code (rgbcmyk)
#		#color='0.75'        # Grayscale between 0 and 1
#		#color='#FFDD44'     # Hex code (RRGGBB from 00 to FF)
#		#color=(1.0,0.2,0.3) # RGB tuple, values 0 to 1
#		#color='chartreuse'; # all HTML color names supported
#
#		#Possible markers: https://matplotlib.org/stable/api/markers_api.html
#
#		self.X = X
#		self.Y = Y
#
#		plt.scatter(X, Y, color=color, marker=marker)
#
	def show(self): 	#, save_path=None, title=None, xlabel=None, ylabel=None, imgText=None, 
					#xlim=None, ylim=None, xTextShift=0.05, yTextShift=0.95,
					#xTextLoc=None, yTextLoc=None):

		plt.show()

#		if title is not None: self.set_title(title, fontsize=self.title_font)
#		if xlabel is not None: self.set_xlabel(xlabel, fontsize=self.xfont)
#		if ylabel is not None: self.set_ylabel(ylabel, fontsize=self.yfont)
#		if imgText is not None: 
#			self.add_text(self.X, self.Y, imgText, α=xTextShift, β=yTextShift, xTextLoc=xTextLoc, yTextLoc=yTextLoc)
#
#		plt.tight_layout()
#		if save_path is None: 
#			plt.tight_layout()
#			plt.show()
#		else: plt.savefig(save_path)

#
#	def plot_line_with_error_area(x, y, error, show=False):
#		#x = np.linspace(0, 30, 30)
#		#y = np.sin(x/6*np.pi)
#		#error = np.random.normal(0.1, 0.02, size=y.shape)
#		#y += np.random.normal(0, 0.1, size=y.shape)
#		
#		plt.plot(x, y, 'k-')
#		plt.fill_between(x, y-error, y+error)
#		if show: 
#			plt.tight_layout()
#			plt.show()
#
#
#if __name__ == "__main__":
###	Example 1	
##	textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
##	x = np.linspace(0, 10, 1000)
##	y = np.sin(x)
##
##	lp = lines()
##	lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)
#
##	Example 2
#	textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
#	x = np.array([0,1,2])
#	y = np.array([1,2,3])
#	textstr = 'X   Y\n-----\n0   1\n1   2\n2   3'
#	pt = scatter(x, y, 'Mysterious Data We Want to Model', 'X axis', 'Y axis', xlim=[-2,6], ylim=[-2,6], imgText=textstr, xTextLoc=-1.5, yTextLoc=5.5)
