#!/usr/bin/env python

import numpy as np
import wplotlib
from wplotlib import scatter
from wplotlib import lines

#	Line and Scatter Plot Example
textstr = r'$y = 0.5 x + 0.5$'
x = np.array([1,2,2,3])
y = np.array([1,1,2,2])

x2 = np.arange(0,4)
y2 = x2*0.5 + 0.5
p = wplotlib.scatter(x, y, '', 'X axis', 'Y axis', xlim=[0,4], ylim=[0,4],
					ticker_fontsize=8, figsize=(10,5), show=False)


wplotlib.lines(x2, y2, 'Regression Example', 'X axis', 'Y axis', imgText=textstr, 
					ticker_fontsize=12, xticker_rotate=90, show=False)		# (width, height)


p.show() 
