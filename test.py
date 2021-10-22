#!/usr/bin/env python

import numpy as np
from wplotlib import histograms

#	Draw a histogram
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
H = histograms()
H.histogram(x, num_bins=10, title='Basic Histogram', xlabel='value', ylabel='count', facecolor='blue', α=0.5, path=None, normalize=True, ylogScale=True)


##	Draw two histograms, on of which is log scaled
H = histograms(figsize=(10,5))
H.histogram(x, num_bins=10, title='Basic Histogram', facecolor='blue', α=0.5, path=None, subplot=121)
H.histogram(x, num_bins=10, title='Y Log Scaled Histogram', facecolor='blue', α=0.5, path=None, subplot=122, ylogScale=True)
H.show()

