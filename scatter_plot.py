import matplotlib.pyplot as plt
import numpy as np



x = np.array([0,1,1,2,3,4,5,6,7,7,8])#hr study
y = np.array([55,60,65,62,68,70,75,78,82,85,87])#grades

plt.scatter(x, y,color="skyblue",alpha=0.5,s=200,label="CLASS")

plt.title("Test scores")
plt.xlabel("hours Studied")
plt.ylabel("grade")
plt.show()