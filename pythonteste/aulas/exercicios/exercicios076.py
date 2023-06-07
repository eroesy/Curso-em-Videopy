
ponto = '.'
tabela = 'Lapis', 2.50, 'Miojo',3.75,'Xicara',13.99,'Bola',300
print('='*39)
print(f'{"TABELA":^40}')
print('='*39)
for pos in range(0,len(tabela)):
    if pos % 2 ==0:
        print(f'{tabela[pos]:.<30}',end='')
    else:
        print(f'R${tabela[pos]:>7}')
print('='*39)





