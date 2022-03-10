class Pessoa(object):
    olhos = 2
    def __init__(self, *filhos,nome=None, idade=1):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

jose = Pessoa()
maria = Pessoa()
print(jose.olhos)

# USANDO  AS INSTÂNCIAS QUE JÁ EXISTEM
maria.nome = 'Maria Cristina'
jose.nome = 'José Paulo'
jose.idade='40'
maria.idade='55'
print(jose.nome)

# ADICIONANDO INSTÂNCIAS DINAMICAMENTO (ATRIBUTOS DE INSTÂNCIA DINÂMICO)
jose.sobrenome = 'Carvalho'
print(jose.sobrenome)

# EXIBINDO UMA INSTÂNCIA COMO DICIONÁRIO
print(jose.__dict__)
print(maria.__dict__)