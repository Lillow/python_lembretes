# se (if)
# A estrutura condicional mais básica, que executa um bloco de código se a condição for verdadeira:
x = 10
if x > 5:
    print("x é maior que 5")

# se-senão (if-else)
# Adiciona uma alternativa para quando a condição não é verdadeira:
x = 3
if x > 5:
    print("x é maior que 5")
else:
    print("x é menor ou igual a 5")

# se-senãose-senão (if-elif-else)
# Permite múltiplas condições:
x = 7
if x > 10:
    print("x é maior que 10")
elif x > 5:
    print("x é maior que 5, mas menor ou igual a 10")
else:
    print("x é menor ou igual a 5")

# if Aninhado
# Permite condições dentro de condições:
x = 15
if x > 10:
    if x > 20:
        print("x é maior que 20")
    else:
        print("x é maior que 10, mas menor ou igual a 20")
else:
    print("x é menor ou igual a 10")

# if em uma linha (Operador Ternário)
# Sintaxe compacta para decisões simples:
x = 5
resultado = "x é maior que 10" if x > 10 else "x é 10 ou menor"
print(resultado)