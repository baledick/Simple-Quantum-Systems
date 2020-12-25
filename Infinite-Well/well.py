import numpy as np
import matplotlib.pyplot as plt

def well(x, a, z):
    val = 0
    if x<0:
        val = 10
    elif x>a:
        val = 10
    return val

def states1(x, a):
    val = 1+ np.sqrt(2/a)*np.sin(np.pi*x/a)
    return val
def states2(x, a):
    val = 3 + np.sqrt(2/a)*np.sin(2*np.pi*x/a)
    return val
def states3(x, a):
    val = 5 + np.sqrt(2/a)*np.sin(3*np.pi*x/a)
    return val
a=7
length = np.arange(-10, 10, 0.001)
shape=[]
state1=[]
state2=[]
state3=[]

for i in np.arange(len(length)):
    shape.append(well(length[i],a,7))
    state1.append(states1(length[i],a))
    state2.append(states2(length[i],a))
    state3.append(states3(length[i],a))

plt.plot(length, shape)
plt.plot(length, state1)
plt.plot(length, state2)
plt.plot(length, state3)
ax = plt.gca()
plt.yticks([1, 3, 5, 7], ['$n=1$', '$n=2$', '$n=3$', '$+\infty$'])
plt.xticks([0, a], ['$0$','$a$'])
ax.tick_params(labelbottom=True, length=0)
ax.set_ylim([0,7])
ax.set_xlim([0,a])
ax.spines['top'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_visible(False)
plt.savefig('well.png', transparent=True)
plt.show() 
