#!/usr/bin/env python

import wplotlib
import numpy as np

#	set ticks
x = np.linspace(0, 10, 40)
y = np.sin(x)

lp = wplotlib.lines(figsize=(10,5))		# (width, height)
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', ticker_fontsize=12, xticker_rotate=90, xtick_locations=[2,4,6], xtick_labels=['A','B','C'])


