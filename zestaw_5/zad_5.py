import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sport5.csv', sep='#')

print(df)

k = df[df['Płeć'] == 'K']
m = df[df['Płeć'] == 'M']

plt.subplot(1, 2, 1)
plt.title('Zainteresowanie sportem mężczyzn')
plt.pie(m['Popularność'], labels=m['Sport'], autopct='%.0f%%')

plt.subplot(1, 2, 2)
plt.title('Zainteresowanie sportem kobiet')
plt.pie(k['Popularność'], labels=k['Sport'], autopct='%.0f%%')
plt.tight_layout()
plt.show()
