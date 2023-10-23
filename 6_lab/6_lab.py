import numpy
import scipy.stats
import matplotlib.pyplot

N_points = 100000
n_bins = 20

dist = numpy.random.normal(50, 1, 100)
mu, std = scipy.stats.norm.fit(dist)  

matplotlib.pyplot.hist(dist, bins=25, density=True, alpha=0.6, color='b')

xmin, xmax = matplotlib.pyplot.xlim() 
x = numpy.linspace(xmin, xmax, 100) 
p = scipy.stats.norm.pdf(x, mu, std)

matplotlib.pyplot.plot(x, p, 'k', linewidth=1.5)
matplotlib.pyplot.show()