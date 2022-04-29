def title (txt):
    print('-'*15)
    print(txt)
    print('-'*15)

# FUNÇÃO QUE CRIA V1 E V2 E CALCULA A ÁREA.
def area(v1, v2):
    calculo = v1*v2
    print(f'A área é {calculo} m².')

# ENTRADAS DO USUÁRIO
v1 = float(input('Largura: '))    
v2 = float(input('Comprimento: '))    

# PEGO V1 E V2 DO USUÁRIO E JOGO PARA DENTRO DA FUNC ÁREA
area(v1, v2)
