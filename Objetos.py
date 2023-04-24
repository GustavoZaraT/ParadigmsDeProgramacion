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

class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d

    def perimetro(mi):
        p = mi.lado1 + mi.lado2 +mi.lado3 + mi.lado4
        print("perimetro = ", p)
        return p

class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)

class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

cuadrado1 = Cuadrado(5)

perimetro1 = cuadrado1.perimetro()

area1 = cuadrado1.area()

print("Perimetro = ", perimetro1)
print("Área = ", area1)

class A:
    __a: float = 0.0
    __b: float = 0.0
    __c: float = 0.0

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

class B:
    __d: float = 0.0
    __e: float = 0.0

    def __init__(self, d: float, e: float):
        self.d = d
        self.e = e

    def sumar_todo(self, aa: float, bb: float):
        x: float = self.d + self. e + aa + bb
        return x

objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)
print(objetoB.sumar_todo(objetoA.a, objetoA.b))

class C:
    __d: float = 0.0
    __e: float = 0.0
    __Aa: A = None

    def __init__(self, d: float, e: float):
        self.d = d
        self.e = e
        self.Aa = A(1.0, 2.0, 3.0)

    def sumar_todo(self):
        x: float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

objetoC = C(4.0, 5.0)
print(objetoC.sumar_todo())

class D:
    __d: float = 0.0
    __e: float = 0.0
    __Aa: A = None

    def __init__(self,d: float, e: float, Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x: float = self.d +self.e + self.Aa.a +self.Aa.b
        return x

objetoD = D(4.0, 5.0, objetoA)
print(objetoD.sumar_todo())
