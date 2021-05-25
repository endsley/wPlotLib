# wplotlib
## Chieh's quick plot library
## Pip Installation
```sh
pip install wplotlib
```

## Example Usage
```python
from wplotlib import lines
	
textstr = ''.join(( r'$\mu=%.2f$' % (0.1, ), r'$\mathrm{median}=%.2f$' % (0, ), r'$\sigma=%.2f$' % (33, )))
x = np.linspace(0, 10, 1000)
y = np.sin(x)

lp = lines()
lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis', imgText=textstr)#, outpath)	#x can be set to None
```
## This code results in
![Image](https://github.com/endsley/wPlotLib/blob/main/wplotlib/result.png?raw=true)
