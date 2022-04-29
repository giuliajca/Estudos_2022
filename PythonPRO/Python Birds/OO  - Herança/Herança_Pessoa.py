class Pessoa:
    def metodo1(self, idade, nome, mensagem):
        self.nome = nome
        self.idade = idade
        self.mensagem = mensagem


class Homem(Pessoa):
    pass

# CRIANDO NOVOS OBJETOS (PESSOAS DIFERENTES)
p1 = Pessoa()
p2 = Pessoa()

# MESMA COISA DA INSTANCIAÇÃO ACIMA /\ \/
p1 = Homem()
p2 = Homem()

p1.nome = 'João'
p2.nome = 'Maria'
p1.idade = 22
p2.idade = 26
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
p1.sobrenome = 'Marques'
print(p1.sobrenome)

print('Nome do módulo: ', __name__)
