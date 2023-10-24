import matplotlib.pyplot 
import numpy

def f1(x):
    return ((numpy.abs(x)**(2/3)) + numpy.lib.scimath.sqrt((numpy.abs(x)**4/3) + (1-(x**2)*4)))/2

def f2(x):
    return ((numpy.abs(x)**(2/3)) - numpy.lib.scimath.sqrt((numpy.abs(x)**4/3) + (1-(x**2)*4)))/2

x_positive = numpy.arange(-0.75, 0.75, 0.005)

y_positive_1 = f1(x_positive)
y_positive_2 = f2(x_positive)

matplotlib.pyplot.xlim(min(x_positive), max(x_positive))

matplotlib.pyplot.plot(x_positive, y_positive_1)
matplotlib.pyplot.plot(x_positive, y_positive_2)

matplotlib.pyplot.show()