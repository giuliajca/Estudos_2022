# FUNÇÃO FEMEA OU MACHO
n = input('Digite seu nome: ')
gender = input('Você é F ou M?')

if gender == 'F':
    def olaf(nome):
        return f'Olá minha querida amiga {nome}.'
    print(olaf(n))
else:
    def olam(nome):
        return f'Olá meu querido amigo {nome}.'
    print(olam(n))
