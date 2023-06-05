#!/usr/bin/env python

import wplotlib

X = ['Nuclear', 'Hydro', 'Oil']
Y = [0.25, 0.25, 0.5]
B = wplotlib.bar(X,Y, 'Some bar chart', 'x', 'p(x)', horizontal=False)
