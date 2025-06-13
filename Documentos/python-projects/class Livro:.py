class Livro:
    def  __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def get_titulo(self):
        return self.__titulo 

    def get_autor(self):
        return self.__autor 

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"O livro '{self.__titulo} foi emprestado.")
        else:
            print(f"O livro '{self.__titulo} nao esta disponivel para emprestimo.")
    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"O livro '{self.__titulo} foi devolvido")
        else:
            print(f"O livro '{self.__titulo} ja esta disponivel.")

    def esta_disponivel(self):
        return self.__disponivel
livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
print(f"Titulo: {livro1.get_titulo()}")
print(f"Autor: {livro1.get_autor()}") 

print("Disponivel:", livro1.esta_disponivel())

livro1.emprestar()
livro1.devolver()
print("Disponivel?", livro1.esta_disponivel())

        
        