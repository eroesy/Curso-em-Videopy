matriz = [[0,0,0],[0,0,0,],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para a posição [{l}],[{c}]'))
print('=='*15)
for l in range(0,3):
    for c in range(0,3):
        print(f' [{matriz[l][c]:^6}] ',end='')
    print()
print('=='*15)




























'''lista =  []
linha =  []
linha1 = []
linha2 = []
count = 0
count1 = 0
for c in range(0,9):

    if count > 2:
        count = 0
        count1 += 1
        if count1 == 3:
            count1 =0
    n = int(input(f'Digite o valor para [{count1},{count}]'))
    if c < 3:
        linha.append(n)
    elif c < 6:

        linha1.append(n)
    else:
        linha2.append(n)


    count += 1
lista.append(linha[:])
lista.append(linha1[:])
lista.append(linha2[:])


for c in lista:
    print(f'{" "*10}[ \033[34m{c}\033[m ]')'''