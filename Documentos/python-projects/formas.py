from abc import ABC, abstractmethod
import math 

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2
    def perimetro(self):
        return 2 * math.pi * self.raio

formas = [Retangulo(4, 5), Circulo(3), Retangulo(2, 7)]

for forma in formas:
    print(f"Area: {forma.area():.2f}")
    print(f"Perimetro: {forma.perimetro}")
    print(f"----------")
            
