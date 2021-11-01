import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dosw6.csv', sep=';')

plt.title('wykres')
plt.plot(df['Czas'], df['Zmienna'], 'r-.', label='zmienna')
plt.xlim(2, 8)
plt.ylim(9, 12)
plt.legend()
plt.annotate("12345", [8, 9])
plt.xlabel('czas')
plt.show()
