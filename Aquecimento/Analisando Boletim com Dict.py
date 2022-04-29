def boletim(items, situacao=False):
    dict = {}
    dict['soma'] = sum(items)
    dict['maior'] = max(items)
    
    if situacao == True:
        if max > 8:
            return f'Sua nota é maior do que 8.'
            situacao = 'Aprovado'
        else:
            return f'Sua nota é menor do que 8.'
            situacao = 'Reprovado'
    dict[situacao] = situacao
    return dict
