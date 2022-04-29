linguas = {'Português' : 'PT-BR', 'Inglês Britânico' : 'EN-BR', 'Inglês Americano' : 'EN-AM'}

for key, values in linguas.items():
    print(f'''{key} : {values}''')

linguas.get('br', 'Não definida.')
