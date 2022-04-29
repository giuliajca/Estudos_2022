
def fibonacci(quantidade):
    lista = [0, 1]
    for _ in range(0, quantidade):
        lista.append(sum(lista[-2:]))
    return lista

if __name__ == "__main__":
    print(fibonacci(20))
