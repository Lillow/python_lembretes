# 1. Variáveis

# Declaração e uso de variáveis:
x = 5       # Variável inteira
y = 3.14    # Variável float
nome = "João"  # Variável string
flag = True  # Variável booleana
print(x, y, nome, flag)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 2. Tipos de Dados Básicos

#Inteiros (int)
# Representam números inteiros:
idade = 25
print(type(idade))  # <class 'int'>

# Ponto Flutuante (float)
# Representam números decimais:
altura = 1.75
print(type(altura))  # <class 'float'>

#Strings (str)
# Representam texto:
mensagem = "Olá, mundo!"
print(type(mensagem))  # <class 'str'>

#Booleanos (bool)
# Representam valores verdadeiros ou falsos:
verdadeiro = True
falso = False
print(type(verdadeiro))  # <class 'bool'>

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 3. Conversão de Tipos

# De String para Inteiro:
numero_str = "10"
numero_int = int(numero_str)
print(type(numero_int))  # <class 'int'>

# De Inteiro para Float:
numero_int = 10
numero_float = float(numero_int)
print(type(numero_float))  # <class 'float'>

# De Float para String:
numero_float = 10.5
numero_str = str(numero_float)
print(type(numero_str))  # <class 'str'>

# De Booleano para Inteiro:
booleano = True
numero_int = int(booleano)
print(type(numero_int))  # <class 'int'>

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 7. Tipagem Dinâmica

# Mudança de tipo de variável:
variavel = 5
print(type(variavel))  # <class 'int'>
variavel = "Agora sou uma string"
print(type(variavel))  # <class 'str'>

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 8. Variáveis Globais e Locais

# Variáveis Locais:
# Definidas dentro de uma função e só acessíveis ali:
def minha_funcao():
    x = 10  # Variável local
    print(x)

minha_funcao()
# print(x)  # Isso causará um erro

# Variáveis Globais:
# Definidas fora de funções e acessíveis em todo o código:
x = 10  # Variável global

def minha_funcao():
    print(x)

minha_funcao()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#  9. Variáveis com None

# Representa ausência de valor:
nada = None
print(type(nada))  # <class 'NoneType'>