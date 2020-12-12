import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

data=np.loadtxt(input())
l=len(data)
x = np.arange(l)

A = np.eye(l) - np.eye(l, k = -1)
A[0, l-1]=-1

fig, ax= plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(data.min(), data.max())
line, = ax.plot(x, data)

def step(data, A, n):
    for i in range(n):
        data = data - 0.5 * (A @ data)
    return data

def animate(i):
    line.set_data(x, step(data, A, i))
    return line,

animation = FuncAnimation(fig, func=animate, frames=len(range(255)), interval = 100, repeat = True)

plt.show()