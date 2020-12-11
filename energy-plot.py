import numpy as np
import matplotlib.pyplot as plt

def tan(x):
    val=np.tan(x)
    return val
def root(x, y):
    val=np.sqrt(np.power(y/x, 2)-1)
    return val

step=np.arange(0.01, 8.0001, 0.0001)

#pi_spots=np.array(['$\pi/2$', '$\pi/2$', '$\pi/2$','$\pi/2$'])
#plt.style.use('greyscale')
#plt.xticks(step, pi_spots)
plt.plot(step, root(step, 8))
plt.plot(step,tan(step))
yax = plt.gca()
yax.axes.yaxis.set_ticks([])
yax.set_ylim([0,9])
plt.savefig('energy-plot.png')
plt.show()
