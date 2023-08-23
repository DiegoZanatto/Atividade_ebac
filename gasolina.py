import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

dados = [
    ["dia", "venda"],
    [1, 5.11],
    [2, 4.99],
    [3, 5.02],
    [4, 5.21],
    [5, 5.07],
    [6, 5.09],
    [7, 5.13],
    [8, 5.12],
    [9, 4.94],
    [10, 5.03]
]

nome_arquivo = "gasolina.csv"

with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)




gasolina_df = pd.read_csv('gasolina.csv')
gasolina = sns.lineplot(data=gasolina_df, x="dia", y="venda")
plt.savefig('gasolina.png', dpi=300)