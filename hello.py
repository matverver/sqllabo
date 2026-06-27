import pandas as pd
import matplotlib.pyplot as plt
print ("First commit")
dataset = pd.read_csv("spotify23dataset.csv")
print(dataset.columns)
dataset.plot()
plt.show()