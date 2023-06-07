'''n = int(input('Digite um numero: '))
c = n
f = 1
print(f'Calculando {n}! = ')
while c > 0:
    print(c,end='')
    print(' X ' if c > 1 else' = ',end='')
    f *= c
    c -= 1


print(f'{f}')
'''

n = int(input('Digite um valor: '))
f =1
for c in range(n,0,-1):
    f *= c
    print(f'{c}',end=' ')
    print(' -> 'if c >1 else ' = ',end=' ')
print(f)




