import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('przepis.csv', sep=',', index_col=1)
print(df)

plt.title('Udział składników w przepsie')
plt.pie(df['Waga w g'], labels=df.index, autopct='%1.f%%', startangle=180)
plt.savefig('zad4.pdf')
plt.savefig('wykres.png', facecolor='r', orientation='portrait')
plt.show()
