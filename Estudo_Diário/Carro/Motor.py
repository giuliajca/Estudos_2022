class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        velocidade = self.velocidade + 1

    def frear(self):
        velocidade = self.velocidade - 1


