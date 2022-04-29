with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}' .format(*registro.split(',')).strip())

if arquivo.closed:
    print('\nArquivo foi fechado.')