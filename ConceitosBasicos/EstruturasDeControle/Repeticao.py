# para (for)
# Itera sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string):

# Iterando sobre uma lista
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Iterando sobre uma string
for letra in "":
    print(letra)

# for com range()
# Usado para gerar uma sequência de números:
# De 0 a 4
for i in range(5):
    print(i)

# De 1 a 5
for i in range(1, 6):
    print(i)

# De 0 a 10 com passo 2
for i in range(0, 11, 2):
    print(i)

# enquanto (while)
# Repete um bloco de código enquanto a condição for verdadeira:

# Contando de 0 a 4
contador = 0
while (contador < 5):
    print(contador)
    contador += 1

# quebra (break)
# Sai do loop imediatamente:

# Encontrar e parar no número 3
for i in range(10):
    if i == 3:
        break
    print(i)

# continue
# Pula o restante do bloco e vai para a próxima iteração:

# Pulando o número 3
for i in range(5):
    if i == 3:
        continue
    print(i)

# else em Loops
# Executa um bloco de código quando o loop termina normalmente (sem break):

# Sem encontrar o número 3
for i in range(5):
    print(i)
else:
    print("Loop terminou normalmente")

# Com `break`
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Isso não será impresso porque o loop terminou com break")

# while com else
# Similar ao for-else, mas para loops while:

contador = 0
while (contador < 5):
    print(contador)
    contador += 1
else:
    print("Loop terminou normalmente")

# Com `break`
contador = 0
while (contador < 5):
    if contador == 3:
        break
    print(contador)
    contador += 1
else:
    print("Isso não será impresso porque o loop terminou com break")

# Estruturas de Controle Combinadas
# for dentro de while

# Combinação de ambos os tipos de loops:
i = 0
while (i < 3):
    for j in range(3):
        print(f"i={i}, j={j}")
    i += 1

# while dentro de for
# Combinação de ambos os tipos de loops:
for i in range(3):
    j = 0
    while j < 3:
        print(f"i={i}, j={j}")
        j += 1