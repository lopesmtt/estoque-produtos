def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

lista = [8, 7.5, 10, 6]
print(calcular_media(lista))