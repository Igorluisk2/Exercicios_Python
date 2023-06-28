import pandas as pd
dataframe=pd.DataFrame()
print(dataframe)

tabela_vendas=pd.read_excel("Vendas.xlsx")
print(tabela_vendas)
print(tabela_vendas.shape)
print(tabela_vendas.head())
print(tabela_vendas.describe())
print(tabela_vendas.loc[:])