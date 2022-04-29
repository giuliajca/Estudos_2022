cachorros = ['Maia','Cristal'] # LISTA
gatos = ('Tobias','Medusa','Odin') # TUPLA
print('Lista:', cachorros)
print('Tupla:', gatos)

# Acrescentando mais um item à lista de cachorros [ ]
cachorros.append('Teodoro')
print('Acrescentado à Lista com Append:', cachorros)

# Acrescentando mais um item à tupla de cachorros ( )
# gatos.append('Felix') -> Neste caso não é possível pois tuplas são imutáveis.

# Gerando um Range de X a Y em N vezes range(x,y,n).
print('-'*10)
print('Lista:', list(range(6,10,2)))
print('Tupla:', tuple(range(6,10,2)))
