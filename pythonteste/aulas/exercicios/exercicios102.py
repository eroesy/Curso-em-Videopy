def fatorial(n,show=False):
    """
    ->Calculo o Fatorial de um número.
    :param n: O numero a ser calculado.
    :pram show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.




    """

    print('=='*20)
    f =1
    for c in range(n,0,-1):
        if show == True:
            print(f'{c} X ',end='')
        f*=c

    f+=1
    if show == True:
        print('= ',end='')
    print(f'{f-1} ',end='')



fatorial(5,True)
print()
help(fatorial)