'''count =0
call = 1

while True:
    n = int(input('Qual o valor a ser sacado?: '))
    while True:
        cal = n // 50
        cel50 = cal
        if cel50 > 0:
            print(f'{cel50} cedulas de R$50')
        cal= n - 50 * cel50
        if cal != 0:
            cel20 = cal // 20
            if cel20 > 0:
                print(f'{cel20} cedulas de R$20')
            cal -= cel20 * 20
            if cal == 0:
                break
            if cal > 0:
                cel10 = cal // 10
                if cel10 > 0:
                    print(f'{cel10} cedulas de R$10')
                cal -= cel10 * 10
                if cal == 0:
                    break
                if cal > 0:
                    cel1 = cal // 1
                    if cel1 > 0:
                        print(f'{cel1} cedulas de R$1')
                    cal -= cel1 *1
                    if cal == 0:
                        break
                        '''
print('='* 30)
print('{:^40} '.format('\033[32mBANCO BB\033[m'))
print('='* 30)
while True:

    n = int(input('Qual valor a ser sacado?: ',))
    print('=' * 23)
    ced50 = n // 50
    ced20 = (n % 50) // 20
    ced10  = (n%50%20)// 10
    ced1 = n%50%20%10//1

    if ced50 >0:
        print(f'Total de {ced50} cedulas de R$50')
        print('=' * 23)
    if ced20 > 0:
        print(f'Total de {ced20} cedulas de R$20')
        print('=' * 23)
    if ced10 > 0:
        print(f'Total de {ced10} cedulas de R$10')
        print('=' * 23)
    if ced1 > 0:
        print(f'total de {ced1} cedulas de R$1')
        print('=' * 23)
    else:
        break


