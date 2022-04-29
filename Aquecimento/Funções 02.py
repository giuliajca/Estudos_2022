# FUNÇÃO PARA CRIAR TÍTULOS ONDE O "MSGN" É A VARIÁVEL MUTÁVEL (QUE SERÁ ALTERADA)
def title(txt):
    print('---' * 10)
    print(     txt    )
    print('---' * 10)
    
title('Contador')
def contador(* num): # <- Desempacotamento está aqui.
    tamanho = len(num)
    print(f'Recebi do usuário {num}, resultando um total de {tamanho} números.')

# Recebi do usuário (0, 1, 2, 3, 4, 5), resultando um total de 6 números.