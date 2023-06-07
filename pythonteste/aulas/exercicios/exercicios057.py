
s = str(input('Digite seu sexo: ')).upper().strip()[0]
print(s)
while s not in 'MmFf':
    if s != 'F' or s != 'M':
        s = input('Digite seu sexo novamente: ').upper().strip()[0]

    if s == 'M':
            print(f'Você é boyzin')
            print(s[0::])
    if s == 'F':
            print('Você é boyzinha')


