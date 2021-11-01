import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('sport6.csv', sep='_')

print(df)

m = df[df['Płeć'] == 'M']
k = df[df['Płeć'] == 'K']

color1 = [np.random.rand(3) for i in range(len(m.index))]
color2 = [np.random.rand(3) for i in range(len(k.index))]

plt.subplot(2, 1, 1)
plt.title('Mężczyźni')
plt.bar(m['Sport'], m['Popularność'], color=color1)
plt.ylim(0, 60)

plt.subplot(2, 1, 2)
plt.title('Kobiety')
plt.bar(k['Sport'], k['Popularność'], color=color2)
plt.ylim(0, 60)
plt.tight_layout()
plt.show()
