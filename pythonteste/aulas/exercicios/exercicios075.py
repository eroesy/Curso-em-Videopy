

nums = int(input('Digite um numero')),  int(input('Digite outro numero')),\
    int(input('Digite mais um numero')), int(input('Digite o ultimo numero')),

print(f'O valor 9 apareceu {nums.count(9)} vezes')

if nums.count(3) != 0:
    print(f'O 3 apareceu a primeira vez na posição {nums.index(3) + 1}')

else:
    print(f'O 3 não foi digitado em nenhuma posição!')

print(f'Os numeros pares são: ',end='')
for c in nums:
    if c % 2 == 0:
        print(c,end=' ')


