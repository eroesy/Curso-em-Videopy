pilh = []
exp = str(input('Digite uma expressão: '))

for c in exp:
    if c == '(':
        pilh.append(c)
    elif c == ')':
        if len(pilh) > 0:
            pilh.pop()
        else:
            pilh.append(')')
            break
if len(pilh) == 0:
    print('Sua expressão esta certa!')
else:
    print('\033[3;31m*ERROR SUA EXPRESSÃO ESTA ERRADA ERROR*!')























'''lista = []
prsd = 0
prse = 0

exp = str(input('Digite um expressão: '))
for letras in exp:
    lista.append(letras)


prsd = lista.count('(')
prse = lista.count(')')
if prsd != prse:
    print('EXPRESSÃO INCORREETA')
'''

