# IO COM STREAMING (ELE VAI LENDO E IMPRIMINDO NA TELA)

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}' .format(*registro.split(',')).strip())

except IndexError:
    pass

finally:
    print('Fim.')
    arquivo.close()

# STRIP TIRA A LINHA PULADA ATOA
# SPLIT TRANSFORMA A STRING REGISTRO EM LISTA, OU SEJA, PALAVRAS COM INDICES
