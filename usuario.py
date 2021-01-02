#Crie uma classe chamada Usuario. Crie dois atriutos de nomes primeiro_nome
# e ultimo_nome e, então, crie varios outros atributos normalmente armazenados em um perfil
# de usuário, escreva um método de nome cescricao_usuario() que apresente um resumo das
# informações do usuário. escreva outro método chamado saudação_usuario() que mostre uma
# saudação personalizada ao usuário.
class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome, idade, cidade, sexo):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.cidade = cidade
        self.sexo = sexo

    def descricao_usuario(self):
        print(self.primeiro_nome.title() + " " + self.ultimo_nome.title())
        print(str(self.idade) + " anos")
        print("Nacido em " + self.cidade)
        print("Do sexo " + self.sexo)


    def saudacao(self):
        print("Olá " + self.primeiro_nome.title() + " " + self.ultimo_nome.title()
              + ", seja bem vindo! ")

usuario1 = Usuario("João", "Ribeiro", 33, " Guará", " Masculino ")
usuario2 = Usuario("Julia", "Tomate", 36, " Ituverava", " Feminico ")
usuario3 = Usuario("alfredo", "Manoel", 53, " Ribeirão preto", " Masculino ")

usuario1.descricao_usuario()
print("")
usuario2.descricao_usuario()
print("")
usuario3.descricao_usuario()