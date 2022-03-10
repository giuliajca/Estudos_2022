pessoas = ['Maia','Medusa','Odin']

def pessoa_aprovada(pessoa):
	if pessoa == 'Maia':
		return True

# Aqui eu chamo meu filtro e a função que irá filtrar.
# filter(pessoa_aprovada,pessoas)

# Aqui eu converto meu filtro em uma lista
# list(filter(pessoa_aprovada,pessoas))

# Aqui eu imprimi convertido na tela.
print(list(filter(pessoa_aprovada,pessoas)))