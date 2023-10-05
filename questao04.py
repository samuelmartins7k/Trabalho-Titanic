import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dados4.csv")

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='fare', alpha=0.5)
plt.xlabel('Idade')
plt.ylabel('Tarifa')
plt.title('Gráfico de Dispersão: Idade vs. Tarifa')
plt.show()