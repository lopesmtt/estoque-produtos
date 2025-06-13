class Veiculo():
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_info(self):
        print(f"Marca:{self.marca}")
        print(f"Ano: {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def exibir_infor(self):
        super().exibir_info()
        print(f"Portas: {self.portas}") 

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir_info(self):
        super().exibir_info()  
        print(f"Cilindradas: {self.cilindradas}cc") 

c1 = Carro("Toyota", 2022, 4)
m1 = Moto("Honda", 2020, 150)    

print("Carro:")
c1.exibir_info()

print("\nMoto:")
m1.exibir_info()