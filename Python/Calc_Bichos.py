dogs=[
    [8, 'Chanel'],
    [2, 'Cristal'],
    [1, 'Tobias'],
    [3, 'Teodoro'],
    [0.5,'Medusa'],
    [0.5,'Odin'],
]

for numero, nome in dogs:
    print(f'''Tem {numero} anos e se chama {nome}''')

print('--'*5, 'QUANTOS ANOS MEU BICHO TERÁ?', '--'*5)
ano = 2022
nome = str(input('Qual Nome do Bicho? '))
anoNovo = int(input('Qual o ano posterior? '))
idadeVelha = int(input('Qual idade atual do bicho? '))
idadeNova = idadeVelha + (anoNovo - ano)
if ano != anoNovo:
    print(f'''O {nome} tinha {idadeVelha} em {ano} e em {anoNovo} terá {idadeNova}.''')