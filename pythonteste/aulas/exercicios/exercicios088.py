from random import randint
from time import  sleep
bs = ' BOA SORTE '
print('=='*30)
palpites = int(input('Digite quantos palpites você quer fazer: '))
print('=='*30)
lista = []
palpite = []

for c in range(0,palpites):
    for i in range(0,6):
        while True:
            n = randint(1,60)
            if palpite.count(n) == 0:
                palpite.append(n)
                palpite.sort()
                break
            else:
                print('omg')


    lista.append(palpite[:])
    palpite.clear()
print('=='*9,f' SORTEANDO {palpites} JOGOS ','=='*9)
for i,c in enumerate(lista):
    sleep(0.5)
    print(f'O {i+1}° jogo é: {c} ')
print(bs.center(57,'='))