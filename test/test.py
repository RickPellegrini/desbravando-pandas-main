# %%
import pandas as pd

# Carregar o DataFrame
df_2017_faturamento = pd.read_csv('C:\\Users\\rick_\\OneDrive\\Desktop\\desbravando-pandas-main\\data\\_faturamento.csv', sep=';')

# Função para limpar e converter os valores
def clean_and_convert_column(df, colunas):
    for coluna in colunas:
        # Garantir que todos os valores são tratados como strings
        df[coluna] = df[coluna].astype(str)
        
        # Remover o símbolo 'R$'
        df[coluna] = df[coluna].str.replace('R\$', '', regex=True)
        
        # Remover espaços em branco extras
        df[coluna] = df[coluna].str.strip()
        
        # Substituir pontos dos separadores de milhares por nada
        df[coluna] = df[coluna].str.replace('.', '', regex=False)
        
        # Substituir vírgula por ponto
        df[coluna] = df[coluna].str.replace(',', '.', regex=False)
        
        # Converter a coluna para valores numéricos, lidando com erros
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

       
        # Preencher NaN com um valor adequado, aqui estamos usando 0
        df[coluna] = df[coluna].fillna(0).astype(int)
        
    
    return df

print("Antes de limpar os dados e converter para numérico:")
print(df_2017_faturamento)

# Liste as colunas que precisam de processamento
colunas = ['Quantia', 'Taxa do Anfitrião', 'Taxa de Limpeza']

# Aplicar a função no DataFrame
df_2017_faturamento = clean_and_convert_column(df_2017_faturamento, colunas)

# Exibir o DataFrame após processamento
print("\nApós limpar os dados e converter para numérico:")
df_2017_faturamento


# %%
df_2017_faturamento[['Noites','Quantia']]

df = df_2017_faturamento.sort_values(by = 'Quantia', ascending=False, inplace=True)


df_2017_faturamento
# %%

df_2017_faturamento.sort_values (by = 'Quantia', 
                                ascending=False, inplace=True)

df_2017_faturamento[['Noites','Quantia']]
df_2017_faturamento


df_2017_faturamento['Ratio'] = df_2017_faturamento['Quantia'] / df_2017_faturamento['Noites']
df_2017_faturamento
# %%
df_2017_faturamento[['Noites','Quantia']]
# %%
df_2017_faturamento['Ratio'] = df_2017_faturamento['Quantia'] / df_2017_faturamento['Noites']
df_2017_faturamento[['Noites','Quantia','Ratio']]
