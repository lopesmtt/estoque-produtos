class ContaBancaria():
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    def set_titular(self, novo_titular):
        self.__titular =  novo_titular


conta = ContaBancaria("Joao", 1000)

conta.depositar(500)

conta.sacar(300)

conta.sacar(2000)

print("Titular: ", conta.get_titular())
print("Saldo atual: ", conta.get_saldo())

conta.set_titular("Maria")
print("Novo titular: ", conta.get_titular())