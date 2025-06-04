from produto import Produto
from estoque import Estoque

def main():
    estoque = Estoque()

    p1 = Produto(1, "Caneta", 100, 1.5)
    p2 = Produto(2, "Caderno",  50, 10.0)

    estoque.adicionar_produto(p1)
    estoque.adicionar_produto(p2)

    print("Lista de produtos em estoque")
    estoque.listar_produtos()

if __name__=="__main__":
    main()    