primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
count = 0
limite = 0
mais = 10

while mais !=0 :
    limite += mais
    while count <= limite:
        primeiro += razão
        count += 1
        print(f'[{primeiro:^6}]')
    print('PAUSA')
    mais = int(input('Digite quantos valores a mais voce deseja: '))
print(f'PA feita com {limite} termos mostrados!')







'''if count == limite:
        razão = int(input('Quer continuar?\n Digite um novo numero para a razão\n Ou digite [ 0 ] para fechar o programa!'))
        count = 0
        s = input('Que mudar a quantidade de valores?[S/N]: ').upper().strip()
        if s == 'S'and razão != 0:
            limite = int(input('Digite o novo valor da quantidade de valores: '))'''