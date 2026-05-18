import matplotlib.pyplot as plt
#list
x = [2023,2024,2025,2026]
y = [15, 25, 100,20]

plt.plot(x,y)

plt.show()

#array : which is faster than pylist

import numpy as np

x = np.array([2023,2024,2025,2026])
y = np.array([15, 25, 30,20])
plt.plot(x,y)
plt.show()