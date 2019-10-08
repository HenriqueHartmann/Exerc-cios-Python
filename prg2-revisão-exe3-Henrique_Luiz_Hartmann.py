nome_completo = 'Pedro de Alcântara Francisco Antônio João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim de Bragança e Bourbon'

def abrevia_nome(nome_completo):
    nomes = nome_completo.split(" ")
    count = len(nomes)
    for i,nome in enumerate(nomes):
        if i != 0 and i != (count -1):
            nomes[i] = nome[0]
    return " ".join(nomes)      
print(abrevia_nome(nome_completo))        