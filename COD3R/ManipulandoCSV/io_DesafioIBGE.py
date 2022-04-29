# <?xml version='1.0' encoding='ISO-8859-1' ?>
import time
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as iniciar:  # ABRINDO UM ARQUIVO
        print('Baixando o CSV...')
        # ARMAZENANDO OS DADOS, LENDO E DECODIFICANDO
        dados = iniciar.read().decode('latin1')
        print('Baixado.')

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
