situ = {}

situ['Nome'] = str(input('Nome: ').capitalize())
situ['Média'] = int(input('Media: '))


if situ['Média'] == 10:
    situ['Situação'] = '\033[35m!!!!NOTAMAXIMA!!!!\033[m'

elif situ['Média'] >= 6:
    situ['Situação'] = '\033[34mAPROVADO\033[m'
elif situ['Média'] <= 6:
    situ['Situação'] = '\033[31mREPROVADO\033[m'
for k,v in situ.items():
    print(f'{k} é igual a {v}')

