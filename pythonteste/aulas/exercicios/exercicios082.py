a = []
par = []
impar = []
while True:
    a.append(int(input('Digite um valor: ')))
    r = input('QUER CONTINUAR[S/N]: ')
    if r in 'Nn':
       break

for c in a:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-='*30)
print(f'A lista digitada foi: {a}')
print(f'A lista com numeros pares é: {par}')
print(f'A lista com numeros impares é: {impar}')
print('-='*30)

