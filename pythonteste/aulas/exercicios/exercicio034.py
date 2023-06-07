sa = float(input('Qual o seu salario?'))

if sa > 1250:
    print(f'Seu novo salario é de: {sa + sa * (10/100)}$')
else:
    print(f'Seu novo salario é de: {sa + sa * (15/100)}$')