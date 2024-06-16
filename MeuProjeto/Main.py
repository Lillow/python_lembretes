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

meuObjeto = MinhaClasse('Atributo1', 'Atributo2') # instanciando um objeto

print(f'Atributo 1: {meuObjeto.atributo1}\nAtributo 2: {meuObjeto.atributo2}')