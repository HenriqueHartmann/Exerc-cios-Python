mantimentos = ["banana", "laranja", "melao"]

estoque = {
    "banana" : 6 ,
    "melao"  : 0 ,
    "laranja": 32,
    "pera"   : 15,
}

precos = {
    "banana" : 4 ,
    "melao"  : 2 ,
    "laranja": 1.5,
    "pera"   : 3,
}

def calcular_conta(mantimentos):
    total = 0
    for item in mantimentos:
        if estoque[item] > 0:
            total += precos[item]
            estoque[item] = estoque[item] -1
        else:
            print("Não temos {} em estoque!".format(item))
    else:
        string = 'O valor total de sua compra é de R$ {}'.format(total)
        return string

print(calcular_conta(mantimentos))