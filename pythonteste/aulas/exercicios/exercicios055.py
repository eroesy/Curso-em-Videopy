'''a = 0
maior = 0
menor = 1000
for c in range(0,2):
    peso = float(input('Informe o peso: '))
    peso1 = float(input('Informe o peso: '))

    if peso > peso1:
        maior = peso
        if peso1 < menor:
            menor = peso1
    elif peso1 > maior:
        maior =peso1
        if peso < menor:
            menor = peso'''



maior = 0
menor = 0

for p in range(1,6):
    peso = input(f'Digite o peso da {p}ª pessoa: ')
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso









print(f'O maior peso lido foi {maior}kg eo menor foi {menor}kg')



