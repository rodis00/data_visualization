import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('zyski.csv', sep=',')
print(df)

plt.title('Zyski z filmów i gier')
plt.plot(df['Miesiąc'], df['Filmy'], 'b--', label='Filmy')
plt.plot(df['Miesiąc'], df['Gry'], 'g', label='Gry')
plt.legend(loc='upper left')
plt.xlabel('Miesiąc')
plt.ylabel('Zyski')
plt.grid()
plt.ylim(0, 100)
plt.show()
