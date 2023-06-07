'''
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))

print(f'O maior valor é {max(valores)} nas posições ', end='')
for m, v in enumerate(valores):


    if max(valores) == v:
        print(f'{m}...', end='')

print(f'\nO menor valor é {min(valores)} nas posições ', end='')
for m, v in enumerate(valores):


    if min(valores) == v:
        print(f'{m}...', end='')

'''




valores = []

for c in range(0,5):

    valores.append(int(input(f'Digite um valor na posição {c}: ')))

print(f'O maior valor foi {max(valores)} nas posiçoes: ',end='')

for p,v in enumerate(valores):

    if v == max(valores):

        print(f'{p}...',end='')


print(f'\nO menor valor foi {min(valores)} nas posiçoes: ',end='')

for p, v in enumerate(valores):

    if min(valores) == v:

        print(f'{p}...',end='')

















