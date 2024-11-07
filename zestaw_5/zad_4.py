import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('rocky.csv')
print(df)

rgb = [np.random.rand(3) for x in range(len(df.index))]
print(rgb)
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for x in range(len(df.index))]
print(color)


plt.title('Zyski')
plt.barh(df['Nazwa'], df['Zyski w mln $'], color=rgb)
plt.xlabel('Nazwa')
plt.ylabel('Zyski w mln $')
plt.show()



