from datetime import date

ano = date.today()

cadastros = {}
cadastros['Nome'] = str(input('Nome: ').capitalize().strip())
nasc = int(input('Ano de nascimento: '))
cadastros['Idade'] = ano.year - nasc
ctps = int(input('Carteira de trabalho (0 Não tem): '))
if ctps != 0:
    cadastros['ctps'] = f'Possui: {ctps}'
    cadastros['contratação'] = int(input('Ano de contratação: '))
    cadastros['Salário'] = int(input('Salário: '))
    cadastros['Aposentadoria'] =f"{((cadastros['Idade'])  + (cadastros['contratação'] + 35)- ano.year)} anos"
else:
    cadastros['ctps'] = 'Não possui.'
print('=='*30)
for k,v in cadastros.items():
    print(f' - {k} = {v}')
print('=='*30)

