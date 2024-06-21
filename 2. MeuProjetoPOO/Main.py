'''
A classe Main não possui atributos.
Utilizamos apenas a palavra reservada pass.
'''
class Main:
    pass

from MinhaClasse import MinhaClasse
'''
e a palavra reservada import é a referência 
de qual classe será utilizada para a 
criação de objetos em um arquivo à parte.
'''

meu_objeto = MinhaClasse('Atributo protegido', 'Atributo privado') # instanciando um objeto

print(f'Atributo 1: {meu_objeto.get_atributo_protected()}\nAtributo 2: {meu_objeto.atributo_private}')

meu_objeto.atributo = 'Atributo público'
meu_objeto.atributo_private = 'Atributo private alterado'