nums = [[],[]]



for c in range(1,8):
    valor = int(input(f'[ {c} ]° Valor '))
    if valor % 2 == 0:
        nums[0].append(valor)
    else:
        nums[1].append(valor)

print(f'=='*30)
nums[0].sort()
nums[1].sort()
print(f'Os valores pares são: {nums[0]}')
print(f'Os valores impares são: {nums[1]}')
print(f'=='*30)




























'''
impar = []
par = []
lista = []

for c in range(1,7):
    n = int(input(f'Digite o {c}° valor!: '))
    if n % 2 == 0:
       par.append(n)
    else:
        impar.append(n)

lista.append(par[:])
lista.append(impar[:])


print(f'O numeros pares são {sorted(lista[0])}')
print(f'Os numeros impares são {sorted(lista[1])}')'''