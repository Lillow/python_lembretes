# 1. Anotação de Variáveis

# Anotação de tipo para variáveis
idade: int = 25
nome: str = "Alice"
altura: float = 1.75
ativo: bool = True

# 2. Anotação de Funções
#Parâmetros e Retorno

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

# Parâmetros opcionais (default)
def adicionar(x: int, y: int = 0) -> int:
    return x + y

# Anotação de uma função sem retorno explícito
def imprimir_mensagem(mensagem: str) -> None:
    print(mensagem)



# 3. Tipos Compostos
#Listas e Dicionários



from typing import List, Dict

# Listas
nomes: List[str] = ["Alice", "Bob", "Charlie"]

# Dicionários
idades: Dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}

# Tuplas e Conjuntos



from typing import Tuple, Set

# Tuplas
pessoa: Tuple[str, int, float] = ("Alice", 25, 1.75)

# Conjuntos
valores_unicos: Set[int] = {1, 2, 3, 4, 5}

# 4. Tipos Genéricos e Any
# Qualquer Tipo (Any)



from typing import Any

# Variável que pode ser de qualquer tipo
variavel: Any = "Pode ser qualquer coisa"

# 5. Union e Optional
# Union

from typing import Union

# Variável que pode ser de múltiplos tipos
resposta: Union[str, int] = "Sim"
resposta = 42

Optional



from typing import Optional

# Variável que pode ser do tipo especificado ou None
telefone: Optional[str] = None

# 6. Callable
# Funções como Primeiro Cidadão



from typing import Callable

# Função que recebe outra função como parâmetro
def aplicar_funcao(funcao: Callable[[int, int], int], a: int, b: int) -> int:
    return funcao(a, b)

def somar(x: int, y: int) -> int:
    return x + y

resultado = aplicar_funcao(somar, 2, 3)  # resultado será 5

# 7. Classes e Objetos
# Tipos de Classe



class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

p: Pessoa = Pessoa("Alice", 25)

# Métodos de Classe



class Circulo:
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def area(self) -> float:
        return 3.14 * self.raio * self.raio

# 8. Tipos Literais
# Literal



from typing import Literal

# Variável que pode ter um valor específico
direcao: Literal['cima', 'baixo', 'esquerda', 'direita'] = 'cima'

# 9. Tipos Avançados
# TypedDict



from typing import TypedDict

class PessoaDict(TypedDict):
    nome: str
    idade: int

pessoa: PessoaDict = {"nome": "Alice", "idade": 25}

Protocol



from typing import Protocol

class Voavel(Protocol):
    def voar(self) -> None:
        ...

class Pato:
    def voar(self) -> None:
        print("Pato voando")

def faz_voar(animal: Voavel) -> None:
    animal.voar()

pato = Pato()
faz_voar(pato)  # Pato voando

#10. Anotação de Tipos no  3.9 e Superior
#List, Dict, Tuple e Set Nativos



# Listas
nomes: list[str] = ["Alice", "Bob", "Charlie"]

# Dicionários
idades: dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}

# Tuplas
pessoa: tuple[str, int, float] = ("Alice", 25, 1.75)

# Conjuntos
valores_unicos: set[int] = {1, 2, 3, 4, 5}

# 11. Tipo Self
# Usado em Métodos de Classe para Anotação do Tipo da Própria Classe



from typing import Self

class Node:
    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.proximo: Optional[Node] = None

    def set_proximo(self, proximo: Self) -> None:
        self.proximo = proximo

# 12. Forward References
# Referências a Tipos Antes de Sua Definição



from __future__ import annotations

class Nodo:
    def __init__(self, valor: int, proximo: Nodo | None = None) -> None:
        self.valor = valor
        self.proximo = proximo

# 13. PEP 563 e PEP 649: Anotações de Tipo Postergadas
# Utilização de Strings para Anotar Tipos



from __future__ import annotations

def f(x: "int") -> "int":
    return x