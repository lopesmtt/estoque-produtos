from produto import Produto

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            for p in self.produtos:
                print(p)            