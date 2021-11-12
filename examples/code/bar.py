#!/usr/bin/env python

import wplotlib

X = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
Y = [5, 6, 15, 22, 24, 8]
B = wplotlib.bar(X,Y, 'Energy Percentage', 'Energy Type', 'Amount')
