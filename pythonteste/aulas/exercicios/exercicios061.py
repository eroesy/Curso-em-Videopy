n1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
r1 = n1
count = 0
while count != 10:

    count += 1
    r1 += r
    print(r1, '->' if count < 10 else '-> FIM', end=' ')
print(f'\nEssa é a PA do primeiro 10 termos {n1} e da razão {r}!')