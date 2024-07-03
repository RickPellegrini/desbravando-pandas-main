# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

# dados = {"nome":["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}


# %%
import pandas as pd



# %%
dados = {'nome':['rick','matts','gins','gui'],'idade':[26,40,29,200]}
pd.Series(dados)
df = pd.DataFrame(dados)

sumario = df.describe()
sumario

# sumario de cada coluna
# media da coluna idade
# ultimo nome da coluna nome


# %%
df['idade'].mean()


# %%

df['nome'].describe()

df['nome'].iloc[-1]

df.to_csv ('Amigos.csv', sep=';')