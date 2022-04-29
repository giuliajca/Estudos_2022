# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'''{penultimo}, {ultimo}''', end=', ')
    continua = 0
    while continua < limite:
        continua = ultimo + penultimo
        print(f'''{continua}''', end=', ')
        penultimo = ultimo
        ultimo = continua

if __name__ == "__main__":
    fibonacci(50)