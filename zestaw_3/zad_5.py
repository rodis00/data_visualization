import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('medale.csv', sep=';')

print(df)

suma = df['Złote'] + df['Srebrne'] + df['Brązowe']
print(suma)

letnie = suma[df['Rodzaj'] == 'Letnie']
zimowe = suma[df['Rodzaj'] == 'Zimowe']


print(letnie)
print(zimowe)

letnie_miejsce = df[df['Rodzaj'] == 'Letnie']['Miejsce']
zimowe_miejsce = df[df['Rodzaj'] == 'Zimowe']['Miejsce']

print(letnie_miejsce)
print(zimowe_miejsce)


plt.subplot(2, 1, 1)
plt.title('Medale Polski - zimowe olimpiady')
plt.bar(zimowe_miejsce, zimowe, color='blue')
plt.subplot(2, 1, 2)
plt.title('Medale Polski - letnie olimpiady')
plt.bar(letnie_miejsce, letnie, color='orange')
plt.yticks([0, 2, 4, 6, 8, 10, 12, 14])
plt.tight_layout()
plt.show()
