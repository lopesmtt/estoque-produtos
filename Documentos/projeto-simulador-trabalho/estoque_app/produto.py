
class Produto:
    def __init__(self, id: int, nome: str, quantidade: int, preco: float):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    def __repr__(self):
        return(f"Produto(id={self.id}, nome='{self.nome}',"
               f"quantidade={self.quantidade}, preco={self.preco:.2f})")    