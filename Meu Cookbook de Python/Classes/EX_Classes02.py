class EuSouUmaClasse:
    # tenho que ser escrita assim mesmo -> PrimeiraLetraMaiúscula
    atributo_estatico = "Eu represento um atributo estático"

    def __init__(self):
        self.atributo_dinamico = "Eu posso ser modificado e sou diferente a cada instância"
        self.outro_atributo = 10

    def eu_sou_um_metodo_de_classe(self):
        # às vezes me chamam de função de classe ou atributo de classe, mas na real eu sou um método de classe
        return "Método de classe"


# INSTANCIANDO A CLASSE
variavel_que_acaba_virando_uma_instancia_da_classe = EuSouUmaClasse()  # A variável é uma instância dessa classe

# ACESSANDO O ATRIBUTO ESTÁTICO DA CLASSE
print(EuSouUmaClasse.atributo_estatico)

# CHAMANDO O MÉTODO DA CLASSE VIA OBJETO NOVO INSTANCIADO
print(variavel_que_acaba_virando_uma_instancia_da_classe.eu_sou_um_metodo_de_classe)

# mesmo que eu não tenha criado o meu atributo dinâmico, dentro do __init__,
# poderei criá-los aqui.
variavel_que_acaba_virando_uma_instancia_de_uma_classe().novo_atributo = "Sou um atributo criado fora do método init."