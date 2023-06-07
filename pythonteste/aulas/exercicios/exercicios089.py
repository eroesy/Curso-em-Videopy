'''
ficha = []
while True:
    nome = str(input('Nome:').capitalize())
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('=='*20)
print(f'{"No.":^4}{"NOME":>15}{"MEDIA":>20}')
print('=='*20)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:>14}{a[2]:>20.1f}')
while True:
    opc = int(input('Digite o numero do aluno para mais informaçoes ou digite 999 para fechar o programa!: '))

    if opc == 999:
        break
    if opc <= len(ficha)-1 :
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
'''






































cacete = 0
boletim = []
notas = []
media = []
aluno = []
maiornota = []
medias = []
aprovados =  recuperçao = total = 0
cores = {'clear':'\033[m',
         'blue':'\033[1;34m',
         'red':'\033[31m',
         'gre':'\033[32m',
         'grey':'\033[37m',
         'yello':'\033[1;33m',
         'sla':'\033[4;36m'




}






while True:
    r = 0
    nome = str(input('Digite o nome do aluno: ')).capitalize()
    if nome == 'N':
        break
    aluno.append(nome)
    maiornota.append(aluno[:])

    notas.append(float(input(f'Nota 1 do(a) {nome}: ')))
    notas.append(float(input(f'Nota 2 do(a) {nome}: ')))



    aluno.append(notas[:])
    for c in notas:
        r += c
    r = r / 2
    media.append(r)
    maiornota.append(media[:])
    aluno.append(media[:])
    medias.append(media[:])
    boletim.append(aluno[:])

    notas.clear()
    aluno.clear()
    media.clear()

print(f'{"=="*46}')
print(f'{cores["yello"]}  No.   NOME          {cores["grey"]}/{cores["yello"]}    NOTA 1    {cores["grey"]}/{cores["yello"]}   NOTA 2   {cores["grey"]}/{cores["yello"]}    MEDIA    {cores["grey"]}|{cores["yello"]}           STATUS          {cores["grey"]}|{cores["clear"]}')
print(f'{"--"*46}')
for a,c in enumerate(boletim):
    print(f'{cores["sla"]}{a+1:3}°{cores["clear"]}',end='    ')
    print(f'{c[0]:10}',end=f'    {cores["grey"]}/{cores["clear"]}   ')
    for c in c[1]:
        if c == 6:
            print(f'{cores["gre"]}',end='')
        elif c > 6:
            print(f'{cores["blue"]}',end='')
        else:
            print(f'{cores["red"]}',end='')
        print(f'  {c:4}{cores["clear"]}',end=f'    {cores["grey"]}/{cores["clear"]}   ')
        total = a + 1

    for c in boletim[a][2]:
        if c == 6:
            print(f'{cores["gre"]}',end='')
        elif c > 6:
            print(f'{cores["blue"]}',end='')
        else:
            print(f'{cores["red"]}',end='')
        print(f'  {c:4}{cores["clear"]}',end=f'    {cores["grey"]}|{cores["clear"]}')

        if c == 6:

            print(' '*3,f'{cores["gre"]}APROVADO(NOTA MINIMA){cores["clear"]}  {cores["grey"]}|{cores["clear"]}')
            aprovados += 1
        elif c > 6:
            print(' '*4,f'{cores["blue"]}APROVADO(NOTA ALTA){cores["clear"]}   {cores["grey"]}|{cores["clear"]}')
            aprovados += 1
        else:
            print(' '*2,f'{cores["red"]}RECUPERAÇÃO(NOTA BAIXA){cores["clear"]} {cores["grey"]}|{cores["clear"]}')
            recuperçao += 1


print(f'{"=="*46}')
print(f'Ao todo foram registrados {total} notas')
print(f'A media de aprovados foi de {(aprovados/total)*100}% .Com o total de {aprovados} aprovados!')
print(f'A media de reprovados foi de e {(recuperçao/total)*100}% . Com o total de {recuperçao} de recuperação!')



