import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt(input())
l=len(data)

n_data = np.zeros(l)

for i in range(9):
    n_data[i] = data[0:i+1].mean()

for i in range(9, l):
    n_data[i] = data[i-9:i+1].mean()

x = np.linspace(0, l, l)
fig, ax = plt.subplots(figsize=(11, 4), nrows=1, ncols=2, sharey=True)
ax[0].plot(x, data, 'tab:red')
ax[0].set_title('Сырой сигнал')
ax[1].plot(x, n_data, 'tab:orange')
ax[1].set_title('После фильтра')
ax[0].grid()
ax[1].grid()
plt.show()