'''
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
1
>>> motor.acelerar()
2
>>> motor.acelerar()
3
>>> motor.velocide# pega a velocidade
# FREANDO
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # TESTANDO A DIREÇÃO
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.virardireita()
>>> direcao.valor
'Leste'
>>> direcao.viraresquerda()
>>> direcao.valor
'Oeste'
>>> direcao.virarPraBaixo()
>>> direcao.valor
'Sul'
'''