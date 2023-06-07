from time import sleep
tabela = []
jogadores = {}
gols = []

total = 0
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome: ').capitalize())
    jogadores['partidas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou?: '))
    for c in range(0,jogadores['partidas']):
        gols.append(int(input(f' - Quantos gols na {c+1}° partida?: ')))
        total = sum(gols)
    jogadores['gols'] = gols[:]
    jogadores['total'] = total
    gols.clear()
    while True:
        resp = input('Quer continuar?[S/N]: ')[0].upper()
        if resp in 'SN':
            break
        print('Responda com S ou N!!!!')
    tabela.append(jogadores.copy())
    if resp =='N':
        break
print('=='*50)
print(f'{"COD":>4}{" "*6}{"NOME":>4}{" "*11}{"PARTIDAS":>5}{" "*14}{"GOLS"}{" "*11}{"TOTAL"}')

for i,c in enumerate(tabela):
    print(f'{i+1:>3}',end='       ')
    for v in c.values():
            print(f'{str(v):<18}', end='')
    print()


print('=='*50)
while True:
    busca = int(input('Digite o codigo do jogador que vc quer os dados [999  para cancelar]: '))
    if busca == 999:
        break
    if busca >= (len(tabela)+1):
        break
    else:
        print(f'- - LEVANTAMENTO DO JOGADOR:{tabela[busca-1]["nome"]}- -')
        for i,k in enumerate(tabela[busca-1]['gols']):
            print(f' - Na {i+1}° partida fez {k} gols.')
print('ENCERRANDO',end='')
sleep(0.9)
print('.',end='')
sleep(0.7)
print('.',end='')
sleep(0.4)
print('.',end='')
print()
print('bye><')