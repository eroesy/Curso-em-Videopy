def ficha(nome='<DESCONHECIDO>',gols=0):
    print(F'O jogador {nome} marcou {gols} gols(s) no campeonato.')



n = input('Nome: ')
g = input('Gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)





















'''def ficha(nome='<desconhecido>',gols='0'):

    if len(nome) ==0:
        nome = '<desconhecido>'
    if len(gols) == 0 or gols.isnumeric() == False:
        gols = 0
    print(f'O {nome} marcou {gols} gols(s) no campeonato.')


ficha(input('Nome do  jogador:'),str(input('Quantos gols ele marcou?:')))'''
