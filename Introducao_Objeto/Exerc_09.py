#Crie uma classe chamada "Retangulo" que tenha como atributos "largura" e "altura".
#Adicione métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return (self.altura * self.largura) / 2

    def perimetro(self):
        return (2*self.largura) + (2*self.altura)


retangulo = Retangulo(4, 7)
print(retangulo.area())
print(retangulo.perimetro())