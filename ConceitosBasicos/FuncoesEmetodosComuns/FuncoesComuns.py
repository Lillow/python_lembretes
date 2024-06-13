# Funções para Strings:
texto = "python"
print(texto.upper())  # PYTHON
print(texto.lower())  # python
print(texto.capitalize())  # Python
print(texto.find("th"))  # 2
print(texto.replace("py", "Py"))  # Python

# Funções para Listas:
numeros = [4, 2, 9, 1]
numeros.sort()  # Ordenar lista
numeros.reverse()  # Reverter lista
print(numeros)

# Funções para Dicionários:
dados = {"nome": "Ana", "idade": 22}
print(dados.keys())  # Chaves
print(dados.values())  # Valores
print(dados.items())  # Pares chave-valor

#
print(type(dados)) # Pegar o tipo do objeto