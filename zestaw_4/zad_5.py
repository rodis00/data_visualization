import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('wyksz.csv')
print(df)

wyzsze = df[df['Wykształcenie'] == 'wyższe']
srednie = df[df['Wykształcenie'] == 'średnie']
podstawowe = df[df['Wykształcenie'] == 'podstawowe']

print(wyzsze)
print(srednie)
print(podstawowe)


x = np.arange(3)
plt.title('Wykształcenie a wiek')
plt.bar(x, wyzsze['Liczebność'], label='wyższe', color='blue', width=0.25)
plt.bar(x+0.25, srednie['Liczebność'], label='średnie', color='green', width=0.25)
plt.bar(x+0.5, podstawowe['Liczebność'], label='podstawowe', color='brown', width=0.25)
plt.xlabel('Przedział wiekowy')
plt.ylabel('Liczebność')
plt.xticks([0.25, 1.25, 2.25], wyzsze['Wiek'])
plt.legend(loc='center right')
plt.ticklabel_format(axis='y', style='plain') #plain, sci, scientific
plt.show()
