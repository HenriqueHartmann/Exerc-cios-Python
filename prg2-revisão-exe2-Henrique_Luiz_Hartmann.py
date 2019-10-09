data = '01/11/2019'

def data_extensao(data):
    dd, mm, aaaa = data.split("/")
    mesExt = [
        'de janeiro de',
        'de fevereiro de',
        'de março de',
        'de abril de',
        'de maio de',
        'de junho de',
        'de julho de',
        'de agosto de',
        'de setembro de',
        'de outubro de',
        'de novembro de',
        'de dezembro de'
    ]
    mm = (int(mm)) - 1
    return '{} {} {}'.format(dd, mesExt[mm], aaaa)

print(data_extensao(data))