class Pessoa:
    def metodo1(self, idade, nome, mensagem):
        self.nome = nome
        self.idade = idade
        self.mensagem = mensagem

# CRIANDO NOVOS OBJETOS (PESSOAS DIFERENTES)
p1 = Pessoa()
p2 = Pessoa()
p1.nome = 'João'
p2.nome = 'Maria'
p1.idade = 22
p2.idade = 26
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
p1.sobrenome = 'Marques'
print(p1.sobrenome)

# IMPRIMINDO EM FORMA DE DICIONÁRIO
print(p1.__dict__)