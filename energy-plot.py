import numpy as np
import matplotlib.pyplot as plt

def tan(x):
    val=np.tan(x)
    return val
def root(x, y):
    val=np.sqrt(np.power(y/x, 2)-1)
    return val

step=np.arange(0.01, 8.0001, 0.0001)


plt.plot(step, root(step, 8))
plt.plot(step,tan(step))
ax = plt.gca()
ax.axes.yaxis.set_ticks([])
ax.set_ylim([0,9])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('energy-plot.png', transparent=True)
plt.show()
