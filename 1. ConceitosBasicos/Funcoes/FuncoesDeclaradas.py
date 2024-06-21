# 1. Definindo Funções
# Função Simples

# Uma função sem parâmetros e sem retorno:
def saudacao():
    print("Olá, mundo!")

saudacao()  # Chamando a função

# Função com Parâmetros
# Uma função que aceita argumentos:
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")

# Função com Retorno
# Uma função que retorna um valor:
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # 7

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 2. Tipos de Argumentos
# Argumentos Posicionais

# Argumentos passados na ordem correta:
def multiplica(a, b):
    return a * b

resultado = multiplica(2, 3)
print(resultado)  # 6

# Argumentos Nomeados (Keyword Arguments)
# Argumentos passados pelo nome:
def dividir(a, b):
    return a / b

resultado = dividir(b=4, a=8)
print(resultado)  # 2.0

# Argumentos Padrão (Default Arguments)
# Argumentos com valores padrão:
def saudacao(nome="Mundo"):
    print(f"Olá, {nome}!")

saudacao()  # Olá, Mundo!
saudacao("Alice")  # Olá, Alice!

# Argumentos Variáveis (Arbitrary Arguments)
# Argumentos variáveis usando *args e **kwargs:

# *args para número variável de argumentos posicionais
def soma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(soma(1, 2, 3))  # 6

# **kwargs para número variável de argumentos nomeados
def dados_pessoais(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="João", idade=30, cidade="São Paulo")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 3. Tipos de Funções
# Funções Lambda (Funções Anônimas)

# Funções curtas sem nome, usadas para operações simples:



# Sintaxe: lambda argumentos: expressão
dobro = lambda x: x * 2
print(dobro(5))  # 10

# Lambda em uma função de ordem superior
lista = [1, 2, 3, 4]
lista_dobrada = list(map(lambda x: x * 2, lista))
print(lista_dobrada)  # [2, 4, 6, 8]

# Funções Aninhadas

# Funções definidas dentro de outras funções:
def pai():
    print("Esta é a função pai.")

    def filho():
        print("Esta é a função filho.")

    filho()

pai()

# Funções como Argumentos

# Passar funções como argumentos para outras funções:
def aplicar(funcao, valor):
    return funcao(valor)

resultado = aplicar(lambda x: x ** 2, 5)
print(resultado)  # 25

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 4. Retornando Funções

# Funções que retornam outras funções:
def saudacao_personalizada(saudacao):
    def mensagem(nome):
        return f"{saudacao}, {nome}!"
    return mensagem

bom_dia = saudacao_personalizada("Bom dia")
print(bom_dia("João"))  # Bom dia, João!

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 5. Funções Recursivas

# Funções que chamam a si mesmas:
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # 120

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 6. Decoradores

# Funções que modificam o comportamento de outras funções:
def decorador(funcao):
    def wrapper():
        print("Algo antes da função")
        funcao()
        print("Algo depois da função")
    return wrapper

@decorador
def saudacao():
    print("Olá!")

saudacao()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 7. Funções de Ordem Superior

# Funções que recebem outras funções como argumentos ou retornam funções:
def saudacao():
    return "Olá"

def executa(func):
    print(func())

executa(saudacao)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 8. Anotações de Tipo

# Indicam os tipos esperados dos parâmetros e do valor de retorno:
def soma(a: int, b: int) -> int:
    return a + b

print(soma(2, 3))  # 5

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 9. Funções com Documentação

# Adicionando docstrings para documentar funções:
def soma(a, b):
    """
    Soma dois números.

    Args:
    a (int): O primeiro número.
    b (int): O segundo número.

    Returns:
    int: A soma de a e b.
    """
    return a + b

print(soma.__doc__)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 10. Funções Geradoras

# Usando yield para retornar um gerador:
def contador(max):
    n = 0
    while n < max:
        yield n
        n += 1

for num in contador(5):
    print(num)