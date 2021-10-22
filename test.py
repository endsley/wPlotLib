#!/usr/bin/env python

import numpy as np
import wplotlib


X = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
Y = [5, 6, 15, 22, 24, 8]
B = wplotlib.bar()
B.plot_bar(X,Y, 'Energy Percentage', 'Energy Type', 'Amount', imgText='Extra Note')
