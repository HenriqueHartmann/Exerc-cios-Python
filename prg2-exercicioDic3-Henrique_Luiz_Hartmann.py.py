# coding: utf-8
def traduz_para_ingles(texto):
    texto = texto.lower().split(' ')
    novotexto = ''
    dicionario = {
        "meio"     : 'middle',
        "menino"   : 'boy',
        "menina"   : 'girl',
        "carro"    : 'car',
        "titulo"   : 'title',
        "nome"     : 'name',
        "pai"      : 'father',
        "mestre"   : 'master',
        "forte"    : 'strong',
        "escrever" : 'write',
        "mãe"      : 'mother',
        "bom"      : 'good',
        "é"        : 'is',
        "estão"    : 'are',
        "meu"      : 'my',
        "eles"     : 'they',
        "viajando" : 'travelling'
    }

    for seg in texto:
        if seg in dicionario:
            novotexto += "{} ".format(dicionario[seg])
    else:
        return novotexto

palavra = input("Digite a palavra a ser traduzida: ")
print(traduz_para_ingles(palavra))