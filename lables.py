import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15, 25, 30,20])
y2 = np.array([17, 23, 38, 5])

plt.title("Class size", fontsize=20,
                            family="Arial",
                            fontweight="bold")
plt.xlabel("Year", fontsize=20,
                    family="Arial",
                    fontweight = "bold",
                    color="#2dbefc")
plt.ylabel("Students", fontsize=20,
                    family="Arial",
                    fontweight = "bold",
                    color="#2dbefc")
plt.tick_params(axis="both",
               colors="#2dbefc")
plt.plot(x,y1)
plt.plot(x,y2)

plt.show()