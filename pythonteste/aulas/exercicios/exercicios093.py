#analisador de goleiro ou jogadore
#classificação
#media de gols por partidas
#comparação com outros craques

tabela = {}
gols = []
blocks =[]
block = gol = classe= maior = partida =  media =0

tabela['Nome'] = str(input('Nome: ').capitalize())
tabela['modo'] = str(input('Goleiro[ G ] ou jogador[ J ]: ').capitalize().strip())
partidas = int(input(f'Quantas partidas {tabela["Nome"]} jogou?: '))
for c in range(1,partidas+1):
    if tabela['modo'] in 'J':
        gols.append(int(input(f'Quantos gols na {c}° partida?: ')))
        tabela['gols'] = gols
    elif tabela['modo'] in 'G':
        blocks.append(int(input(f'quantos chutes ao gol na {c}° ele pegou?: ')))
        tabela['blocks'] = blocks



if tabela['modo'] in 'J':
    tabela['Posição'] = str(input('Posição: ').capitalize())
    print(f'jognado na posição {tabela["Posição"]}')
print(f'O jogador {tabela["Nome"]}, jogou {partidas} partidas.')
print('=='*30)
if tabela['modo'] in 'J':
    for i,z in enumerate(tabela['gols']):
        print(f'     => Na sua {i + 1:3}°  partida, fez {z} gols')
        if i ==0:
            maior = z
            partida = i+1
        else:
            if maior < z:
                maior = z
                partida = i+1
        gol += z

        media = gol / partidas

    print(f'Com um total de {gol} gols em {partidas} partidas, {tabela["Nome"]} tem em media {media:.0f} de gols por partida')
    print(f'Com a melhor partida sendo {partida}° partida com {maior} gols!!!')

elif tabela['modo'] in 'G':
    for i,z in enumerate(tabela['blocks']):
        print(f'     => Na sua {i + 1:3}°  partida, pegou {z} chutes ao gol')
        if i ==0:
            maior = z
            partida = i+1
        else:
            if maior < z:
                maior = z
                partida = i+1
        block += z
        media = block / partidas


    print(f'Com um total de {block} bloqueios em {partidas} partidas, {tabela["Nome"]} tem em media {media:.0f} de bloqueios por partida')
    print(f'Com a melhor partida sendo {partida}° com {maior} defesas!!!')




if media <= 1:
    classe = '\033[34mJOGADOR'
elif media <= 2:
    classe = '\033[32mPROPLAYER'
elif media <= 3:
    classe = '\033[33mCRAQUE'
elif media >= 4:
    classe = '\033[31mKINGZINHO'

print('=='*30)
print(f'Nosso programa classificou {tabela["Nome"]} em {classe}')
print('=='*30)
print('''
\033[m
 ⣠⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡄⣄⠀⠀⠀⠀
⠀ ⢂⠏⡴⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣜⠳⡍⢢⠁
⠀⠀⠀⠈⠘⡔⣫⢞⣤⣶⣾⣶⣿⣿⣷⣶⣶⣿⣿⣶⣿⣶⣍⡣⢈⠆⠁
    ⠘⣽⠿⠿⠿⣿⣯⣿⡿⣯⢿⣿⣿⣿⡯⢜⡱⢫⣿⠷⠯⣄⠀⠀⠀⠀
    ⢸⣽⠀⠀⡀⠀⠉⢷⣿⣿⣿⣿⣿⡿⣽⢪⣝⠋⡀⠀⠀⠸⠄⠀⠀⠀
    ⢠⣾⠇⠀⠀⠀⠀⠀⣀⠻⣿⣿⣿⣿⣿⣽⣧⢇⠀⠀⠀⠀⠈⣆⠀⠀⠀
    ⣿⢿⣿⣦⣤⣤⣤⣶⣿⣷⣻⣟⣿⣿⣿⣿⣾⣏⡳⢶⣤⣴⣴⡣⠆⠀⠀
    ⢀⣯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⡟⣿⢻⠟⢷⠛⠝⠫⣟⠿⣭⡓⠆⠀⠀
    ⠀⣿⣾⣟⡾⣽⢻⣿⣿⣿⣿⣿⠳⠉⠆⢉⠈⠄⠂⠈⠀⢈⣿⣲⠹⠀⠀⠀
      ⣿⣷⣏⣞⡽⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⣈⡷⣭⢳⡄⠀⠀
      ⣿⣿⣾⡽⣾⣿⣿⠿⡿⢛⠏⢯⡙⠲⡀⠀⠀⠀⢀⠰⡈⡑⠎⡹⠀⠀⠀
     ⣠⣾⣿⣿⣿⣿⣿⣏⣏⠳⡑⢊⠜⠠⠈⠁⠐⠀⠀⠀⠀⠂⠐⠀⠂⠡⠁⠀⠀
    ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣮⡱⣀⠂⡈⠀⠠⠀⠀⠀⠀⠀⠀⢀⠀⠀⠈⠀⠀⠀⠀
    ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣳⢿⡱⢃⠤⠁⡀⠀⠀⠀⠀⢀⠈⢀⠈⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣟⡻⣝⠞⣭⠲⡉⢋⠤⢁⠀⠈⠀⠄⠁⠀⠀⡀⠠⠀
''')
print(tabela)


