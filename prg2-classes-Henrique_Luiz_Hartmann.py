class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
    def mostraCor(self):
        print(self.cor)
    def trocaCor(self):
        self.cor = input("Digite a nova cor: ")
        print(self.cor)
# b1 = Bola('azul', 20, 'borracha')
# b1.mostraCor()
# b1.trocaCor()

class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
    def mudarValorLado(self):
        self.tamanhoLado = int(input("Digite o novo valor do lado: "))
        print(self.tamanhoLado)
    def retornaValorLado(self):
        print(self.tamanhoLado)
    def calculaArea(self):
        print(self.tamanhoLado ** 2)
# q1 = Quadrado(10)
# q1.mudarValorLado()
# q1.retornaValorLado()
# q1.calculaArea()

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def mudarValorLados(self):
        self.base = int(input('Digite a nova base: '))
        self.altura = int(input('Digite a nova altura: '))
        print('base: {}; altura: {}'.format(self.base, self.altura))
    def retornaValorLados(self):
        print('base: {}; altura: {}'.format(self.base, self.altura))
    def calcularArea(self):
        area = self.altura * self.base
        print(area)
    def calcularPerimetro(self):
        perimetro = self.altura * 2 + self.base * 2
        print(perimetro)
# r1 = Retangulo(10, 20)
# r1.mudarValorLados()
# r1.retornaValorLados()
# r1.calcularArea()
# r1.calcularPerimetro()