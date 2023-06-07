tabuada = 'TABUADA'
print(F'{tabuada:-^100}')

n = int(input('Escolha a tabuada: '))

for c in range(1,11,):
    re = n * c
    print(f'{n} x {c:2} = {re:2}')



