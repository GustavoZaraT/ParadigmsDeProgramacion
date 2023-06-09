from functools import lru_cache

def fibonacci_lento(n):
    if n==1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacci_lento(n-1)+fibonacci_lento(n-2)

for i in range(1, 36):
    print(str(i) + ": ", fibonacci_lento(i))

fibonaccis = {}
def fibonacci(n):
    if n in fibonaccis:
        return fibonaccis[n]
    
    if n == 1:
        fibonaccis[n] = 1
    elif n == 2:
        fibonaccis[n] = 1
    elif n > 2:
        fibonaccis[n] = fibonacci(n-1) + fibonacci(n-2)

    return fibonaccis[n]

for i in range(1, 10001):
    print(str(i) + ": ", fibonacci(i))

@lru_cache(maxsize =  3)
def nfibonacci(n):
    if type(n) != int:
        raise TypeError("n debe de ser entero positivo")
    if n<1:
        raise ValueError("n debe de ser entero positivo")

    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return nfibonacci(n-1) + nfibonacci(n-2)

for i in range(1, 10001):
    print(str(i) + ": ", nfibonacci(i))
