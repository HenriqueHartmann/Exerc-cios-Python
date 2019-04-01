#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@ifc-araquari.edu.br>
# Lista de exercícios 2
import math
def media_final_aprovado_reprovado(p1, p2, ep1, ep2):
    ''' Recebe as notas das 2 provas e 2 exercícios de programação e retorna
    se o aluno foi ou não aprovado. As provas tem peso 7 e os exercícios
    tem peso 3. Cada parcial tem peso igual.'''
    mediaFinal = ((p1*7)+(p2*7)+(ep1*3)+(ep2*3))/20
    if mediaFinal >= 7:
        return True
    else:
        return False

def excesso_peso_peixes(peso_peixes_kg, peso_limite):
    ''' Recebe o peso dos peixes pescados, e o limite legal e devolve
    o peso em excesso, ou zero se não houver'''

    peso_excesso = peso_peixes_kg - peso_limite
    if peso_excesso < 0:
        peso_excesso = 0
        return round(peso_excesso, 2)
    else:
        return round(peso_excesso, 2)


def testa_lados(a, b, c):
    ''' Receba os três lados de um triângulo. Informe se os valores
    podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno. '''

    if a+b > c and a+c > b and b+c > a:
        if a == b and a == c and b == c:
            return "Triângulo equilátero"
        elif a == b or b == c or a == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Não forma um triângulo"

def ano_bissexto(ano):
    ''' Determine se um ano é bissexto'''
    anoDivBy4 = ano % 4
    anoDivBy100 = ano % 100
    anoDivBy400 = ano % 400
    if anoDivBy4 != 0:
        if anoDivBy400 == 0:
            return True
        else:
            return False
    else:
        if anoDivBy100 != 0:
            return True
        elif anoDivBy400 == 0:
            return True
        else:
            return False

def data_valida(data):
    '''Valida data. Recebe uma string no formato dd/mm/aaaa e informa
    um valor lógico indicando se a data é válida ou não.'''
    line = data.split('/')
    dia = int(line[0])
    mes = int(line[1])
    ano = int(line[2])
    anobi = ano_bissexto(ano)
    diasnomes = ['', 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(mes >= 1 and mes <= 12 and ano != 0):
        if(dia >=1 and dia <= diasnomes[mes]):
            teste1 = 'True'
        else:
            teste1 = 'False'
    else:
        teste1 = 'False'
    if (mes == 2 and dia <= 28 and anobi == False):
        teste2 = 'True'
    elif(mes == 2 and dia <= 29 and anobi == True):
        teste2 = 'True'
    elif(mes != 2):
        teste2 = 'True'
    else:
        teste2 = 'False'
    if(teste1 == 'True'and teste2 == 'True'):
        return True
    elif(teste1 == 'True'and teste2 == 'True'):
        return False
    else:
        return False

def maior3(a, b, c):
    ''' Recebe tres valores, e retorna o maior dos tres'''
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

def menor3(a, b, c):
    ''' Recebe tres valores, e retorna o menor dos tres'''
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

def salario(dinheiro_horas, horas_mensais):
    ''' Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.
    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto'''
    salarioBruto = dinheiro_horas * horas_mensais
    saldiv100 = salarioBruto / 100
    inss = saldiv100 * 8
    ir = saldiv100 * 11
    sindicato = saldiv100 * 5
    descontoTotal = inss + ir + sindicato
    salarioLiquido  = salarioBruto - descontoTotal
    return int(salarioLiquido)


def tinta(metros_pintar):
    ''' Recebe quanto metros quadrados precisa pintar,
    e retorna a quantidade de latas de tinta a comprar.
    A cobertura da tinta é de 3 metros por litro de tinta
    Cada lata possui 18 litros de tinta'''

    qtdLitros = metros_pintar / 3
    qtdLatas = qtdLitros  / 18
    return math.ceil(qtdLatas)


def acrescimo_nota_bb(nota_sozinho, nota_com_ajuda):
    ''' Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo'''
    if nota_sozinho > nota_com_ajuda :
        return 0

    elif nota_sozinho < nota_com_ajuda:
        diferenca = nota_com_ajuda - nota_sozinho
        acrescimo = diferenca / 4
        acre = f'{acrescimo:.1f}'
        acre = float(acre)
        return acre
# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Média final:')
    test(media_final_aprovado_reprovado(10, 10, 0, 0), True)
    test(media_final_aprovado_reprovado(0, 0, 10, 10), False)
    test(media_final_aprovado_reprovado(10, 10, 10, 10), True)
    test(media_final_aprovado_reprovado(0, 0, 5, 0), False)
    test(media_final_aprovado_reprovado(8.0, 7.0, 9.0, 8.0), True)

    print('Pesca em excesso:')
    test(excesso_peso_peixes(10, 50), 0)
    test(excesso_peso_peixes(50, 50), 0)
    test(excesso_peso_peixes(50.01, 50), 0.01)
    test(excesso_peso_peixes(190.99, 50), 140.99)

    print('Triângulos:')
    test(testa_lados(7, 1, 2), 'Não forma um triângulo')
    test(testa_lados(7, 2, 1), 'Não forma um triângulo')
    test(testa_lados(1, 7, 2), 'Não forma um triângulo')
    test(testa_lados(1, 2, 7), 'Não forma um triângulo')
    test(testa_lados(2, 1, 7), 'Não forma um triângulo')
    test(testa_lados(2, 7, 1), 'Não forma um triângulo')
    test(testa_lados(2, 2, 2), 'Triângulo equilátero')
    test(testa_lados(3, 3, 3), 'Triângulo equilátero')
    test(testa_lados(2, 3, 4), 'Triângulo escaleno')
    test(testa_lados(2, 4, 3), 'Triângulo escaleno')
    test(testa_lados(3, 4, 2), 'Triângulo escaleno')
    test(testa_lados(3, 2, 4), 'Triângulo escaleno')
    test(testa_lados(2, 3, 3), 'Triângulo isósceles')
    test(testa_lados(3, 2, 2), 'Triângulo isósceles')
    test(testa_lados(3, 3, 2), 'Triângulo isósceles')
    test(testa_lados(3, 2, 3), 'Triângulo isósceles')

    print('Ano bissexto:')
    test(ano_bissexto(1000), False)
    test(ano_bissexto(1200), True)
    test(ano_bissexto(1004), True)
    test(ano_bissexto(1040), True)
    test(ano_bissexto(2012), True)
    test(ano_bissexto(2014), False)

    print('Valida datas:')
    test(data_valida("01/01/2014"), True)
    test(data_valida("31/01/2014"), True)
    test(data_valida("00/00/0000"), False)
    test(data_valida("30/04/2014"), True)
    test(data_valida("31/04/2014"), False)
    test(data_valida("30/09/2014"), True)
    test(data_valida("31/09/2014"), False)
    test(data_valida("30/06/2014"), True)
    test(data_valida("31/06/2014"), False)
    test(data_valida("30/11/2014"), True)
    test(data_valida("31/11/2014"), False)
    test(data_valida("32/01/2014"), False)
    test(data_valida("01/01/0000"), False)
    test(data_valida("01/13/2014"), False)
    test(data_valida("01/00/2014"), False)
    test(data_valida("29/02/2014"), False)
    test(data_valida("29/02/2016"), True)

    print('Maior de 3 valores:')
    test(maior3(1, 2, 3), 3)
    test(maior3(1.01, 1.1, 1.02), 1.1)
    test(maior3(0, -1, -2), 0)
    test(maior3(-100, 0, 100), 100)

    print('Menor de 3 valores:')
    test(menor3(1, 2, 3), 1)
    test(menor3(1.01, 1.02, 1.1), 1.01)
    test(menor3(0, -1, -2), -2)
    test(menor3(-100, 0, 100), -100)

    print('Salário líquido:')
    test(salario(10, 80), 608)
    test(salario(100, 30), 2280)
    test(salario(2.5, 300), 570)
    test(salario(5, 120), 456)

    print('Latas de tinta:')
    test(tinta(10), 1)
    test(tinta(100), 2)
    test(tinta(560), 11)
    test(tinta(50001), 926)

    print('Acréscimo BB:')
    test(acrescimo_nota_bb(1, 10), 2.2)
    test(acrescimo_nota_bb(7, 6), 0.0)
    test(acrescimo_nota_bb(0, 10), 2.5)
    test(acrescimo_nota_bb(6.9, 7.1), 0.0)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
