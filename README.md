# wplotlib
## Chieh's quick plot library
## Pip Installation
```sh
pip install wplotlib
```

## Example Line Plot Usage
```python
from wplotlib import lines
	
textstr = ''.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 1000)
y = np.sin(x)

lp = lines()
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)	#x can be set to None
```
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/line_output.png?raw=true)

## Example Heat Map Usage
```python
import numpy as np
from wplotlib import heatMap
from sklearn.cluster import SpectralClustering
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle

X1 = np.random.randn(100,2)
X2 = np.random.randn(100,2) + 5
X = np.vstack((X1,X2))

Y1 = np.ones(100)
Y2 = np.zeros(100)
Y = np.hstack((Y1,Y2))

X_sparse = coo_matrix(X)
X, X_sparse, y = shuffle(X, X_sparse, Y, random_state=0) 


clf = SpectralClustering(n_clusters=2)
allocation = clf.fit_predict(X)
kernel = clf.affinity_matrix_
axis_label = range(kernel.shape[0])
hMap = heatMap()
sorted_kernel = hMap.sort_kernel(kernel, allocation)

hMap.draw_HeatMap(kernel, title='Drawing Unsorted Heat Map')
hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map')
```

## This code results in
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/Unsorted_HeatMap_output.png?raw=true)
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/Sorted_HeatMap_output.png?raw=true)

