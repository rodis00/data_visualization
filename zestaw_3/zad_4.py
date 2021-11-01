import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dosw3.csv', sep=';')

print(df)


plt.title('Zmienna od czasu')
plt.plot(df['Czas'], df['Zmienna'], 'g--', label='zmienna')
plt.legend(loc='upper left')
plt.xlabel('czas')
plt.ylabel('wartosci zmiennej')
plt.savefig('zad_4.png')
plt.show()
