from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, placa, preco_base):
        self.__modelo = modelo
        self.__placa = placa
        self.__preco_base = preco_base

    def get_modelo(self):
        return self.__modelo
    
    def get_placa(self):
        return self.__modelo
    
    def get_preco_base(self):
        return self.__preco_base

    @abstractmethod
    def calcular_preco(self, dias):
        pass

class Carro(Veiculo):
    def __init__(self, modelo, placa, preco_base, portas):
        super().__init__(modelo, placa, preco_base)
        self.__portas = portas

    def calcular_preco(self, dias):
        return self.get_preco_base() * dias + 50

class Moto(Veiculo):
    def __init__(self, modelo, placa, preco_base, cilindradas):
        super().__init__(modelo, placa, preco_base)        
        self.__cilindradas = cilindradas

    def calcular_preco(self, dias):
        return self.get_preco_base() * dias 

class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
class Locadora:
    def __init__(self, nome):
        self.__nome = nome    
        self.__veiculos_disponiveis = []

    def adicionar_veiculo(self, veiculo):
        self.__veiculos_disponiveis.append(veiculo)

    def listar_veiculos(self):
        for v in self.__veiculos_disponiveis:
            print(f"Modelo: {v.get_modelo()}| Placa: {v.get_placa()} | Preço base/dia: R$ {v.get_preco_base()}")

    def alugar(self, cliente, veiculo, dias):
        preco_total = veiculo.calcular_preco(dias)
        print(f"\nCliente: {cliente.get_nome()} alugou {veiculo.get_modelo()} por {dias} dias.")
        print(f"Preço total: R${preco_total:.2f}")      

locadora = Locadora("RapidoCar")

carro1 = Carro("Fiat", "ABC123", 100, 4)
moto1 = Moto("Honda Titan","XZY333", 50, 150 )

locadora.adicionar_veiculo(carro1)
locadora.adicionar_veiculo(moto1)

print("🚘 Veiculos disponiveis: ")
locadora.listar_veiculos()

cliente1 = Cliente("Maria")

locadora.alugar(cliente1, carro1, 3)

locadora.alugar(cliente1, moto1, 2)