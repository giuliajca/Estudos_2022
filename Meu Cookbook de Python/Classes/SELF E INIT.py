class Carro(object):

    variavel_estatica = "Essa é uma variável estática, existe 1 em toda a memória."

    # CRIANDO VARIÁVEIS DINÂMICAS (VÁRIAS INSTÂNCIAS NA MEMÓRIA).
    def __init__(self, estado, cor, motor, conversivel):
        # VARIÁVEIS DINÂMICAS
        self.estado = "usado"
        self.cor = cor
        self.motor = motor
        self.conversivel = True

peugeot_206 = Carro(estado = 'Novo', cor = 'Preto', motor = 1.4, conversivel = False)
ranger = Carro(estado = 'Semi-Novo',cor = 'Preto', motor = 3.1, conversivel = False)
saveiro = Carro(estado = 'Semi-Novo',cor = 'Prata', motor = 1.8, conversivel = False)
ferrari = Carro('novo','vermelho',4.5,True) # MESMA COISA DO ANTERIOR

# IMPRIMINDO UM TERMO
print(peugeot_206.cor) # PRETO
print(ferrari.cor) # VERMELHO
print(Carro.variavel_estatica)