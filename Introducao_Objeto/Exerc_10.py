#Crie uma classe chamada "Circulo" que tenha como atributo "raio".
#Adicione métodos para calcular a área e o perímetro do círculo.
from math import pi

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return f'A área é {round(pi * (self.raio**2),2)}cm²'

    def perimetro(self):
        return f'O perimetro é {round((pi*2) * self.raio, 2)}cm'


bola = Circulo(3)
print(bola.area())
print(bola.perimetro())