### LISTAS QUE IREI TRABALHAR ###
dado = list()
pessoas = list()
pesototal = list()

### ESTRUTURA DE REPETIÇÃO INFINITA
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    
### CONDIÇÃO DE SAÍDA DA ESTRUTURA DE REPETIÇÃO ###
    resp = str(input('Deseja continuar? [S/N]\n')).upper()
    if resp == 'n' or resp == 'N':
        break

### TRABALHANDO COM FOR IN ###
for var_peso in pessoas: #Adicionei à nova variável var_peso todos os pesos da lista "PesoTotal" (referente ao indice [1])
    pesototal.append(var_peso[1])
    
for var_MinMax in pessoas: #Criei uma variável com o maior e menor número da lista "PesoTotal"
    maiorpeso = max(pesototal)
    menorpeso = min(pesototal)


print(f'Ao todo, você cadastrou {len(pessoas)} pessoa(s).')
print(f'O maior peso foi {maiorpeso}')
print(f'O menor peso foi {menorpeso}')