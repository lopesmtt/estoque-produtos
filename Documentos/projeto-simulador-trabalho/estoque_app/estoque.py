import json
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
            for produto in self.produtos:
                print(produto)            

    def cadastrar_produto(self, id_produto, nome, quantidade, preco):
        produto = Produto(id_produto, nome, quantidade, preco)
        self.produtos.append(produto)

    def salvar_em_arquivo(self, nome_arquivo ="produtos.json"):
        produtos_dict = [p.__dict__ for p in self.produtos]
        with open(nome_arquivo, "w") as f:
            json.dump(produtos_dict, f, indent=4)

    def carregar_de_arquivo(self, nome_arquivo="produtos.json"):
        try:
            with open(nome_arquivo, "r") as f:
                produtos_dict = json.load(f)
                self.produtos = [Produto(**p) for p in produtos_dict]
        except FileNotFoundError:
            # Arquivo ainda não existe, inicia com lista vazia
            self.produtos = []