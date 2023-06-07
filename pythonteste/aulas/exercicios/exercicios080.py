lista = []
for c in range(0,10):
    n = int(input('Digite um valor: '))

    if c == 0 or n >= lista[-1]:
        lista.append(n)
        print('O valo foi adicionado no primeiro lugar da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if n < lista[pos]:
                lista.insert(pos,n)
                print(f'O valor foi adicionado na posição {pos}°!')
                break
            pos += 1
print(lista)


lista = []


















''' lista.append(int(input('\nDigite um valor')))

    print('O valor foi adicionado', end='')
    if lista[c] == max(lista):
        print('na ultima posição da lista!', end='')


    elif lista[c] == min(lista):

        lista.insert(0, lista[c])
        lista.pop()
        print('na primeira posição da lista')


    elif c > 2 and lista[c] < max(lista):
        if lista[2] < lista[c]:
            lista.insert(3, lista[c])
            lista.pop()
            print(f'na 3° posição da lista!')

        if lista[(c - 2)] < lista[c] < lista[(c - 1)]:
            lista.insert(2, lista[c])
            lista.pop()
            print(f'na 2° posição da lista!')

    if lista[c] < lista[(c - 1)]:
        if min(lista) < lista[c] < max(lista):
            lista.insert(1, lista[c])
            lista.pop()
            print('na 1° posição da lista!')
'''
print(lista)
