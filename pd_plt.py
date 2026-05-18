import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\smrij\OneDrive\Desktop\matplotlib\matplotlib\data.csv")

type_count= df["Type1"].value_counts(ascending=True)

plt.bar(type_count.index,type_count.values,color="#03dffc",edgecolor="black")
plt.title("# of pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()#for fit everything in figure
plt.show()