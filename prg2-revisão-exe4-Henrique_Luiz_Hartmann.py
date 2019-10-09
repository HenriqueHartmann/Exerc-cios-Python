def resgatando_dados():
    arquivo = open('entrada.txt', encoding='utf-8').read().splitlines()
    dicionario = {}
    for nome in arquivo:
        nome, valor = nome.split(";")
        valor = float(valor)
        if nome not in dicionario:
            dicionario[nome] = valor
        else:
            dicionario[nome] += valor
    return dicionario

def inserindo_dados():
    arquivo = open('totais.txt', 'w+', encoding='utf-8')
    dicionario = resgatando_dados()
    conteudo = ''
    for nome in dicionario:
        conteudo += '{};{}\n'.format(nome,dicionario[nome])
    arquivo.write(conteudo)
    arquivo.close()

inserindo_dados()