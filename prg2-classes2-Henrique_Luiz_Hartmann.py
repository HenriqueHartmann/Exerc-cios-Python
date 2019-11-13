class Macaco:
    def __init__(self, nome, bucho=[]):
        self.nome = nome
        self.bucho = bucho
    def comer(self, comida):
        self.bucho.append(comida)
    def verBucho(self):
        print(self.bucho)
    def digerir(self):
        self.bucho = []

# mc1 = Macaco('Jhonny')
# mc1.comer('uva')
# mc1.comer('queijo')
# mc1.verBucho()
# mc1.digerir()
# mc1.verBucho() 

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0
    def andar(self, distancia):
        consumo = distancia / self.consumo
        self.tanque -= consumo
    def obterGasolina(self):
        print(self.tanque)    
    def adicionarGasolina(self, qtdGasosa):
        self.tanque += qtdGasosa

# fusca = Carro(15)
# fusca.adicionarGasolina(20)
# fusca.andar(100)
# fusca.obterGasolina()
