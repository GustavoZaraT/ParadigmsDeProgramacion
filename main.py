from aplicacion.banco.cliente_bancario import ClienteBancario

try:
    cliente = ClienteBancario("Jaime Andrade","Hernandez Sanchez",28,0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
except Exception as e:
    print("Error: " + str(e))

try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error: "+str(ex))
