import matplotlib.pyplot as plt
import numpy as np

#Barchart = Circular Chart divided into slice to show parcentage of the total.
#           food foe visualization distribution among categories.
#for karger dat set we should use numpy array not python list
#python list of strings doesnt really benefit from np array 
categories = ["Freshmen", "Sphomores","Juniors","Seniors"]
values = np.array([300,250,275,225])
colors =["red","yellow","blue","green"]
#sungle % means format specifier so to show uo % sign we use Double %% .
plt.pie(values, labels=categories,
                autopct="%1.1f%%" ,
                colors=colors,
                explode=[0,0,0,0.2],
                shadow=True,
                startangle=180)
plt.title("Sj the badass")
plt.show()