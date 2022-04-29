# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8

def fibonacci(quantidade, sequencia=(0,1)):
    if len(sequencia == quantidade):
        return sequencia
    return fibonacci(quantidade, sequencia)

