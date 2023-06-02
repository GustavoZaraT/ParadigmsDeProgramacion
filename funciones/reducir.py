from functools import reduce

bigdata = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

multiplicar = lambda x, y: x*y

print(reduce(multiplicar, bigdata))
