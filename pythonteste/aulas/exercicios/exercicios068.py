from random import randint,choice
wst = over = 0
n = int(input('Vamos jogar par ou impar?\nDigite um valor: '))
while True:


    pc = randint(0,10)

    total = pc + n
    pl = ' '
    while pl not in 'PI':
        pl = input('Você escolhe par ou impar?:[P/I] ').upper().strip()
    print(f'Você jogou {n} e o computador jogou {pc}.', end=' ')
    print(f'No total deu {total}. ',end='')


    calculo = total % 2
    if calculo == 0:
        resposta = 'PAR'
        print(f'{total} é par!')
        if pl == 'P':
            print('Você ganhou ')
            wst += 1
        else:
            print('Você perdeu')
            break
    else:
        resposta = 'IMPAR'
        print(f'{total} é impar!')
        if pl == 'I':
            print('Você ganhou!')
            wst +=1
        else:
            print('Você perdeu!')
            break
    n = int(input('Vamos jogar de novo??\nDigite um valor: '))



print(f'DEAD MAN\nVocê ganhou {wst} vezes')



