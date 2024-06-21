'''
Todo método Python tem self como primeiro parâmetro.
A palavra reservada representa o objeto em si, portanto, 
sempre que quisermos especificar atributos de objetos, 
devemos associá-lo à palavra reservada self.
'''
class MinhaClasse: # Classe
    def __init__(self, atributo1, atributo2): # Método construtor
        
        self.atributo = 0# Atributo public 
        self._atributo_protected = atributo1 # Atributo protected
        self.__atributo_private = atributo2 # Atributo private

    def get_atributo_protected(self): # get 
        return self._atributo_protected
        
    def set_atributo_protected(self, atributo_protected): # set
        self._atributo_protected = atributo_protected

    @property # Decorator Property
    def atributo_private(self):    # get
        return self.__atributo_private
    
    @atributo_private.setter
    def atributo_private(self, atributo): # set
        self.__atributo_private = atributo
    
    '''
    Em Python, não é considerada uma boa prática criar uma classe e, 
    logo em seguida, adicionar propriedades (property) para todos os atributos.
    
    A função Property deve ser utilizada somente se você precisar 
    da funcionalidade de transformar ou verificar um atributo 
    quando ele é atribuído ou lido.
    '''

    '''
    def
    Na linguagem Python não é recomendável 
    criar mais de um Método Construtor para a classe.
    '''
