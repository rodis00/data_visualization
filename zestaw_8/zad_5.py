import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('wyksz.csv', sep=',')
print(df)


wyzsze = df[df['Wykształcenie'] == 'wyższe']
policealne = df[df['Wykształcenie'] == 'policealne']
srednie = df[df['Wykształcenie'] == 'średnie']


x = np.arange(len(wyzsze['Wiek']))

plt.figure(figsize=(7.5, 5))
plt.title('Wykształcenie a wiek')
plt.bar(x, wyzsze['Liczebność'], width=.25, label='wyższe', color='purple')
plt.bar(x + 0.25, policealne['Liczebność'], width=.25, label='policealne', color='brown')
plt.bar(x + 0.50, srednie['Liczebność'], width=.25, label='średnie', color='green')
plt.legend(loc='right')
plt.ticklabel_format(style='plain')
plt.ylabel('Liczebność')
plt.xlabel('Przedział wiekowy')
plt.xticks([.25, 1.25, 2.25], wyzsze['Wiek'])
plt.show()
