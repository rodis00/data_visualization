import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dosw4.csv')

print(df)

plt.title('Wykres')
plt.plot(df['Czas'], df['Zmienna'], '.', label='zmienna')
plt.xlabel('os x')
plt.ylabel('os y')
plt.legend(loc='lower center')
plt.savefig('zad_4.pdf')
plt.show()
