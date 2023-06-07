from time import sleep
vazio =' '*48
print(vazio,end='')
n0 = int(input('Digite um numero: '))
print(vazio,end='')
n1 = int(input('Digite outro numero: '))
ply = 0
balls = 'CALCUBALLS'

while ply != 5:
    maior = n0


    print(f'''
                                                {balls:=^30}
                                                [ 1 ] SOMAR
                                                [ 2 ] MUTIPLICAR
                                                [ 3 ] MAIOR
                                                [ 4 ] NOVOS NÚMEROS
                                                [ 5 ] SAIR DO PROGRAMA
                                                {balls:=^30}
     ''')
    print(vazio,end='')

    ply = int(input('Digite a opção escolhida: '))

    if ply == 1:
        print(vazio, end='')
        print(f'A soma dos dois numeros ditados é {n0 + n1}')

    elif ply == 2:
        print(vazio, end='')
        print(f'A mutlipicaçao dos valores digitados é {n1 * n0}')
    elif ply == 3:
        if maior > n1:
            print(vazio, end='')
            print(f'O maior é {maior}')
        else:
            print(vazio, end='')
            print(f'O maior é{n1}')
    elif ply == 4:
      print(vazio, end='')
      n0 = int(input('Digite um numero: '))
      print(vazio, end='')
      n1 = int(input('Digite outro numero: '))
    elif ply ==5:
        print(vazio, end='')
        print('Ah')
        sleep(0.6)
        print(vazio, end='')
        print('Você já esta indo! T-T')


    else:
        print(vazio, end='')
        print('Opção invalida. Tente novamente:) ')
    sleep(0.6)







