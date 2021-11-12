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

wplotlib.lines(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, 
					ticker_fontsize=12, xticker_rotate=90, figsize=(10,5))		# (width, height)

wplotlib.scatter(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, 
					ticker_fontsize=8, figsize=(10,5))							# (width, height)


p = wplotlib.lines(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=12, 
					xticker_rotate=90, xtick_locations=[2,4,6], xtick_labels=['A','B','C'], 
					figsize=(10,4), subplot=121)
wplotlib.scatter(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=8 , 
					xticker_rotate=90, ytick_locations=[2,4,6], ytick_labels=['A','B','C'], 
					xtick_locations=[2,4,6], xtick_labels=['A','B','C'], subplot=122)

p.show() 	# when making subplots, you have to call show explicitly after all the plots, 
			#if you include path, then it will save instead of show

