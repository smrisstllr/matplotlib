import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])

figure, axes = plt.subplots(2,2)
#Figure = the entire canvas
#ax = a single plot(subplot)
figure, axes = plt.subplots(2,2)
 
axes[0,0].plot(x,x*2, color="red")
axes[0,0].set_title("x*2")

axes[0,1].bar(x,x*2, color="pink")
axes[0,1].set_title("x*2")
plt.show()