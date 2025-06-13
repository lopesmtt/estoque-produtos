class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo

    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, novo_salario):
        self.__salario = novo_salario  
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            print("Salario invalido. Deve ser maior que 0.")      

    def get_cargo(self):
        return self.__cargo
    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    def aplicar_aumento(self, percentual):
        if percentual > 0:
            aumento = self.__salario *  (percentual / 100)
            self.__salario += aumento
        else:
            print("Percentual invalido.")

    def exibir_dados(self):
        print(f"Nome:{self.__nome}" )
        print(f"Cargo: {self.__cargo}")
        print(f"Salario: {self.__salario: .2f}") 


func = Funcionario("Carlos", 4000.00, "Analista")

func.exibir_dados()

print("\nAplicando  aumento  de 10%")
func.aplicar_aumento(10)

func.exibir_dados()

func.set_salario(-500)

