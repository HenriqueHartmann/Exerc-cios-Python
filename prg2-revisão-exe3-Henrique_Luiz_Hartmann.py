nome_completo = 'Pedro de Alcântara Francisco Antônio João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim de Bragança e Bourbon'

def abrevia_nome(nome_completo):
    nomes = nome_completo.split(" ")
    count = len(nomes)
    for i,nome in enumerate(nomes):
        if len(nome) <= 3:
            nomes[i] = ''
        elif i != 0 and i != (count -1):
            nomes[i] = nome[0]
    nomes = filter(None, nomes)
    return " ".join(nomes)
print(abrevia_nome(nome_completo))