matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = maior = lsoma = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Valor para [{l},{c}]: '))

print('=='*30)

for l in range(0,3):
    for c in range(0,3):
        if c == 2:
            lsoma += matriz[l][c]
        if c == 0 and l == 1:
            maior = matriz[l][c]
        elif matriz[1][l] > maior:
            maior = matriz[1][l]
        if matriz[l][1] % 2 ==0:
            spar += matriz[l][c]

        print(f'[{matriz[l][c]}] ',end='')
    print()
print('==' * 30)
print(f'A soma dos numeros pares é {spar}!')
print(f'O maior numero da linha 2 é {maior}')
print(f'a soma da linha 2 é {lsoma}')































'''matriz = []
linha = []
linha1 = []
linha2 = []
soma = []
s = v = par = 0

for c in range(0,9):
    n = int(input('Digite o valor: '))


    if c < 3:
        linha.append(n)
    elif c < 6:
        linha1.append(n)
    else:
        linha2.append(n)


matriz.append(linha)
matriz.append(linha1)
matriz.append(linha2)
for c in matriz:
    print(f'{  c  }')

r = matriz[0] + matriz[1] +matriz[2]
for c in r:
    s += c

print(f'A soma de todos os valores das matrizes é: {s}')
print(f'O maior valor da segunda linha é: {max(linha1)}')

soma = matriz[0][2]+matriz[1][2]+matriz[2][2]
print(f'A soma da segunda coluna é {soma}')

for c in matriz:
   for f in c:
       if f % 2 ==0:
           par += f

print(f'A soma dos numeros pares é: {par} ')'''