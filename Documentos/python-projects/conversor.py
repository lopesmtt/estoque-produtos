def celsius_para_fahrenheit(c):
    return(c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def fahrenheit_para_kelvin(f):
    c = fahrenheit_para_celsius(f)
    return celsius_para_fahrenheit(c)

def kelvin_para_fahrenheit(k):
    c = kelvin_para_celsius(k)
    return celsius_para_fahrenheit(c)

def conversor():
    print("Conversor de Temperatura")
    print("Unidades disponiveis: Celsius(C), Fahrenheit(F), Kelvin(K)")

    unidade_origem = input("Digite a unidade de origem (C/F/K): ").upper()
    temp = float(input("Digite a temperatura a converter: "))
    unidade_destino = input("Digite a unidade para converter (C/F/K)").upper()

    if unidade_origem == unidade_destino:
        print(f"A temperatura permanece a mesma: {temp} {unidade_destino}")
        return
    
    if unidade_origem == "C" and unidade_destino == "F":
        resultado = celsius_para_fahrenheit(temp)
    elif unidade_origem == "F" and unidade_destino == "C":    
        resultado = fahrenheit_para_celsius(temp)
    elif unidade_origem == "C" and unidade_destino == "K":
        resultado = celsius_para_kelvin(temp)
    elif unidade_origem == "K" and unidade_destino == "C":
        resultado = kelvin_para_celsius(temp)
    elif unidade_origem == "F" and unidade_destino =="F":
        resultado = kelvin_para_fahrenheit(temp)
    else:
        print("Unidade invalida. Tente novamente.")
        return
    print(f"{temp} {unidade_origem} equivalem a {resultado: .2f} {unidade_destino}") 
                  
conversor()                  
