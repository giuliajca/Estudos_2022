# PRINCIPAL
import turtle

t = turtle.Turtle()  # INICIALIZANDO E INSTANCIANDO
t.speed(1)  # VELOCIDADE


def obter_distancia():
    distancia = int(input('Quantos pixels movimentar para frente?\n'))
    return distancia


def rotacionar(turtle):
    rotacao = int(input('Virar pra d:direita | e: esquerda | n: não rotacionar').upper())
    if rotacao == 'd':
        rotacionar_direita()
    elif rotacao == 'e':
        rotacionar_esquerda()


def rotacionar_direita(turtle):
    angulo = int(input('Digite o âgulo para virar para direita: '))
    t.right(angulo)


def rotacionar_esquerda(turtle):
    angulo = int(input('Digite o âgulo para virar para esquerda: '))
    t.left(angulo)


while True:
    direcao = input('Para que direção iremos? F: FRENTE | T: TRÁS\n').upper()
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar(t)
        t.backward(distancia)
    resposta = input('Continuar?')
    if resposta not in ('s','sim'):
        break

    '''
    sair = str(input('Continuar andando?')).upper()
    if sair not in ('sim', 's'):
        break

------------------------
user = str(input('Deseja continuar? [S/N]\n')).upper()
if user == 'N':
    break
else:
    continue
'''
