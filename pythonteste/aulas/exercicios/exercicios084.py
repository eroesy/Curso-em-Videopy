principal = []
temp = []
maior = menor = 0
while  True:
    temp.append(str(input(f'[ {len(principal)}° ] Nome: ').capitalize()))
    temp.append(float(input(f'({temp[0]}) Peso: ')))

    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()

    resp = input('Quer continuar?[S/N]: ').capitalize()
    if resp[0] == 'N':
        break



print(f'O registro contem {len(principal)} cadastrados!')
print(f'O maior peso registrado é: {maior}Kg. O peso de:',end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')


print(f'\nO menor peso registrado é: {menor}Kg. O peso de:',end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')


































'''lista = []
dados = []
pesos = []


while True:

    nome = str(input(f'Digite o nome do {len(lista)}° intrevistado: '))
    if nome == 'n':
        break
    dados.append(nome)

    peso = float(input(f'Digite o peso do {nome}: '))
    pesos.append(peso)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()




print(f'Ao total foram registradas {len(lista)} pessoas!')
print(f'O maior peso registrado foi {max(pesos)}. O peso de: ',end='')
for c in lista:
    if max(pesos) in c:
        print(f'[{c[0]}]', end=' ')


print(f'\nO menor peso registrado foi {min(pesos)}. O peso de: ',end='')
for c in lista:
    if min(pesos) in c:

        print(f'[{c[0]}]', end=' ')

'''