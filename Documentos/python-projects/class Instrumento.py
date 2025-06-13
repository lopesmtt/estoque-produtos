class Instrumento():
    def tocar(self):
        print("Som generico de instrumento.")

class Violao(Instrumento):
    def tocar(self):
        print("Tocando acordes de violao...")

class Piano(Instrumento):
    def tocar(self):
        print("Tocando notas de piano...") 

class Bateria(Instrumento):
    def tocar(self):
        print("Tocando ritmo de bateria...") 

banda = [
    Violao(),
    Piano(),
    Bateria(),
    Violao()
]                               

for instrumento in banda:
    instrumento.tocar()