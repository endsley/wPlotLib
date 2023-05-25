#!/usr/bin/env python

import numpy as np
import wplotlib
from wplotlib import scatter
from wplotlib import lines

#	Line and Scatter Plot Example
textstr = r'$y = (x - 2)^2$'

x = np.arange(0,6)
y = (x-2)*(x-2)


wplotlib.lines(x, y, '', 'X axis', 'Y axis', imgText=textstr, 
					ticker_fontsize=12, xticker_rotate=90)	
#
#
#p.show() 
