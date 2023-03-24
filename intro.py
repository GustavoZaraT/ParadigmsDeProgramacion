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
# 
#
