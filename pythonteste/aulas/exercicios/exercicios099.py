from time import sleep

def maior(*num):
    print('==' * 15)
    print('Analizando os valores passados...')
    maior = 0
    for i,c in enumerate(num):
        print(f'{c} ', end='')
        sleep(0.3)
        if i == 0:
            maior = c
        elif c > maior:
            maior = c


    print(f'Foram informados {len(num)} valores')
    if len(num) > 0:
        print(f'O maior valor informado foi: {maior}.')
    else:
        print('Não ha numeros!')
    print('=-='*15)
    sleep(0.3)


maior(8,9,1)
maior()
maior(2,2,1,3,4,5,6,7,8,9,14,23,1231312313,1,2,3,4,7,8,9,0,123,34,565,78)