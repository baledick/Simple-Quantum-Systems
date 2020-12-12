import numpy as np
import matplotlib.pyplot as plt

def scatter(x, y, z):
    val = 1+((np.power(x,2)/(4*y*(x+y)))*np.power(np.sin(2*z*np.sqrt(2*(x+y))),2))
    return val

#1+((np.power(x,2)/(4*y*(y+x)))

a=5
v0=10

energy=np.arange(0.01, 10, 0.01)
shape=[]
line=[]
for i in np.arange(len(energy)):
    shape.append(1/scatter(v0,energy[i],a))
    line.append(1)

plt.plot(energy, line)
plt.plot(energy, shape)
plt.plot
ax = plt.gca()
plt.yticks([1])
plt.xticks([5],['Energy'])
ax.tick_params(length=0)
ax.set_ylim([0,1.2])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.savefig('scatter.png', transparent=True)
plt.show()
