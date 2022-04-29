# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8

def fibonacci(limite):
    lista = [0, 1]
    while lista[-1] < limite:
        lista.append(sum(lista[-2:])) # INDICE NEGATIVO (2 ÚLTIMOS ELEMENTOS)
        print(f'''{lista}''')


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
