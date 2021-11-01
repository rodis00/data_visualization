import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('medale.csv', sep=';')
print(df)

suma = df['Złote'] + df['Srebrne'] + df['Brązowe']
letnie = suma[df["Rodzaj"] == "Letnie"]
zimowe = suma[df["Rodzaj"] == "Zimowe"]
x = np.arange(len(letnie))
print(suma)
print(letnie)
print(zimowe)

lato = df[df['Rodzaj'] == 'Letnie']
zima = df[df['Rodzaj'] == 'Zimowe']


plt.subplot(2, 1, 1)
plt.bar(x, letnie, color="orange")
plt.xticks(x, lato['Miejsce'])
plt.yticks([0, 2, 4, 6, 8, 10, 12, 14])
plt.title("Medale Polski - letnie olimpiady")
plt.subplot(2, 1, 2)
plt.bar(x, zimowe)
plt.xticks(x, zima['Miejsce'])
plt.title("Medale Polski - zimowe olimpiady")
plt.tight_layout()
plt.show()

