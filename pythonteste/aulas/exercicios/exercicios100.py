from random import randint
from time import sleep

numeros = []


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)



def sorteio():
    print('Sorteando numeros', end='')
    print('.', end='')
    sleep(0.15)
    print('.', end='')
    sleep(0.15)
    print('.')
    sleep(0.15)
    print('Numeros sorteados: ',end='')

    for c in range(0,5):
        nums = randint(0,1000)
        print(f'{nums} ',end='')
        sleep(0.3)
        numeros.append(nums)
    print()
    print('==' * 30)
    print(' - Somando os valores pares de ',end='')
    print(numeros,end='')
    print(', temos: ',end='')





sorteio()
somapar(numeros)
