import math

def fatorial(n: int) -> int:
    resultado: int = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado

def sen(x: float, n: int) -> float:
    resultado: float = 0
    for i in range(n):
        resultado += ((-1)**i * x**(2*i + 1)) / (fatorial(2*i + 1))
    return resultado

def cos(x: float, n: int) -> float:
    resultado: float = 0
    for i in range(n):
        resultado += ((-1)**i * x**(2*i)) / (fatorial(2*i))
    return resultado

print(cos(1, 10))
print(math.cos(1))