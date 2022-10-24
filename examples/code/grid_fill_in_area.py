#!/usr/bin/env python
import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')

import numpy as np
from sklearn.cluster import SpectralClustering
from wplotlib import lines
from wplotlib import scatter

#	Line and Scatter Plot Example
textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 40)
y = np.sin(x)

#	Top image
l = lines(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, subplot=211, 
					ticker_fontsize=8, xticker_rotate=90, figsize=(7,6))		# (width, height)
l.fill_area()

#	Bottom image
x2 = np.linspace(2, 4, 20)
y2 = np.sin(x2) + 1

l.add_line(x, y+1, 'Title Here', 'X axis', 'Y axis', subplot=212, grid=True,
					ticker_fontsize=5, xticker_rotate=90)		# (width, height)

l.fill_area(x=x2, y=y2, color='pink')

l.show() 	# when making subplots, you have to call show explicitly after all the plots, 
			#if you include path, then it will save instead of show

