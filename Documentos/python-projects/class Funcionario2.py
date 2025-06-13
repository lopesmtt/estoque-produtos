class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return 0

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20
    
class Vendedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10    

funcionarios = [
    Gerente("Joao", 5000),
    Vendedor("Maria", 3000),
    Gerente("Carlos", 7000),
    Vendedor("Ana", 3500)
]           
for f in funcionarios:
    print(f"{f.nome} recebera  um bonus de R${f.calcular_bonus():.2f}")