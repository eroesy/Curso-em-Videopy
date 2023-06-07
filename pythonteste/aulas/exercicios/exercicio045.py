from emoji import emojize
import time
import random




print('Oi eeeeeeeeeeeeee. Vamos jogar jokenpô ebaaa')

print(emojize('Digite tesoura para :scissors:',language = 'alias'))
print(emojize('digite pedra para :moai:'))
print(emojize('Digite papel para :newspaper:'))

t = (emojize(':scissors:'))
pa = (emojize(':newspaper:'))
pe = (emojize(':moai:'))



ec = input('Escolha um: ').upper().strip()
lista = ('TESOURA','PAPEL','PEDRA')
pc = random.randint(0,2)

time.sleep(0.6)
print('JO ')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')



print(f'O computador jogou {lista[pc]}')
print(f'Voce jogou {ec}')

vt = '\033[32mVocê ganhou\033[m ebaaa!!!'
dt = '\033[31mVocê perdeu\033[m T-T'
et = '\033[36mVocê empatou \033[m'
if ec == 'TESOURA':
    if pc == 1:
        print(t,' X ',pa)
        print(vt)
    elif pc == 2:
        print(t,' X ',pe)
        print(dt)
    else:
        print(t,' X ',t)
        print(et)
elif ec == 'PAPEL':
    if pc == 2:
        print(pa,' X ',pe)
        print(vt)
    elif pc == 0:
        print(pa,' X ',t)
        print(dt)
    else:
        print(pa,' X ', pa)
        print(et)
elif ec == 'PEDRA':
    if pc == 0:
        print(pe,' X ',t)
        print(vt)
    elif pc == 1:
        print(pe,' X ', pa)
        print(dt)
    else:
        print(pe,' X ', pe)
        print(et)
else:
    print('Voce digitou errado, lerdão')