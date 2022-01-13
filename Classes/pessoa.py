class Pessoa:
    def __init__(self, nome = None, idade=22): # DUNDER INIT
        # ATRIBUTOS DE OBJETO
        self.nome = nome # DIGO QUE O ATRIBUTO EXISTE, MAS NÃO TEM NENHUM VALOR ARMAZENADO NELE.
        self.idade = idade
        
    def ola(self):
        return 'Hello World Ethan!'


# Importando a Classe
# from Classes.pessoa import Pessoa
# Chamando a Classe: p = Pessoa()

# TESTANDO
if __name__ == "__main__":
    p = Pessoa('Ethan Marques')
    print(Pessoa.ola(p))
    print(p.ola())
    print(p.nome)
