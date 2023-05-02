#Crie uma classe abstrata chamada "Pokemon" com atributos como nome, tipo, saúde, ataque, defesa e velocidade.
#Implemente um método abstrato chamado "atacar" que recebe outro objeto "Pokemon" e calcula o dano com
#base na diferença entre o ataque do atacante e a defesa do defensor.
# Crie pelo menos duas subclasses concretas da classe "Pokemon" com valores diferentes para os atributos.
from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self, name, ):