import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados4.csv")

contagem_sobreviventes = df['survived'].value_counts()
labels = ['Não Sobreviventes', 'Sobreviventes']
cores = ['#ff9999','#66b3ff']
explode = (0.1, 0)

plt.figure(figsize=(6, 6))
plt.pie(contagem_sobreviventes, labels=labels, colors=cores, autopct='%1.1f%%', startangle=140, shadow=True, explode=explode)
plt.axis('equal')
plt.title('Porcentagem de Sobreviventes e Não Sobreviventes')
plt.show()
