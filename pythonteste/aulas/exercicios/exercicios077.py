palavras = 'CASA','APRENDER','ESTUDAR','JOGAR','COMPREENDER','VIVER','ABACAXI', 'ABACATE', 'ABRIL', 'AGOSTO', 'AMARELO', \
    'ANO', 'AZUL', 'BANANA', 'BATATA', 'BRANCO', 'CAFE', 'CAMISA', 'CARRO', 'CASA', 'CHUVA', 'COR', 'DIA', 'DOCE', 'ESCOLA',\
    'ESTADO', 'FEVEREIRO', 'FLOR', 'FRIO', 'FUTEBOL', 'GELADO', 'JANEIRO', 'JULHO', 'JUNHO', 'LARANJA', 'LIVRO', 'MAIO', 'MAR', 'MES',\
    'NOVEMBRO', 'NUMERO', 'OUTUBRO', 'PRETO', 'ROSA', 'RUA', 'SETEMBRO', 'SOL', 'VERDE', 'NEGAO','AVENIDA'



for c in palavras:

    print(f'\nNa palavra {c} nós temos: ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(),end=' ')














    '''print(f'Na palavra {c} temos: ', end='')

    if 'A' in c:
        print('a',end=' ')
    if 'E' in c:
        print('e',end=' ')
    if 'I' in  c:
        print('i',end=' ')
    if 'O' in c:
        print('o',end=' ')
    if 'U' in c:
        print('u',end=' ')
    print('')'''




