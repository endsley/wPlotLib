# wplotlib
## Chieh's quick plot library
## Pip Installation
```sh
pip install wplotlib
```

## Example Line Plot Usage
```python
from wplotlib import lines
from sklearn.cluster import SpectralClustering
	
textstr = ''.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 1000)
y = np.sin(x)

lp = lines()
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)	#x can be set to None
```
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/line_output.png?raw=true)

## Example Heat Map Usage
```python
from wplotlib import heatMap

X1 = np.random.randn(100,2)
X2 = np.random.randn(100,2) + 5
X = np.vstack((X1,X2))

Y1 = np.ones(100)
Y2 = np.zeros(100)
Y = np.hstack((Y1,Y2))

clf = SpectralClustering(n_clusters=2)
allocation = clf.fit_predict(X)
kernel = clf.affinity_matrix_
axis_label = range(kernel.shape[0])
hMap = heatMap()
sorted_kernel = hMap.sort_kernel(kernel, allocation)

hMap.draw_HeatMap(kernel, title='Drawing Unsorted Heat Map', fsize=14)
hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map', fsize=14)
hMap.draw_HeatMap(sorted_kernel, title='Drawing Sorted Heat Map', use_seaborn=True, vmin=0, vmax=1, center=None, linewidths=0, cmap=None, fsize=14)
#cmap types: "Blues", "YlGnBu", "BuPu", "Greens", None

```

## This code results in
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/Unsorted_HeatMap_output.png?raw=true)
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/Sorted_HeatMap_output.png?raw=true)
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/Sorted_HeatMap_output2.png?raw=true)

## Example Clustering Plots
```python
from wplotlib import cluster_plot
import numpy as np

n = 100
x1 = np.random.randn(n,2) + np.array([4,4])
x2 = np.random.randn(n,2) + np.array([-4,-4])
X = np.vstack((x1,x2))

Y = np.concatenate([np.zeros(n), np.ones(n)])

cluster_plot(X, Y, title='Clustering Results')
```

## This code results in
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/clustering.png?raw=true)

