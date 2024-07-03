# %%
import pandas as pd

# %%

data = {
    'nome': ['rick','matts','gins','gui'],
    'sobrenome':['calvo','calvinho','calvao','calvudo'],
    'idade':[26,300,27,40]
    }


data['idade'][0]

# %%

df = pd.DataFrame(data)
df

# %%
df['idade'].iloc[0]



# %%

df['sobrenome'].iloc[0]


# %%
df.iloc[0]
# %%
df.index

# %%
df.columns
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%

df['peso'] = [30,60,90,50]

sumario = df.describe()
# %%
df.head(2)
# %%
df.tail(2)