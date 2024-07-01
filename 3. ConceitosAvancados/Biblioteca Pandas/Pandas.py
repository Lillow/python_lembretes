'''Pandas é uma biblioteca poderosa para análise de dados em python, 
oferecendo estruturas de dados flexíveis e ferramentas para manipulação e 
análise de dados numéricos e tabulares. '''
# 1. Instalação

# Para instalar o Pandas, use o seguinte comando:

# bash

# pip install pandas

# 2. Estruturas de Dados Principais
# Series

# Uma série é um objeto unidimensional semelhante a uma matriz, lista ou coluna em uma tabela.

import pandas as pd

# Criar uma série a partir de uma lista
s = pd.Series([1, 3, 5, 7, 9])
print(s)

# DataFrame

# Um DataFrame é uma estrutura de dados tabular semelhante a uma planilha do Excel, com colunas nomeadas que podem conter diferentes tipos de dados.



import pandas as pd

# Criar um DataFrame a partir de um dicionário
data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35],
        'Cidade': ['Rio de Janeiro', 'São Paulo', 'Recife']}
df = pd.DataFrame(data)
print(df)

# 3. Carregamento e Armazenamento de Dados
# Carregar Dados de Arquivos

# Pandas suporta a leitura e escrita de diversos formatos de arquivo, como CSV, Excel, HDF5, SQL, JSON, entre outros.



import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('dados.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Escrever Dados em Arquivos



import pandas as pd

# Criar um DataFrame
data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35],
        'Cidade': ['Rio de Janeiro', 'São Paulo', 'Recife']}
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_salvos.csv', index=False)

# 4. Exploração e Manipulação de Dados
# Informações Básicas



import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('dados.csv')

# Informações básicas sobre o DataFrame
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Seleção de Dados



# Selecionar uma coluna
print(df['Nome'])

# Selecionar várias colunas
print(df[['Nome', 'Idade']])

# Selecionar linhas com base em uma condição
print(df[df['Idade'] > 30])

# Adicionar e Remover Colunas



# Adicionar uma nova coluna
df['Novo'] = [True, False, True]

# Remover uma coluna
df.drop('Novo', axis=1, inplace=True)

# Agrupamento e Agregação



# Agrupar por uma coluna e calcular a média de outra
print(df.groupby('Cidade')['Idade'].mean())

# 5. Limpeza de Dados
# Tratamento de Valores Nulos



# Verificar valores nulos
print(df.isnull().sum())

# Preencher valores nulos com a média da coluna
df['Idade'].fillna(df['Idade'].mean(), inplace=True)

# Remoção de Dados Duplicados



# Remover linhas duplicadas
df.drop_duplicates(inplace=True)

# 6. Visualização de Dados

# Pandas permite integração com bibliotecas de visualização como Matplotlib e Seaborn para criar gráficos diretamente a partir dos DataFrames.
# 7. Operações Avançadas
# Concatenação de DataFrames



# Concatenar DataFrames verticalmente
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
result = pd.concat([df1, df2])
print(result)

# Junção de DataFrames



# Juntar DataFrames baseado em uma chave
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'C': [7, 8, 9]})
result = pd.merge(df1, df2, on='A')
print(result)

# Transformações de Dados



# Aplicar uma função a cada elemento de uma coluna
df['Idade'] = df['Idade'].apply(lambda x: x * 2)

# 8. Análise de Séries Temporais
# Manipulação de Datas



# Converter uma coluna para o tipo de data
df['Data'] = pd.to_datetime(df['Data'])

# Extrair componentes de data (dia, mês, ano)
df['Dia'] = df['Data'].dt.day
df['Mês'] = df['Data'].dt.month
df['Ano'] = df['Data'].dt.year

# 9. Integração com SQL

# Pandas suporta leitura e escrita direta de DataFrames para bancos de dados SQL através de SQLAlchemy.
# 10. Otimização de Desempenho

# Pandas oferece métodos para otimização de desempenho, como o uso de Cython ou vetorização de operações.
# 11. Manipulação Avançada de Dados

# Pandas permite a aplicação de funções complexas e manipulações avançadas de índices e hierarquias.
# 12. Exportação de Relatórios

# Pandas pode ser usado para gerar relatórios diretamente a partir de DataFrames formatados.