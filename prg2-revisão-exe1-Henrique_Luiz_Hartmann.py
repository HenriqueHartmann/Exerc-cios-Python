texto = 'alo alo poxa oloko alo poxa pr pr'

def conta_palavras(texto):
    lista = texto.lower().split(" ")
    dicionario = {}
    for palavra in lista:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario
print(conta_palavras(texto))