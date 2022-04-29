numeros = [[], []]
valor = 0

for i in range(0, 8):
    valor = int(input('Digite o valor {}:\n' .format(i)))
    
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares são {numeros[0]}')
print(f'Os valores ímpares são {numeros[1]}')