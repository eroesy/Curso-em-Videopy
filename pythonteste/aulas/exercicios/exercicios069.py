dmaior =macho = femjov = 0
while True:
    print(f'='*20)
    print('CADRASTAMENTO')
    print('='*20)
    while True:
        sexo = input('SEXO[M/F]')[0]
        if sexo in 'Mm':
            macho +=1
        if sexo in 'MmFf':
            break

    while True:
        idade = int(input('IDADE: '))
        print('=' * 20)

        if sexo in 'Ff':
            if idade < 20:
                femjov += 1
        if idade > 18:
            dmaior +=1
        if idade > 0:
            break

    while True:
        esc = input('QUER CONTINUAR?[ S/N ]: ')
        print('=' * 20)
        if esc in 'SsNn':
            break
    if esc in 'Nn':
        print('CABOU')
        print('=' * 20)
        break

print(f'O total de pessoas cadastradas com mais de 18 anos é {dmaior}!')
print('*'*60)
print(f'O total de homens cadastrados foi {macho}!')
print('*'*60)
print(f'O total de mulheres com menos de 20 anos foi {femjov}!')
print('*'*60)