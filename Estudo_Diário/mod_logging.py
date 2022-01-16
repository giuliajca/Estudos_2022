import logging

logging.basicConfig(level = logging.DEBUG,
                    filename='erros.log',
                    filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('E-mail:\n')
    senha = int(input('Senha:\n'))

    if senha == 123:
        print('Logado com sucesso!')
        logging.info(f'{email} entrou.') # ARMAZENA O EMAIL NO ERROS.TXT
        logging.info(senha), # ARMAZENA A SENHA NO ERROS.TXT

except ValueError:
    print('Digite apenas números.')
    logging.info(ValueError)