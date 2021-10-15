#!/usr/bin/env python

import numpy as np
from sklearn.cluster import SpectralClustering

import wplotlib

from wplotlib import scatter
from wplotlib import lines

#	Line and Scatter Plot Example
textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 40)
y = np.sin(x)

lp = wplotlib.lines(figsize=(10,5))		# (width, height)
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, ticker_fontsize=12, xticker_rotate=90)#, outpath)

lp = wplotlib.scatter(figsize=(10,5))		# (width, height)
lp.plot_scatter(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, ticker_fontsize=8 )#, outpath)


lp = wplotlib.lines(figsize=(10,5))		# (width, height)
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=12, xticker_rotate=90, xtick_locations=[2,4,6], xtick_labels=['A','B','C'])

lp = wplotlib.scatter(figsize=(10,5))		# (width, height)
lp.plot_scatter(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=8 , xticker_rotate=90, 
					ytick_locations=[2,4,6], ytick_labels=['A','B','C'],
					xtick_locations=[2,4,6], xtick_labels=['A','B','C'])

