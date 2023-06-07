from time import sleep


def contagenm(a,b,c):
    print('-='*30)
    print(f'Contagem de {a} a {b} de {c} em {c}.')
    cont = a
    if c ==0:
        c = 1
    if c < 0:
        c *= -1
    if c > 0:
        while cont <= b:
            print(f'{cont} ',end='')
            sleep(.25)
            cont += c
    if a > b:
        while cont >= b:
            print(f'{cont} ',end='')
            sleep(.25)
            cont -= c
    print('FIM')
    print('-=' * 30)


print('-='*30)
contagenm(int(input('Inicio: ')),int(input('Fim: ')),int(input('Passo: ')))





'''
def contagem():
    print('=='*15)
    print('Contagem de 1 a 10.')
    for l in range(1,11):
        print(f'{l} ',end='')
        sleep(0.4)
    print(' FIM!')
    sleep(0.2)
    print('==' * 15)
    print('Contagem de 10 até 0 de 2 em 2')
    sleep(0.2)
    for h in range(10,-2,-2):
        print(f'{h} ',end='')
        sleep(0.4)
    print(' FIM!')
    sleep(0.2)
    print('==' * 30)
    print('Agora personalize sua contagem: ')
    sleep(0.2)
    a = int(input('Inicio: '))
    sleep(0.2)
    b = int(input('Fim: '))
    sleep(0.2)
    c = int(input('Passo: '))
    sleep(0.2)

    if c == 0:
        c = 1
    if a < b and c > 0:
        c *= -1
        print('oi')
    if a < b and c < 0:
        print('Burrão kkkkkk')
        


    for cont in range(a, b, c):
        print(f'{cont} ',end='')
        sleep(0.4)
    print(f'{b} FIM!')
    print('==' * 30)




contagem()
'''