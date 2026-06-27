import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("spotify23dataset.csv")
print("Mean year for a song to be released: "+str(dataset["released_year"].mean()))
print("Standard deviation: "+str(dataset["released_year"].std()))
dataset["released_year"].plot()
plt.show()