# PARÂMETROS VARIÁVEIS COM TUPLAS

def soma(*parcelas): # 1 SÓ ASTERISTICO* É UMA TUPLA
    contador = 0
    for valor in parcelas:
        contador = valor + contador
    return contador
print(soma(5,4,6,4))

# PARÂMETROS VARIÁVEIS COM DICIONÁRIOS

def soma2(**parcelas2):
    pass