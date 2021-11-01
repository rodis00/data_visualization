import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wyksz.csv')
print(df)

wyzsze = df[df['Wykształcenie'] == 'wyższe']
srednie = df[df['Wykształcenie'] == 'średnie']
podstawowe = df[df['Wykształcenie'] == 'podstawowe']

print(wyzsze)
print(srednie)
print(podstawowe)

x = np.arange(3)
plt.figure(figsize=(8, 5))
plt.title("Wykształcenie a wiek")
plt.bar(x, wyzsze["Liczebność"], width=0.25, label="wyższe", color="blue")
plt.bar(x + 0.25, srednie["Liczebność"], width=0.25, label="srednie", color="green")
plt.bar(x + 0.5, podstawowe["Liczebność"], width=0.25, label="podstawowe", color="brown")
plt.xticks([0.25, 1.25, 2.25], wyzsze["Wiek"])
plt.xlabel("Przedział wiekowy")
plt.ylabel("Liczebność")
plt.legend(loc="right")
plt.ticklabel_format(axis='y', style='plain')
plt.show()
