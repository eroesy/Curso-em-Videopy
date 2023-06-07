vel = float(input('Qual a velocidade do carro em km: '))
if vel > 80:
    diff = vel - 80
    multa = diff * 7.00
    print(f'O carro foi multado no valor de: \033[31m{multa:.2f}$\033[m')
else:
    print('\033[32mO carro n será multado\[m')



