#!/usr/bin/env python

import numpy as np
from wplotlib import lines

textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 1000)
y = np.sin(x)

lp = lines()
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)

