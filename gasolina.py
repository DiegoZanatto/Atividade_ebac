import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Atividade_ebac/gasolina.csv')
#df
sns.lineplot(data=df, x='dia', y='venda')

plt.savefig('grafico.png')