class Carros():
    """Uma tentariva simples de representar um carro"""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 100
        self.odometro = 0

    def descricao_nome(self):
        """Devolve um nome decritivo, formatado de modo elegante."""
        nome_longo = str(self.ano) + " " + self.fabricante + " " + self.modelo
        return nome_longo.title()

    def leia_odometro(self):
        """Exibe uma frase que mostra o valor do odometro do carro"""
        print(" O carro tem " + str(self.odometro) + " KM rodados.")

    def altera_odometro(self, novo_odometro):
        """Altera o odometro pelo valor passado como argumento"""
        self.odometro = novo_odometro

    def incrementa_odometro(self, novo_odometro):
        """Incrementa um determinado valor ao odometro."""
        self.odometro += novo_odometro

    def tanque_gasolina(self):
        """Exibe  a quantida de gasolina no tanque"""
        print("O tanque de gasolina está " + str(self.combustivel) + "% cheio")

carro1 = Carros("Honda", "Civic", 2015)

print(carro1.descricao_nome())
carro1.tanque_gasolina()
print("")

#carro1.tanque_gasolina()

class CarrosEletricos(Carros):
    """Representa aspectos de um carro especificos, no caso, elétricos"""
    def __init__(self, fabricante, modelo, ano):
        """Incializa os atributos da classe-pai"""
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()
        
    def tanque_gasolina(self):
        """Carros eletricos não usan gasolina"""
        print("Carros elétricos não usam gasolina. ")

class Bateria():
    """Uma tentativa simples de criar uma bateria"""
    def __init__(self, bateria=100):
        """Inicializa os atributos da bateria"""
        self.bateria = bateria

    def altera_bateria(self, novo_valor):
        """Altera o valor da bateria"""
        self.bateria = novo_valor

    def mostra_bateria(self):
        print("A bateria está " + str(self.bateria) + "% cheia")

meu_carro = CarrosEletricos("Honda", "Civic", 2015)
meu_outro_carro = CarrosEletricos("Ford", "Focus", 2017)

#print(meu_carro.bateria.bateria)

meu_carro.bateria.mostra_bateria()

meu_carro.bateria.altera_bateria(56)

meu_carro.bateria.mostra_bateria()


meu_outro_carro.bateria.mostra_bateria()

meu_outro_carro.bateria.altera_bateria(70)

meu_outro_carro.bateria.mostra_bateria()


#print(meu_carro.bateria.bateria


#bateria = Bateria()

#print(bateria.bateria)
#bateria.altera_bateria(80)
#print(bateria.bateria)


#carro_eletric = CarrosEletricos("tesla", "model s", 2016)
#print(carro_eletric.descricao_nome())
#carro_eletric.tanque_gasolina()

#meu_carro = Carros("audi", "A4", 2016)
#print(meu_carro.descricao_nome())
#meu_carro.leia_odometro()
#print("")

#print("Mudando o odômetro!")

#meu_carro.odometro = 5
#meu_carro.leia_odometro()

#print("")
#print("mudando odometro")
#meu_carro.altera_odometro(10)
#meu_carro.leia_odometro()

#print("")
#print("mudando odometro")
#meu_carro.incrementa_odometro(10)
#meu_carro.leia_odometro()

#print("")
#print("mudando odometro")
#meu_carro.incrementa_odometro(3)
#meu_carro.leia_odometro()

#meu_outro_carro = Carros("Honda", "civic", 2015)
#print("")
#print("")

#print(meu_outro_carro.descricao_nome())
#meu_outro_carro.leia_odometro()
#print("")

#print("Mudando o odômetro!")

#meu_outro_carro.odometro = 7
#meu_outro_carro.leia_odometro()

#print("")
#print("mudando odometro")
#meu_outro_carro.altera_odometro(13)
#meu_outro_carro.leia_odometro()

#print("")
#print("mudando odometro")
#meu_outro_carro.incrementa_odometro(12)
#meu_outro_carro.leia_odometro()

#print("")
#print("mudando odometro")
#meu_outro_carro.incrementa_odometro(5)
#meu_outro_carro.leia_odometro()


