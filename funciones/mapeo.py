def alcuadrado(x):
    return x*x

def alcubo(x):
    return x*x*x

def mapeo(func, lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado, [1,2,3,4,5,6,7,8])
cubos = mapeo(alcubo, [1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)

def en_mayusculas(texto):
    return texto.upper()

def en_minusculas(texto):
    return texto.lower()

def saludar(func):
    print(func("Hola, ¿Que tal?"))

saludar(en_mayusculas)
saludar(en_minusculas)

def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo

division = divisor(2)
print(division(3))

temps = [("Berlin",29),("Cairo",36),("Buenos Aires",19),("Los Angeles",26),("Tokyo",27),("Nueva York",28),("Londres",22),("Pekin",32),("Mexico Tenochtitlan",23)]

C_a_F = lambda datos: (datos[0], (9/5)*datos[1] + 32)
print(list(map(C_a_F, temps)))
