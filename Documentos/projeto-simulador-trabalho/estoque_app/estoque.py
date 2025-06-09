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


    def entrada_produto(self, id_produto, quantidade):
        for produto in self.produtos:
            if produto.id == id_produto:
                produto.quantidade += quantidade
                print(f"Entrada: {quantidade} unidades adicionadas & '{produto.nome}'")
                return
            print("Produto nao encontrado.")


    def saida_produto(self, id_produto, quantidade):
        for produto in self.produtos:
            if produto.id == id_produto:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    print(f"Saida: {quantidade} unidades removidas do produto'{produto.nome}'")
                else:
                    print(f"Erro: Estoque insuficiente  para o produto '{produto.nome}'")
                    return
                print("Produto nao encontrado.")            

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

    def buscar_por_id(self, id_produto):
        for produto in self.produtos:
            if produto.id == id_produto:
                return produto

        return None
    def buscar_por_nome(self, nome):
        encontrados = [p for p in self.produtos if nome.lower() in p.nome.lower()]
        return encontrados

    def relatorio_estoque_baixo(self, limite):
        produtos_baixos = [p for p in self.produtos if p.quantidade < limite]
        if not produtos_baixos:
            print(f"Nenhum produto com estoque abaixo de {limite} unidades.")
        else:
            print(f"Produtos  com estoque abaixo  de {limite} unidades:")
            for p in  produtos_baixos:
                print(p)



if __name__ == "__main__":
    estoque = Estoque()
    estoque.carregar_de_arquivo()

    print("\n--- Produtos carregados ---")
    estoque.listar_produtos()

    print("\n--- Buscando produto por ID 1 ---")
    produto = estoque.buscar_por_id(1)
    print(produto if produto else "Produto não encontrado.")

    print("\n--- Buscando produto por nome 'caderno' ---")
    resultado = estoque.buscar_por_nome("caderno")
    if resultado:
        for p in resultado:
            print(p)
    else:
        print("Nenhum produto encontrado com esse nome.")

    print("\n--- Relatório de estoque baixo (< 60 unidades) ---")
    estoque.relatorio_estoque_baixo(60)                