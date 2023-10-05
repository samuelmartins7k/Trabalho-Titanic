import pandas as pd


df = pd.read_csv("dados4.csv")


moda_idades = df['age'].mode()[0]
df['age'].fillna(moda_idades, inplace=True)


df.to_csv('Resposta01.txt', index=False)


somatorio_homens = df[df['sex'] == 'male']['sex'].count()
somatorio_mulheres = df[df['sex'] == 'female']['sex'].count()
print("Somatório de Homens:", somatorio_homens)
print("Somatório de Mulheres:", somatorio_mulheres)