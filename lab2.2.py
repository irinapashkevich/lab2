import numpy as np
import matplotlib.pyplot as plt

f = open(input())
a = []
for line in f:
    a.append(float(line.split()[0]))

data = np.zeros(len(a))

for i in range(len(a)):
    data[i] = a[i]

n_data = np.zeros(len(a))

for i in range(9):
    n_data[i] = data[0:i+1].mean()

for i in range(9, len(a)):
    n_data[i] = data[i-9:i+1].mean()

x = np.linspace(0, len(a), len(a))
fig, ax = plt.subplots(figsize=(11, 4), nrows=1, ncols=2, sharey=True)
ax[0].plot(x, data, 'tab:red')
ax[0].set_title('Сырой сигнал')
ax[1].plot(x, n_data, 'tab:orange')
ax[1].set_title('После фильтра')
ax[0].grid()
ax[1].grid()
plt.show()