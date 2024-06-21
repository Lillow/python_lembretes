# 1. Abertura e Fechamento de Arquivos
# open()

# Abre um arquivo, retornando um objeto de arquivo. Pode-se especificar o modo de abertura:

    # 'r':  Abre o arquivo somente para leitura. O arquivo deve já existir.
    # 'r+': Abre o arquivo para leitura e escrita. O arquivo deve já existir. A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.
    # 'w':  Abre o arquivo somente para escrita, no início do arquivo. Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
    # 'w+':	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
    # 'a':  Abre o arquivo para escrita no final do arquivo. Não apaga o conteúdo preexistente.
    # 'a+':	Abre o arquivo para escrita no final do arquivo e leitura.
    # 'b':  modo binário
    # 't':  modo texto (padrão)
    # 'x':  criação exclusiva (falha se o arquivo já existir)

# Abrir um arquivo para leitura
arquivo = open('exemplo.txt', 'r')

# Fechar o arquivo
arquivo.close()

# Context Manager (with)

# Abre e fecha o arquivo automaticamente:



with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Arquivo é fechado automaticamente aqui

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 2. Leitura de Arquivos
# read()

# Lê o arquivo inteiro:



with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# readline()

# Lê uma linha do arquivo:



with open('exemplo.txt', 'r') as arquivo:
    linha = arquivo.readline()
    print(linha)

# readlines()

# Lê todas as linhas e retorna uma lista:



with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 3. Escrita em Arquivos
# write()

# Escreve uma string no arquivo:



with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Esta é uma nova linha.\n")

# writelines()

# Escreve uma lista de strings no arquivo:



linhas = ["Linha 1\n", "Linha 2\n", "Linha 3\n"]
with open('exemplo.txt', 'w') as arquivo:
    arquivo.writelines(linhas)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 4. Anexar em Arquivos
# append

# Abre um arquivo para anexar conteúdo:



with open('exemplo.txt', 'a') as arquivo:
    arquivo.write("Esta linha será anexada.\n")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 5. Manipulação de Arquivos Binários
# Leitura e Escrita Binária



# Escrita binária
with open('imagem.jpg', 'wb') as arquivo:
    arquivo.write(b'conteudo binario')

# Leitura binária
with open('imagem.jpg', 'rb') as arquivo:
    conteudo = arquivo.read()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 6. Manipulação de Arquivos CSV

# Usando a biblioteca csv para ler e escrever arquivos CSV:
# Leitura de CSV



import csv

with open('dados.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# Escrita em CSV



import csv

dados = [
    ['Nome', 'Idade'],
    ['João', 30],
    ['Maria', 25]
]

with open('dados.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 7. Manipulação de Arquivos JSON

# Usando a biblioteca json para ler e escrever arquivos JSON:
# Leitura de JSON



import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)

# Escrita em JSON



import json

dados = {
    'nome': 'João',
    'idade': 30
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 8. Outros Métodos Úteis
# tell()

# Retorna a posição atual do cursor no arquivo:



with open('exemplo.txt', 'r') as arquivo:
    print(arquivo.tell())

# seek()

# Move o cursor para uma posição específica:



with open('exemplo.txt', 'r') as arquivo:
    arquivo.seek(10)
    conteudo = arquivo.read()
    print(conteudo)

# truncate()

# Reduz o tamanho do arquivo:



with open('exemplo.txt', 'w') as arquivo:
    arquivo.truncate(10)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 9. Manipulação de Arquivos com os e shutil

# Usando as bibliotecas os e shutil para operações avançadas de arquivos e diretórios:
# Verificar Existência



import os

print(os.path.exists('exemplo.txt'))  # True ou False

# Renomear Arquivo



import os

os.rename('exemplo.txt', 'novo_exemplo.txt')

# Remover Arquivo



import os

os.remove('novo_exemplo.txt')

# Copiar Arquivo



import shutil

shutil.copy('exemplo.txt', 'copia_exemplo.txt')

# Mover Arquivo



import shutil

shutil.move('exemplo.txt', 'novo_diretorio/exemplo.txt')

# Criar Diretório



import os

os.mkdir('novo_diretorio')

# Remover Diretório



import os

os.rmdir('novo_diretorio')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 10. Manipulação de Arquivos Temporários

# Usando a biblioteca tempfile para criar arquivos temporários:



import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Teste de arquivo temporario')
    temp.seek(0)
    conteudo = temp.read()
    print(conteudo)