
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = i * resultado
        return resultado

print(fatorial(8))
