import pandas as pd
import matplotlib.pyplot as plt
# Importando as bibliotecas necessárias para o desenvolvimento da análise de dados

df = pd.read_csv(r"/home/jorge/Documentos/GitHub/ETEPD_AD/II_Bimestre/Desafio_I/dentistasphabitante2011.csv")
# Importando lista de dados de uma tabela.

valores = df.values
colunas = df.columns
# Verificando valores das colunas.

# df.Municípios = df.Municípios.astype("category")

maiores = df.query('Dentistasphabitante > 0.85').head(10)
print(maiores)
# Selecionando os Municípios com as maiores taxas de dentista por mil habitantes

plt.figure(figsize=(16, 12))
plt.bar(maiores["Municípios"], maiores["Dentistasphabitante"])
# Gráfico de barras(Figure_1)
# plt.plot(maiores["Municípios"], maiores["Dentistasphabitante"], "o")
# Gŕafico de pontos(Figure_2)

plt.xlabel("Munícipios")
plt.ylabel("Dentistas por mil habitantes")
plt.title("Dentistas por habitantes no estado de Alagoas")
# Gerando as etiquetas do gráfico.

plt.show()
# Mostrando o gráfico
