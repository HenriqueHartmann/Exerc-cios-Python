# coding: utf-8
from functions import escolhaDificuldade
from functions import arquivoSelecionado
from functions import embaralharPalavra
from functions import jogo

jogar = input('Deseja jogar? s para sim e qualquer tecla para não: ')
if jogar == 's':
    dificuldade = escolhaDificuldade()
    palavra = arquivoSelecionado(dificuldade)
    palavraEmbaralhada = embaralharPalavra(palavra)
    jogo(palavra, palavraEmbaralhada)