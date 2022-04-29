import os

def scanner(pasta_inicial):
    arquivos = os.listdir(pasta_inicial)

    for arquivo in arquivos:
        print(arquivo)

# COLOCAR UM "R" antes para converter A STRING PARA BRUTA.
caminho = r"C:\Users\Joe\Downloads\Estudos\PY — Python 3 Curso Completo do Básico ao Avançado (Coder)\8. Segundo Projeto"
scanner(caminho)
