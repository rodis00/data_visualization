import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dosw.csv')

print(df)

czas = df['Czas']
val_1 = df['Zmienna1']
val_2 = df['Zmienna2']

plt.title('Wykres liniowy wartosci 1 i 2 wzgledem czasu')
plt.plot(czas, val_1, '--', color='brown', label='Zmienna1')
plt.plot(czas, val_2, color='red', label='Zmienna2')
plt.xlabel('Czas')
plt.ylabel('Wartości')
plt.legend(loc='center left')
plt.grid()
plt.xticks([2, 3, 4, 5])
plt.yticks([-15, -10, -5])
plt.savefig('zad_4.png')
plt.show()

