
class Carro:
    frase = "Alocando o 1º Objeto Estático na Memória."

    def __init__(self, frase02):
        self.frase02 = frase02

instancia = Carro('Instanciando o 1º Objeto Dinâmico na memória.')
print(instancia.frase) # Alocando o 1º Objeto Estático na Memória.
print(instancia.frase02) # Instanciando o 1º Objeto Dinâmico na memória.

# HERANÇA
class Vendas(Carro):
    def __init__(self):
        pass
print(instancia.frase) #Alocando o 1º Objeto Estático na Memória.
