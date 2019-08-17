#Aluno: Henrique Luiz Hartmann BSI-2
# coding: utf-8
import random

def escolherPalavra():
    palavras = open("Palavras.txt", encoding='utf-8').read().splitlines()
    return random.choice(palavras)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def embaralharPalavra(palavra):
    return ''.join(random.sample(palavra, len(palavra)))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def jogo(palavra, palavraEmbaralhada):
    print('Seu objetivo é desembaralhar a palavra em até 5 tentativas! Será que você consegue? \n')
    tentativa = 5
    frasesAnimadoras = ['Enquanto houver vontade de lutar haverá esperança de vencer. Então tente outra vez.\n',
                            'O importante não é vencer todos os dias, mas lutar sempre. Então tente outra vez.\n',
                            'Maior que a tristeza de não haver vencido é a vergonha de não ter lutado. Então tente outra vez.\n',
                            'Pessimismo leva à fraqueza, otimismo ao poder. Então tente outra vez.\n',
                            'Nossa maior fraqueza está em desistir. O caminho mais certo de vencer é tentar mais uma vez. Então tente outra vez.\n',
                            'Você perdeu, mas quem sabe da próxima ;)']

    while tentativa != 0:
        resp = input('Sua palavra é: {} , num. tentativa(s): {}. R: '.format(palavraEmbaralhada, tentativa))
        tentativa -= 1
        if resp == palavra:
            print("Você venceu, a palvra era '{}' e você utilizou {} tentativa(s)".format(palavra, (5 - tentativa)))
            break
        else:
            print(frasesAnimadoras[(5 - tentativa)])
    else:
        print("A palavra era '{}' e você utilizou {} tentativa(s)".format(palavra, (5 - tentativa)))

    jogarDNV = input('Deseja jogar novamente? s(sim) e qualquer tecla para não: ')
    if jogarDNV == 's':
        palavra = escolherPalavra()
        palavraEmbaralhada = embaralharPalavra(palavra)
        jogo(palavra, palavraEmbaralhada)
    else:
        exit()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
jogar = input('Deseja jogar? s para sim e qualquer tecla para não: ')
if jogar == 's':
    palavra = escolherPalavra()
    palavraEmbaralhada = embaralharPalavra(palavra)
    jogo(palavra, palavraEmbaralhada)
