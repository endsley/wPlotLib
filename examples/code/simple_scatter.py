#!/usr/bin/env python

import numpy as np
import wplotlib
from wplotlib import scatter
from wplotlib import lines

#	Line and Scatter Plot Example
textstr = r'$y = 0.5 x + 0.5$'
#x = np.array([1,2,2,3])
#y = np.array([1,1,2,2])

x = np.array([1,2,1.5,3])
y = np.array([1,1,0,2])


x2 = np.arange(0,3.5)
y2 = x2*0.5 + 0.5
p = wplotlib.scatter(x, y, '', 'X axis', 'Y axis', xlim=[0,3.5], ylim=[0,3],
					ticker_fontsize=8, figsize=(7,5))


