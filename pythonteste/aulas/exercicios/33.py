from time import sleep


jogadores = []
jogador = {}
gols = []

while True:
    jogador['nome'] = str(input('Nome: ').capitalize())
    jogador['idade'] = int(input(f'Idade de {jogador["nome"]}: '))
    jogador['partidas'] = int(input(f'Partidas jogadas de {jogador["nome"]}: '))
    for c in range(0,jogador['partidas']):
        gols.append(int(input(f' - Quantos gols na {c+1}° partida: ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()

    while True:
        resp = str(input('Quer continuar?[S/N]: ').upper().strip())
        if resp[0] in "SN":
            break
        print('Por favor digite S ou N!!!')
    if resp == 'N':
        break
print('=='*40)
print(f'{"COD":<3}{"NOME":>6}{"IDADE":>13}{"PARTIDAS":>17}{"GOLS":>14}{"TOTAL":>24}')
print('=='*40)
for i,c in enumerate(jogadores):
    print(f'{i+1:>2}  ',end='')
    for n,v in enumerate(c.values()):
        if n ==3:
            print(f'{str(v):<25}', end='')
        else:
            print(f'{str(v):<15}',end='')
    print()
print('=='*40)
print()


while True:
    busca = int(input('Digite o codigo do jogador para puchar seus dados[999 para cancelar!]: '))
    if busca == 999:
        break
    elif busca >= (len(jogadores)+1):
        print('POR FAVOR! somente os codigos que estão dentro da lista!!!')
    else:
        print('   _--LEVANTAMENTO DE DADOS--_')
        print(f'{jogadores[busca-1]["nome"]:^31}')
        sleep(0.4)
        for i,v in enumerate(jogadores[busca-1]['gols']):
            print(f' - Na {i}° O {jogadores[busca-1]["nome"]} fez {v}gols!!!')
            sleep(0.2)
        print()
print(F'\n\n{"ENCERRANDO":^70}')
sleep(0.4)
print('.',end='')
sleep(0.4)
print('.',end='')
sleep(0.4)
print('.',end='')
print()
print()