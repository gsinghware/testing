"""import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans   = (20.0, 35.0, 30.0, 35.0, 27.0)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r')

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
plt.show()"""
"""
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd

fig, axes = plt.subplots(2, 1)
data = Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)"""
"""
from pylab import *
import matplotlib.pyplot  as pyplot
a = [ pow(10,i) for i in range(10) ]
fig = pyplot.figure()
ax = fig.add_subplot(2,1,1)

line, = ax.semilogy(a, color='blue', lw=2)
show()"""

from pylab import *
import matplotlib.pyplot  as pyplot
a = [ pow(10,i) for i in range(10) ]
fig = pyplot.figure()
ax = fig.add_subplot(2,1,1)

line, = ax.plot(a, color='blue', lw=2)

ax.set_yscale('log')

show()