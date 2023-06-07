lista = []
r = count = 0
while True:
    n = int(input('Digite um valor: '))


    if count == 0 or n <= lista[-1]:
        lista.append(n)

    else:
        pos = 0
        while pos <= len(lista):
            if n > lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1



    count += 1
    r = input('Quer continuar?[S/N]: ')
    if r in 'Nn':
        break



print(f'Os elemtenso digitados foram{count}')
print(f'A lista em ordem decrescente é:{lista} ')
if lista.count(5) !=0:
    print('O 5 apareceu! E na posição',end=' ')
    for i,c in enumerate(lista):
        if c == 5:
            print(f'{i}...',end='')
else:
    print('O 5 não foi digitado')



