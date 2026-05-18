import matplotlib.pyplot as plt
import numpy as np

# BarChart = compare categories of data by representing each category with bar

categories =np.array(["Grains", "Fruits", "Vegetables","Protein","Dairy","Sweets"])
values=np.array([4,3,2,5,3,1])
#vertical bar chart
plt.bar(categories,values,color="pink")
#horizontal bar chart
plt.barh(categories,values,color="green")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()