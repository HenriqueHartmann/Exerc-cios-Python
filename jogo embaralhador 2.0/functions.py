# coding: utf-8
import random
def escolhaDificuldade():
    escolha = int(input("Fácil - digite 1 | Médio - digite 2 | Difícil - digite 3 \n: "))
    return escolha

def arquivoSelecionado(escolha):
    if escolha == 1:
        facil = open('facil.txt', encoding='utf-8').read().splitlines()
        return random.choice(facil)
    elif escolha == 2:
        medio = open('medio.txt', encoding='utf-8').read().splitlines()
        return random.choice(medio)
    elif escolha == 3:
        dificil = open('dificil.txt', encoding='utf-8').read().splitlines()
        return random.choice(dificil)

def embaralharPalavra(palavra):
    return ''.join(random.sample(palavra, len(palavra)))

def jogo(palavra, palavraEmbaralhada):
    tentativa = 5
    while tentativa != 0:
        resp = input('Sua palavra é: {} , num. tentativa(s): {}. R: \n'.format(palavraEmbaralhada, tentativa))
        tentativa -= 1
        if resp == palavra:
            print("Você venceu, a palvra era '{}' e você utilizou {} tentativa(s) \n".format(palavra, (5 - tentativa)))
            break
        else:
            palavraAnimadora = escolhaFraseAnimadora()
            print(palavraAnimadora)
    else:
        print("A palavra era '{}' e você utilizou {} tentativa(s)".format(palavra, (5 - tentativa)))

    jogarDNV = input('Deseja jogar novamente? s(sim) e qualquer tecla para não: \n')
    if jogarDNV == 's':
        dificuldade = escolhaDificuldade()
        palavra = arquivoSelecionado(dificuldade)
        palavraEmbaralhada = embaralharPalavra(palavra)
        jogo(palavra, palavraEmbaralhada)
    else:
        exit()

def escolhaFraseAnimadora():
    frase = open('palavrasDeAnimo.txt').read().splitlines()
    return random.choice(frase)