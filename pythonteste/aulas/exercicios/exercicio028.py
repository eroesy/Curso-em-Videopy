import random
from time import sleep

e = input('Oi tudo bem?: ').upper().strip()
if e == 'SIM':
    print('Que bom ><')
    sleep(1)
else:
    print('Que tal um jogo para melhorar?')
    sleep(1)
q = input('Vamos jogar?: ').upper().strip()
if q == 'SIM':

    #computador = randint(0,5) tem q importar viu burrão
    n = ([1,2,3,4,5])
    es = random.choice(n)
    print('A brincadeira séra assim ó:\n Vou escolher um numero de 0 a 5, e você vai tentar acertar. ')
    sleep(2)
    esc = int(input('Já escolhi o numero, agora tente acertar qual foi: '))
    if esc == es:
        print('Ebaaa, você acertou')
    else:

        print("T-T xiiiiii, vc errou")
        sleep(0.3)
        print(f'Era {es}, foi quase><')
else:
    print('AH. TUDO BEM t-t')