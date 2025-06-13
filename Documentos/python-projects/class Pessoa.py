class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
         super().__init__(nome, idade)        
         self.salario = salario
class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
         super().__init__(nome, idade, salario)       
         self.departamento = departamento
    
    def mostrar_dados(self):
        print(f"Nome:{self.nome}")
        print(f"Idade: {self.idade} anos.")
        print(f"Salario: R${self.salario}")
        print(f"Departamento: {self.departamento}")

g = Gerente("Maria", 33, 9000, "Financeiro")
g.mostrar_dados()        

        