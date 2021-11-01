import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('planety.csv', sep=',')
print(df)

planety = df[df['Masa'] > 100000]

color = [np.random.rand(3) for x in range(len(planety.index))]

plt.title('Masa planet')
plt.pie(planety['Masa'], labels=planety['Planeta'], autopct='%.1f%%', colors=color)
plt.annotate('12345', (-1.25, -1))
plt.savefig('zad_4.png')
plt.show()
