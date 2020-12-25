import numpy as np
import matplotlib.pyplot as plt

def well(x, a, z):
    if x < -a:
        val = 0
    elif x > a:
        val=0
    else:
        val=-z
    return val
a=5
length = np.arange(-10, 10, 0.001)
shape=[]
for i in np.arange(len(length)):
    shape.append(well(length[i],a,7))
    
plt.plot(length, shape)
ax = plt.gca()
plt.yticks([-8], ['$V_{0}$'])
plt.xticks([-a, a], ['$-a$','$a$'])
ax.tick_params(labelbottom=False,labeltop=True, length=0)
ax.set_ylim([-10,10])
ax.spines['top'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.savefig('empty-well.png', transparent=True)
plt.show()
