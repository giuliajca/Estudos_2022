import time

def title (txt):
    print('-=-'*15)
    print(txt)
    print('-=-'*15)

title('Contagem de 1 até 10 de 1 em 1')


for c in range(0, 3):
    print(c)
    time.sleep(0.4)
print('FIM!')

def contador(i, f, p):
    for c2 in range(inicio, fim, passo):
        print(c2)
        time.sleep(0.4)
    print('FIM!')

print('Agora é sua vez!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))