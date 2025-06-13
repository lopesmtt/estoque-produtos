import math

class Forma():
    def area(self):
        return 0
    
class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio **2)

formas = [
    Retangulo(4, 5),
    Circulo(3),
    Retangulo(2, 7)
]                   
for  forma in formas:
    print(f"Area da forma: {forma.area():.2f}") 