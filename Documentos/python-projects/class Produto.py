class Produto():
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome):
        self.__novo_nome = novo_nome 
    def get_preco(self):
        return self.__preco
    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("Preço invalido. Deve  ser maior que  0.")

    def get_quantidade(self):
        return self.__quantidade
    def set_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Quantidade  invalida. Nao pode ser negativa.")

    def valor_total_em_estoque(self):
        return self.__preco * self.__quantidade                        

produto = Produto("Notebook", 3000.00, 5)

print("Nome:", produto.get_nome())
print("Preço:", produto.get_preco() )
print("Quantidade:", produto.get_quantidade())
print("Valor total em estoque: ", produto.valor_total_em_estoque())

produto.set_preco(-100)
produto.set_quantidade(-5)

produto.set_preco(3200.00)
produto.set_quantidade(6)

print("Novo Preço:", produto.get_preco())
print("Nova quantidade:", produto.get_quantidade())
print("Novo valor total:", produto.valor_total_em_estoque())