class ObjetoVacio:
    pass

nada = ObjetoVacio()
print(type (nada))

class Llanta:
    cuenta = 0
    def __init__(mi, radio=50, ancho=30, presión=1.5):
        Llanta.cuenta += 1
        mi.radio = radio
        mi.ancho = ancho
        mi.presión =presión

llanta1 = Llanta(50, 30, 1.5)
llanta2 = Llanta(presión = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)

class Coche:
    def __init__(mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4


micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta)
print("Presión de la llanta 4 = ", llanta4.presión)
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta1.presión)

class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamo a ponerme nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamó a obener_nombre')
        return mi.__nombre
    nombre=property(obtener_nombre, ponerme_nombre)

estudiante = Estudiante()

estudiante.nombre = "Ivan"

print(estudiante.nombre)
