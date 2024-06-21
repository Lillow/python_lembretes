# 1. Entrada Simples

# Ler uma string do usuário:
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

# 2. Entrada e Conversão de Tipos

# Ler e converter a entrada para um tipo específico:

# Ler um número inteiro
idade = int(input("Quantos anos você tem? "))
print(f"Você tem {idade} anos.")

# Ler um número de ponto flutuante
altura = float(input("Qual é a sua altura em metros? "))
print(f"Sua altura é {altura} metros.")

#3. Entrada com Manipulação de Strings

# Ler e manipular a string:
texto = input("Digite algo: ")
print(f"Em maiúsculas: {texto.upper()}")
print(f"Em minúsculas: {texto.lower()}")

# 4. Uso em Cálculos

# Ler valores e utilizá-los em cálculos:
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma é: {soma}")

# 5. Entrada com Listas

# Ler múltiplos valores e armazená-los em uma lista:
valores = input("Digite vários valores separados por espaço: ").split()
print(f"Valores: {valores}")

# 6. Uso com Estruturas de Controle

# Ler valores e utilizar em estruturas de controle:
idade = int(input("Quantos anos você tem? "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 7. Repetição e Acumulação

# Ler valores em um loop:
soma = 0
for _ in range(3):
    valor = int(input("Digite um número: "))
    soma += valor
print(f"A soma dos números é: {soma}")

# 8. Tratamento de Erros

# Ler valores com tratamento de erros:
try:
    idade = int(input("Quantos anos você tem? "))
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Por favor, digite um número válido.")

# 9. Validação de Entrada

# Validar a entrada do usuário:
while True:
    nome = input("Qual é o seu nome? ")
    if nome.isalpha():
        break
    else:
        print("Por favor, digite um nome válido.")
print(f"Olá, {nome}!")

# 10. Usando input() com F-Strings

# Ler valores e usar f-strings diretamente:
nome = input(f"Digite o seu nome: ")
idade = int(input(f"Digite a sua idade, {nome}: "))
print(f"{nome}, você tem {idade} anos.")

# 11. Customização de Mensagens de Entrada

# Usar diferentes tipos de mensagens para orientar o usuário:
print("Bem-vindo ao nosso sistema!")
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
print(f"Olá, {usuario}. Sua senha foi registrada.")