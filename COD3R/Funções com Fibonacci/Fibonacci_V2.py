# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'''{penultimo}, {ultimo}''', end=', ')
    continua = 0
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(f'''{ultimo}''', end=', ')

if __name__ == "__main__":
    fibonacci(50)