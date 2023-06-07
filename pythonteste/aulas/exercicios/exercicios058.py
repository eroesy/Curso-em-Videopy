from random import randint
from time import sleep
pc = randint(1,10)
ply = count = 0
while ply != pc:

    ply = int(input('Digite um numero e tente acertar o numero escolhido :-: : '))
    if ply != pc:
        print('ERROUUUUUU 0_0')
        if ply > pc:
            print('Um pouco mais para baixo!')
        else:
            print('Um pouco mais para cima')

    count += 1








print('ah! 0o0')
sleep(0.7)
print('voce acertou T-T')
sleep(0.7)
if 5 >count > 1:
    print(f'Com {count} tentativas')
    sleep(0.6)
    print('até que foi bom xD')

elif count > 10:
    print(f'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
    sleep(0.6)
    print(f'voce acertou com {count} tentativas')
    sleep(0.6)
    print('MUITO RUIM VC KKKkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')

elif count == 1 :
    print(f'como que você acerta com {count} tentativas?T-T')
    sleep(0.7)
    print('OU VOCÊ É MUITO BOM, OU VOCE TA ROUBANDO!!!')
else:
    print(f'Com {count} tentavias')
    sleep(0.6)
    print('ruimzão!!')

