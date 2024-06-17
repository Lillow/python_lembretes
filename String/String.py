# 1. Criação de Strings
# Strings Simples

string1 = "Olá, mundo!"
string2 = ' é incrível!'

#Strings Múltiplas Linhas

string_multilinhas = """Esta é uma string
de múltiplas linhas."""

# Strings com Caracteres de Escape

string_com_escapes = "Linha 1\nLinha 2\tCom tabulação"



# 2. Operações Básicas com Strings
# Concatenação

saudacao = "Olá"
nome = "João"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)  # Olá, João!

# Repetição

repetida = "Ha" * 3
print(repetida)  # HaHaHa

# Comprimento da String

tamanho = len("")
print(tamanho)  # 6



# 3. Acesso a Caracteres e Fatiamento
# Acesso a Caracteres

string = ""
primeiro_caractere = string[0]
print(primeiro_caractere)  # P

#Fatiamento

string = ""
sub_string = string[1:4]
print(sub_string)  # yth

# Outros exemplos de fatiamento
print(string[:3])  # Pyt
print(string[3:])  # hon
print(string[-1])  # n
print(string[::2])  # Pto
print(string[::-1])  # nohtyP



# 4. Métodos de String
# Alteração de Caso

string = ""
print(string.upper())  # 
print(string.lower())  # 
print(string.capitalize())  # 
print(string.title())  # 
print(string.swapcase())  # 

# Verificação de Conteúdo

string = "123"
print(string.isalpha())  # False
print(string.isdigit())  # False
print(string.isalnum())  # True
print(string.isspace())  # False
print(" ".isspace())  # True

# Pesquisa e Substituição

string = "Olá, mundo!"
print(string.find("mundo"))  # 5
print(string.index("mundo"))  # 5
print(string.replace("mundo", ""))  # Olá, !
print(string.count("o"))  # 2

# Divisão e Junção

string = "um,dois,três"
lista = string.split(",")
print(lista)  # ['um', 'dois', 'três']

string = " ".join(lista)
print(string)  # um dois três

# Remoção de Espaços

string = " Olá, mundo! "
print(string.strip())  # "Olá, mundo!"
print(string.lstrip())  # "Olá, mundo! "
print(string.rstrip())  # " Olá, mundo!"

# Checagem de Prefixo/Sufixo

string = ""
print(string.startswith("Py"))  # True
print(string.endswith("on"))  # True



# 5. Formatação de Strings
# Interpolação de Variáveis (f-strings)

nome = "João"
idade = 30
print(f"Meu nome é {nome} e eu tenho {idade} anos.")  # Meu nome é João e eu tenho 30 anos.

# Método format()

print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))  # Meu nome é João e eu tenho 30 anos.
print("Meu nome é {1} e eu tenho {0} anos.".format(idade, nome))  # Meu nome é João e eu tenho 30 anos.
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade))  # Meu nome é João e eu tenho 30 anos.

# Substituição com %

print("Meu nome é %s e eu tenho %d anos." % (nome, idade))  # Meu nome é João e eu tenho 30 anos.



# 6. Strings com Estruturas de Dados
# Lista de Strings

lista = ["", "é", "incrível"]
print(" ".join(lista))  #  é incrível

# Iteração sobre Strings

string = ""
for char in string:
    print(char)



# 7. Funções Úteis
# len()

#Retorna o comprimento da string:

string = ""
print(len(string))  # 6

# ord() e chr()

# Converte caracteres para seus valores Unicode e vice-versa:

print(ord('A'))  # 65
print(chr(65))  # A



# 8. Codificação e Decodificação
# Codificação de Strings

string = "Olá, mundo!"
string_bytes = string.encode('utf-8')
print(string_bytes)  # b'Ol\xc3\xa1, mundo!'

#Decodificação de Strings

string_decodificada = string_bytes.decode('utf-8')
print(string_decodificada)  # Olá, mundo!



# 9. Strings e Expressões Regulares

# Usando o módulo re para manipulação avançada de strings:


import re

string = "O número de telefone é 123-456-7890"
padrao = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(padrao, string)
if resultado:
    print(resultado.group())  # 123-456-7890



# 10. Strings Multilíngues
# Manipulação de Strings Unicode



string = u"Olá, mundo!"
print(string)  # Olá, mundo!



# 11. Comparação de Strings
# Comparação Simples



print("" == "")  # False
print("".lower() == "".lower())  # True

# Comparação Lexicográfica



print("apple" < "banana")  # True
print("apple" > "banana")  # False



# 12. Métodos Específicos
zfill()

# Preenche a string com zeros à esquerda:



print("42".zfill(5))  # 00042

expandtabs()

# Expande tabulações na string:



print("1\t2\t3".expandtabs(4))  # 1   2   3