from class_introdução import Carro

# INSTANCIANDO A CLASSE (ARMAZENANDO OS DADOS DA CLASSE EM UMA VARIÁVEL).
carro01 = Carro('Peugeot', '206', '2001', 'Prata')
print(f'O carro é um {carro01.marca}, {carro01.modelo} do ano {carro01.ano} e na cor {carro01.cor}.')

carro02 = Carro()
carro02.marca = str(input('Qual marca?\n'))
carro02.modelo = str(input('Qual modelo?\n'))
carro02.ano = int(input('Qual ano?\n'))
carro02.cor = str(input('Qual cor?\n'))
print(f'O carro é um {carro02.marca}, {carro02.modelo} do ano {carro02.ano} e na cor {carro02.cor}.')
