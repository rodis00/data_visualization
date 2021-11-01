import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dosw7.csv', sep=';')
print(df)

plt.title('Wyniki doświadczenia')
plt.plot(df['Czas'], df['Zmienna1'], 'b--', label='zmienna 1')
plt.plot(df['Czas'], df['Zmienna2'], 'g', label='zmienna 2')
plt.xlabel('Czas')
plt.ylabel('Zmienna')
plt.legend(loc='lower left')
plt.grid()
plt.show()
