import statistics

bigdata = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print(promedio)

print(list(filter(lambda x: x > promedio, bigdata)))

paises = ["", "Argentina", "", "Brasil", "", "Chile", "México", "", "Colombia", "", "", "Cuba", "Venezuel"]

print(list(filter(None, paises)))
