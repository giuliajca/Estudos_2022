import time

def title (txt):
    print('-=-'*15)
    print(txt)
    print('-=-'*15)

title('Contagem de 1 até 10 de 1 em 1')

# FUNÇÃO
def contador (inicio, fim, passo):
    print(f'Contador selecionado: de {inicio} até {fim} de {passo} em {passo}.')

#Corrigindo o Passo Negativo
    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(f'{contador}', end=' ', flush=True) # FLUSH PARA DESLIGAR O BUFFER.
            contador += passo
            time.sleep(0.4)
        print('Fim!')
    else:
        while contador >= fim:
            print(f'{contador}', end=' ', flush=True) # FLUSH PARA DESLIGAR O BUFFER.
            contador -=passo
        print('Fim!')
        
contador(1, 5, 1) #Dados do Contador

i = abs(int(input('Inicio: ')))
f = abs(int(input('Fim: ')))
p = abs(int(input('Passo: ')))

contador(i, f, p)