# PRINCIPAL

import turtle

# INICIALIZANDO
t = turtle.Turtle()
# VELOCIDADE
t.speed(1)

while True:
    # MOVIMENTAR A TURTLE PARA FRENTE
    distancia = int(input('Foward:\n'))
    t.forward(distancia)

    # ROTACIONAR EM X GRAUS PARA DIREITA
    rot_x = int(input('Right:\n'))
    t.right(rot_x)

    # MOVIMENTAR " PARA TRÁS
    tras = int(input('Backward:\n'))
    t.backward(tras)
    #t.right(90)

    # ROTACIONAR EM Y GRAUS PARA ESQUERDA
    rot_y = int(input('Left:\n'))
    t.left(rot_y)

    user = str(input('Deseja continuar? [S/N]\n')).upper()
    if user == 'N':
        break
    else:
        continue


# PARA JANELA NÃO FECHAR QUANDO TERMINAR
