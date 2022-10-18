#!/usr/bin/env python

import numpy as np
from wplotlib import lines
from wplotlib import scatter

##	Multiple Line subPlot Example
tx1 = r'$f(x)= \alpha x + \beta$'
tx2 = r'$f(x)= \alpha x^2 + \beta x + c$'
tx3 = r'$f(x)= \alpha log(\beta x + c)$'
tx4 = r'$f(x)= \alpha sin(\beta x + \theta)$'

x = np.linspace(1, 10, 30)

y1 = 2*x + 1 + 0.7*np.random.randn(30)
y2 = (x-6)*(x-6) + 1  + 0.5*np.random.randn(30)
y3 = np.log(x)  + 0.01*np.random.randn(30)
y4 = np.sin(x)  + 0.1*np.random.randn(30)

lp = scatter(x, y1, 'Probably a Line', 'X axis', 'Y axis', imgText=tx1, subplot=221, figsize=(10,5), title_font=10, xfont=9, yfont=9)
lp.plot_scatter(x, y2, 'Probably a Parabola', 'X axis', 'Y axis', imgText=tx2, subplot=222)
lp.plot_scatter(x, y3, 'Probably a Log', 'X axis', 'Y axis', imgText=tx3, subplot=223)
lp.plot_scatter(x, y4, 'Probably a sine', 'X axis', 'Y axis', imgText=tx4, subplot=224)
lp.show() # when making subplots, you have to call show explicitly after all the plots, if you include path, then it will save instead of show


