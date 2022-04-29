# FUNÇÃO PARA CRIAR TÍTULOS ONDE O "MSGN" É A VARIÁVEL MUTÁVEL (QUE SERÁ ALTERADA)
def title(txt):
    print('---' * 10)
    print(     txt    )
    print('---' * 10)
    
title('MAIOR OU MENOR')

def maior_menor(a,b):
    if a > b:
        print(f' {a} é maior que {b}.')
     
    elif a < b:
        print(f'{a} é menor que {b}.')
    
    elif a == b or b == a:
        print('O número é igual.')
       
a = int(input('A: '))
b = int(input('B: '))

maior_menor(a, b)