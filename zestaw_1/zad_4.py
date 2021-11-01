import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('sport.csv', header=None, sep=';')
print(df)

sports = df[0]
values = df[1]

plt.pie(values, labels=sports, autopct='%.0f%%', explode=(0.1, 0, 0, 0, 0, 0))
plt.title('Wykres zainteresowania sportami')
plt.text(-2.2, 1.5, '123456')
#plt.savefig('sport.pdf')
plt.show()
