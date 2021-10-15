#!/usr/bin/env python

import numpy as np
from wplotlib import lines

##	Multiple Line subPlot Example
textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0.1, 10, 1000)
y = np.sin(x)
y2 = np.log(x)

lp = lines(figsize=(10,5))
lp.plot_line(x, y, 'First Plot', 'X axis', 'Y axis', imgText=textstr, subplot=121, xlim=[0,3])
lp.plot_line(x, y2, '2nd Plot', 'X axis', 'Y axis', imgText=textstr, subplot=122)
lp.show() # when making subplots, you have to call show explicitly after all the plots, if you include path, then it will save instead of show


