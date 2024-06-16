'''
Todo método Python tem self como primeiro parâmetro.
A palavra reservada representa o objeto em si, portanto, 
sempre que quisermos especificar atributos de objetos, 
devemos associá-lo à palavra reservada self.
'''
class MinhaClasse: # Classe
    def __init__(self,atributo1, atributo2): # Método construtor
        
        self.atributo1 = atributo1 # Atributos
        self.atributo2 = atributo2

        '''
        Na linguagem Python não é recomendável 
        criar mais de um Método Construtor para a classe.
        '''
