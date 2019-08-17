#Por Henrique Luiz Hartmann BSI2 14-08-2019
tituloPagina = input('Digite o titulo da página: ')
tituloCabecalho = input('Digite do cabeçalho: ')

arquivo = open('exec.html', 'w', encoding='utf-8')
stringPrimaria = '''<!doctype html>
                <html>
                <head>
                    <title>{}</title>
                </head>
                <body>
                    <h1>{}</h1>
                    '''.format(tituloPagina, tituloCabecalho)
stringPostagens = ''

resp = 's'
while resp == 's':
    tituloPostagem = input('Digite o título da postagem: ')
    descricao = input('Digite a descrição da postagem: ')
    link = input('Digite o link da postagem: ')

    stringPostagens += '''<div><a href="{}">{}</a>: {}</div>'''.format(link, tituloPostagem, descricao)

    resp = input('Deseja adicionar mais uma postagem(s igual sim, digite qualquer outra tecla para parar)? ')

stringTerceira = '</body></html>'
stringSuprema = stringPrimaria+stringPostagens+stringTerceira
arquivo.write('{}'.format(stringSuprema))
arquivo.close()
