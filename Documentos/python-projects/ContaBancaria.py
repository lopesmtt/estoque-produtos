class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo}")

# 🧪 Testando a classe
conta = ContaBancaria("Maria", 1000)
conta.exibir_saldo()

conta.depositar(500)
conta.exibir_saldo()

conta.sacar(200)
conta.exibir_saldo()

conta.sacar(2000)  # Tentativa de saque acima do saldo
