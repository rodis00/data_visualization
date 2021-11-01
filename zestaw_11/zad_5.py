import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dosw11.csv', sep=';')
print(df)

plt.subplot(2, 1, 1)
plt.title('Zmienna od czasu')
plt.plot(df['Czas'], df['Zmienna'], label='zmienna', color='r')
plt.legend(loc='upper left')

plt.subplot(2, 1, 2)
plt.title('Zmienna od czasu 2')

higher = df[df['Zmienna'] > 10]
print(higher)

higher_value = higher['Zmienna'].values
print(higher_value)

df['Zmienna'] = df['Zmienna'].replace(higher_value, 1.13)
print(df[df['Zmienna'] == 1.13])

plt.plot(df['Czas'], df['Zmienna'], label='zmienna2', color='g')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()



