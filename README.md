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


## Example Scatter Plot Usage
```python
import wplotlib 
	
textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 40)
y = np.sin(x)

lp = wplotlib.scatter(figsize=(10,5))		# (width, height)
lp.plot_scatter(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)
```
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/scatterPlot.png?raw=true)


## Example Multiple Line subPlot Usage
```python
import numpy as np
from sklearn.cluster import SpectralClustering

from wplotlib import lines
from wplotlib import heatMap
from wplotlib import cluster_plot

textstr = '\n'.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 1000)
y = np.sin(x)
y2 = np.log(x)

lp = lines(figsize=(10,5))
lp.plot_line(x, y, 'First Plot', 'X axis', 'Y axis', imgText=textstr, subplot=121)
lp.plot_line(x, y2, '2nd Plot', 'X axis', 'Y axis', imgText=textstr, subplot=122)
lp.show(save_path='twoSubplots.png') 
# when making subplots, you have to call show explicitly after all the plots, if you include path, then it will save instead of show

```
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/subplot_lines.png?raw=true)


## Example Single Histogram 
```python
from wplotlib import histograms
	
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
H = histograms()
H.histogram(x, num_bins=10, title='Basic Histogram', xlabel='value', ylabel='count', 
			facecolor='blue', α=0.5, path=None, normalize=True)

```
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/basicHistogram.png?raw=true)


## Example of Two Histograms one is log scaled
```python
from wplotlib import histograms
	
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
H = histograms(figsize=(10,5))
H.histogram(x, num_bins=10, title='Basic Histogram', facecolor='blue', α=0.5, path=None, subplot=121)
H.histogram(x, num_bins=10, title='Y Log Scaled Histogram', facecolor='blue', α=0.5, path=None, subplot=122, ylogScale=True)
H.show()
```
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/imgs/TwoHistograms.png?raw=true)



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

