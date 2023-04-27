#Crie uma classe chamada Animal com as propriedades nome e idade.
#Em seguida, crie uma classe Cachorro que herde de Animal e adicione a propriedade raca.
#Crie um objeto Cachorro e exiba suas propriedades na tela.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cachorro(Animal):
    def __init__(self, name, age, breed):
        Animal.__init__(self, name, age)
        self.breed = breed


dog = Cachorro('Lilika', 5, 'Pastor Alemão')
print(vars(dog))