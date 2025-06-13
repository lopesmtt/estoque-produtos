from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class  CartaoCredito(MetodoPagamento):
    def __init__(self, nome_cartao):
        self.nome_cartao = nome_cartao

    def pagar(self, valor):
        print(f"Pagamento de R${valor:.2f} realizado com o cartao: {self.nome_cartao}.")

class Paypal(MetodoPagamento):
    def __init__(self, email):
        self.email = email
    def pagar(self, valor):
        print(f"Pagamento de R${valor:.2f} Realizado via Paypal com a conta: {self.email}.")    


def processar_pagamentos(metodos, valor):
    for metodo in metodos:
        metodo.pagar(valor)

pagamentos = [
    CartaoCredito("Mastercard - Joao"),
    Paypal("Joao@email.com")
]                        
processar_pagamentos(pagamentos, 150.75)