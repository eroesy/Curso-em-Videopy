from datetime import date

atual = date.today().year
ano = int(input('Em que ano você nasceu?: '))
idade = atual - ano

print(f'Em {atual} vc tem {idade} anos')

if idade <= 9:
    print(f'Com {idade} anos, você esta na categoria \033[36mMIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos. Voce esta na categoria \033[32mINFANTIL')
elif idade <= 19:
        print(f'Com {idade} anos. Voce esta na categoria \33[34mJUNIOR')
elif idade <= 25:
    print(f'Com {idade} anos. Você esta na categiria \033[33mSÊNIOR')
else:
    print(f'Com idade de {idade}. Você esta na categoria \033[31mMASTER')
