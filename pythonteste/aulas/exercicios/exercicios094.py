from time import sleep

cadastro = []
ficha = {}
soma =  count = 0

while True:
    ficha['nome'] = str(input('Nome: ').capitalize())
    while True:
        ficha['sexo'] = str(input('Sexo[M/F]: ').capitalize())
        if ficha['sexo'] in 'MF':
            break
        print('Por favor digite F ou M')
    ficha['idade'] = int(input('Idade: '))
    resp = str(input('Quer continuar?: '))
    cadastro.append(ficha.copy())
    soma += ficha['idade']
    media = soma / (len(cadastro))


    ficha.clear()
    if resp in 'Nn':
        break
print(f'Foram cadastrados {len(cadastro)} pessoas.')
print(f' - A media das idades dos intregrantes é: {media}.')
print(f' - \nAs mulheres cadastradas foram: ',end='')
for i,c in enumerate(cadastro):
    if c['sexo'] == 'F':
        for k,v in c.items():
            if k == 'nome':
                print(f'[{v}] ',end='')
print('.')
print(f'Lista das pessoas que estão acima da media:')
for i,c in enumerate(cadastro):
    if c['idade'] > media:
        count += 1
        for k,v in cadastro[i].items():
             print(f' - {k} = {v}; ',end='')
        print('\n')

palavra = '<<ENCERRANDO>>'
for letra in palavra:
    print(letra,end='')
    sleep(0.3)


'''
print(cadastro)
print('<< ',end='')
sleep(0.5)
print('E',end='')
sleep(0.3)
print('N',end='')
sleep(0.3)
print('C',end='')
sleep(0.3)
print('E',end='')
sleep(0.3)
print('R',end='')
sleep(0.3)
print('R',end='')
sleep(0.3)
print('A',end='')
sleep(0.3)
print('N',end='')
sleep(0.3)
print('D',end='')
sleep(0.3)
print('O',end='')
sleep(0.5)
print(' >>',end='')
        '''