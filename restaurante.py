#Crie uma classe Restaurante. O metodo __init__() de Restaurante deve
# aramzenar dois atributos: restaurante_nome tipo_cozinha. Crie um metodo chamado
# restaurante_descricao() que mostre essas duas informações, e um metodo de nome
# restaurante_aberto() que exiba uma mensagem informando que o restaurante está aberto.
# Creie uma instancia chamada a partir de sua classe. Mostre os dois atributos
# individualmente e, em seguida, chame os dois métodos.

#Três restaurantes: Comece com a classe do exercício anterios. Crie três instâncias
#diferentes da classe e chame restaurante_descricao() para cada instância.

class Restaurante():
    """Representa um restaurante"""
    def __init__(self, restaurante_nome, tipo_cozinha):
        self.restaurante_nome = restaurante_nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        print("O restaurante se chama " + self.restaurante_nome + " e sua especialidade é "
              + self.tipo_cozinha)

    def restaurante_aberto(self):
        print("O restaurante " + self.restaurante_nome + " está aberto no momento!")

restaurante1 = Restaurante("La casa do pastel", "pastel")
restaurante2 = Restaurante("Comida á mineira", "comida mineira")
restaurante3 = Restaurante("Massa Fera", "massas")

#print(restaurante1.restaurante_nome)
#print(restaurante1.tipo_cozinha)

restaurante1.restaurante_descricao()
restaurante2.restaurante_descricao()
restaurante3.restaurante_descricao()