#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios de revisão de listas

# Exercícios apenas com for (sempre que possível), e sem funções embutidas.

def contem(lista, item_procurado):
    '''Verifica se uma lista contém um item e devolve um valor booleano.
    Não utilize find, index, in ou outras funções prontas da linguagem.'''
    # return item_procurado in lista
    for item in lista:
            if item == item_procurado:
                return True
    else:
        return False

def conta(lista, item_procurado):
    '''Informa quantas ocorrências de um item existem numa lista.
    Não utilize find, index, in, count ou outras funções prontas da linguagem.'''
    count = 0
    for item in lista:
        if item == item_procurado:
            count += 1
    return count

def posicoes(lista, item_procurado):
    '''Devolve uma lista com as posições em que aparece um item solicitado.
    Não utilize find, index, in, count ou outras funções prontas da linguagem.'''
    listaposicoes = []
    for i,item in enumerate(lista):
        if item == item_procurado:
            listaposicoes.append(i)
    return listaposicoes

def troca_ocorrencias(lista, item_procurado, item_novo):
    '''Devolve uma nova lista com o item procurado trocado pelo item_novo.
    Não utilize find, index, in, count, replace ou outras funções prontas da linguagem.'''
    novalista = lista
    for i,item in enumerate(lista):
        if item == item_procurado:
            novalista[i] = item_novo
    return novalista

def remove_ocorrencias(lista, item_procurado):
    '''Devolve uma nova lista sem as ocorrencias do item procurado.
    Não utilize find, index, in, count, replace, remove, del ou outras funções prontas da linguagem.'''
    novalista = []
    for item in lista:
        if item != item_procurado:
            novalista.append(item)
    return novalista

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
    print('Possui item:')
    test(contem([1, 2, 3, 4, 5], 6), False)
    test(contem([1, 2, 3, 4, 5], 3), True)
    test(contem(['b', 's', 'i'], 'i'), True)
    test(contem(['b', 's', 'i'], 'S'), False)

    print('Conta itens:')
    test(conta([1, 2, 3, 4, 5], 6), 0)
    test(conta([1, 2, 3, 4, 5], 1), 1)
    test(conta([1, 2, 1, 4, 1], 1), 3)
    test(conta(['b', 's', 'i'], 'i'), 1)
    test(conta(['b', 's', 'i'], 'S'), 0)
    test(conta(['b', 's', 'i', 'i', 'f', 'c'], 'i'), 2)

    print('Devolve as posições de um item:')
    test(posicoes([1, 2, 3, 4, 5], 6), [])
    test(posicoes([1, 2, 3, 4, 5], 1), [0, ])
    test(posicoes([1, 2, 1, 4, 1], 1), [0, 2, 4])
    test(posicoes(['b', 's', 'i'], 'i'), [2, ])
    test(posicoes(['b', 's', 'i'], 'S'), [])
    test(posicoes(['b', 's', 'i', 'i', 'f', 'c'], 'i'), [2, 3])

    print('Troca as ocorrências de um item:')
    test(troca_ocorrencias([1, 2, 3, 4, 5], 6, 1), [1, 2, 3, 4, 5])
    test(troca_ocorrencias([1, 2, 3, 4, 5], 1, 6), [6, 2, 3, 4, 5])
    test(troca_ocorrencias([1, 2, 1, 4, 1], 1, 5), [5, 2, 5, 4, 5])
    test(troca_ocorrencias(['b', 's', 'i'], 'i', 'd'), ['b', 's', 'd'])
    test(troca_ocorrencias(['b', 's', 'i'], 'I', 'd'), ['b', 's', 'i'])

    print('Remove as ocorrências de um item:')
    test(remove_ocorrencias([1, 2, 3, 4, 5], 1), [2, 3, 4, 5])
    test(remove_ocorrencias([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])
    test(remove_ocorrencias([1, 2, 1, 4, 1], 1), [2, 4])
    test(remove_ocorrencias(['b', 's', 'i'], 'i'), ['b', 's'])
    test(remove_ocorrencias(['b', 's', 'i'], 'I'), ['b', 's', 'i'])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")