''' ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN

'''
#~~~~~~~~~~~~~~~~~~~~~~~
#/*Operaciones básicas*/
#~~~~~~~~~~~~~~~~~~~~~~~
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5) #sqrt
print (10%2)
print(10%0.1) #exclusivo de python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Para saber el tipo del objeto se usa type*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
t=0
print(type(t)) #int
t=3.6
print(type(t)) #float
t=True
print(type(t)) #bool

#~~~~~~~~~~~~~~~~~~~~~~
#/*Mensaje a pantalla*/
#~~~~~~~~~~~~~~~~~~~~~~
print("Este es un comando de python. ", "Este es otro enunciado.", t)
print('id: ', 1)
print('First Name: ', 'Steve')
print('Last Name', 'Jobs')
print("vamos a sumar esto " + "con esto otro")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Continuar una instruccion en varios renglones*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if 100 > 99 and \
        200<= 300 and \
        True != False:
            print('Hello World!')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Comandos diferentes en la misma línea*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Hola "); print("tu!!") #Se considera mala practica >:(

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Usando paréntesis redondos, cuadrados o llaves se puede escrivir en varios renglones*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
print(list)
print(matriz)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Identación estricta parea procesos dependientes de : (dos puntos)*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if 10>5:
    print("diez es mayor que cinco")
    print("otra identación")
for i in list:
    print(i)
    print("ok")
if 10>5
    print("vredadero")
    if 10<20:
        print("verdadero")
elif 5>3 # comienza segundo condicional
    print ("esto no se imprimiria")
else:
    print ("aquí nunca llega")

#~~~~~~~~~~~~~
#/*Funciones*/
#~~~~~~~~~~~~~
def say_hello(name):
    print("Hello", name)
    print("Welcome to Python Tutorials")

say_hello("ZaraT")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Input permite obtener datos del usuario de prompter*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nombre = input("Dame tu nombre: ")
print("Hola como estás", nombre)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Los enteros son de presición ilimitada*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
y = 50000000000000000000000000000000000
print(y)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Se pueden delimitar números con guión bajo pero no con coma*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
y = 5_000_000
print(y)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*La función int() cambia srings y floats a enteros*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numero = int(input("Dame tu edad: "))
type(numero)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*La notación cinetifíca de flotantes utiliza e o E*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*1.2 x 10^{-9}*/
#~~~~~~~~~~~~~~~~~
y = 1.2E-09
print(y)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*La funcion float() convierte strings y enteros a floats*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
y  = float("14.3")
print(y)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Los complejos se escriben con la raíz de menos uno
#  j siempre con un numero como prefijo
#  no acepta j suelta*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
z= 1+1j

# suma +
# resta -
# multiplicación *
# división /
# módulo %
# exponente **
# // función piso
# Funciones para transformar números int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159, 4))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*String de varias líneas*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
parrafo = """ En el bosque de la china
    la chunita de perdio """
print(parrafo)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*La función len() obtiene el tamaño de string*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n=len(parrafo)
print(n)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Las letras en un string ocupan lugares como en un arreglo*/
#((tambien de atrás para adelante comenzando en -1 el último))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
palabra = "hola"
print(palabra[0])
print(palabra[-4])

#~~~~~~~~~~~~~~~~~~~~~~
#/*Conjunto en python*/
#~~~~~~~~~~~~~~~~~~~~~~
even_num = {2, 4, 6, 8, 10} # conjunto de números pares
print(even_num)

# El bool no es parte del conjunto
wmp = {1, 'Steve', 10.5, True} # conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*Convertir secuencia a conjunto*/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#/*No lo genera en orden*/
#~~~~~~~~~~~~~~~~~~~~~~~~~
s = set('Hello')
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

su = s1|s2 # Unión
print(su)

si = s1 &s2 # Intersección
print(si)

#~~~~~~~~~~~~~~~~~~~~~~~
#/*Uso de diccionarios*/
#~~~~~~~~~~~~~~~~~~~~~~~
capitals = {"USA" : "Washington D.C.", "France" : "Paris", "India" : "New Delhi"}
print(capitals)

#~~~~~~~~~~~~~~~~~
#/*llave : valor*/
#~~~~~~~~~~~~~~~~~

#diccionario vacío
d = {}
