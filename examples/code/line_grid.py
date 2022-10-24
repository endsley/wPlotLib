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

l = lines(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, subplot=211, 
					ticker_fontsize=12, xticker_rotate=90, figsize=(7,6))		# (width, height)

l.add_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr, subplot=212, grid=True,
					ticker_fontsize=12, xticker_rotate=90)		# (width, height)

l.show() 	# when making subplots, you have to call show explicitly after all the plots, 
			#if you include path, then it will save instead of show

