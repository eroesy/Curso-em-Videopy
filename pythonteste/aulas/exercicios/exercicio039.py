import datetime
data = datetime.date.today().year
print("""
Digite [ 1 ] se seu sexo biologico é masculino!
Digite [ 2 ] se seu sexo biologico é feminino!

""")
sexo = int(input('DIGITE O NUMERO DE SUA OPÇÃO: '))

if sexo == 1:


    ano =int(input('Em que ano voce nasceu?: '))
    idade = data - ano
    print(f'em {data} você tem {idade}')
    if idade == 18 :
        print(f'Esta na hora de voce se alistar!')
    elif idade < 18:
        print(f'Falta {18 - idade} anos pra você se alistar')
        print(f'Seu alitstamento sera em {data + 18 + idade}')
    elif idade > 18:
        print(f'Ja passou {idade - 18} anos do  alistamento: ')
        print(f'Seu alistamento foi {data - 18 + idade}')
else:
    print('Você não é obrigada aa se alistar!')