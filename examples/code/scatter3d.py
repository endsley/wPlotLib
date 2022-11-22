#!/usr/bin/env python

import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')
import wplotlib
import wuml
import numpy as np



dataMatrix = np.array([[1,1,2]])
dataMatrix2 = np.array([[1,1,0]])

#	plot the points
S = wplotlib.scatter3d(dataMatrix=dataMatrix,  color='green', add_horizontal_surface_at=0, xlim=[0,2], ylim=[0,2], 
		zlim=[-2,5], ticker_fontsize=5, figsize=(10,6), show=False)

S.add_scatter(dataMatrix=dataMatrix2, title='3d plot', title_font=13, color='red', add_horizontal_surface_at=0, xlim=[0,2], ylim=[0,2], 
		zlim=[-2,5], ticker_fontsize=5)

