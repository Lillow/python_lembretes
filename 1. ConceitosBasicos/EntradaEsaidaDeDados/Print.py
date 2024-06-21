# 1. Simples

# Imprimir uma string simples:
print("Olá, mundo!")

# Imprimir múltiplos argumentos:
print("Olá,", "mundo!")

# 2. Variáveis

# Imprimir o valor de uma variável:
nome = "João"
print(nome)

# 3. Formatação de Strings

# Usando a concatenação:
idade = 25
print("Eu tenho " + str(idade) + " anos.")

# Usando a vírgula (automático adiciona espaço):
idade = 25
print("Eu tenho", idade, "anos.")

# Usando o operador %:
nome = "João"
idade = 25
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))

# Usando o método str.format():
nome = "João"
idade = 25
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Usando f-strings (a partir do Python 3.6):nome = "João"
idade = 25
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

#4. Caracteres Especiais

# Quebra de linha:
print("Linha 1\nLinha 2")

# Tabulação:
print("Coluna 1\tColuna 2")

# 5. Argumentos da Função print()

# Alterar o separador padrão:
print("Python", "é", "legal", sep="-")

# Alterar o caractere de fim de linha:
print("Isso está na mesma linha.", end=" ")
print("Mesmo aqui.")

# Escrever a saída para um arquivo:
with open("output.txt", "w") as f:
    print("Essa saída vai para o arquivo.", file=f)

# 6. Utilização com Coleções

# Imprimir listas, tuplas e dicionários:
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
dicionario = {"nome": "João", "idade": 25}
print(lista)
print(tupla)
print(dicionario)

# 7. Funções Avançadas

# Imprimir utilizando expressão lambda:
x = lambda a, b: a + b
print(x(5, 6))

# Imprimir utilizando comprehensions:
quadrados = [x**2 for x in range(5)]
print(quadrados)

# 8. Encadeamento de Prints

# Imprimir múltiplas vezes na mesma linha:
for i in range(5):
    print(i, end=' ')


