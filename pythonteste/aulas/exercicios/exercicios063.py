'''opç = int(input('escolha uma forma de usar a sequencia de fibonnaci\n DIGITE [ 1 ] para determinar o limite\n DIGITE [ 2 ] PARA DETERMINAR A QUANTIDADE DE TERMOS\n: '))

maior = 1
menor = 0
soma = 1

if opç == 1:
    n1 = int(input('Digite até que valor voce quer que  a sequencia de Fibonacci vá: '))
    while maior <= n1:

         soma = maior + menor
         print(f'{menor} -> {maior}',end=' -> ')
         if soma <= n1:
            print(f'{soma}',end=' -> ')


         if soma >= maior:
             menor = maior + soma
             maior = menor + soma
         if maior > n1:
             print(f' {n1}')

if opç == 2:
    count = 0
    qnt = int(input('Digite a quantidade de termos que voce dejesa: '))
    while count <= qnt:
     if qnt > count:

         print(f'{menor}',end='')
         menor = soma + maior
         count += 1
         if qnt > count:
             print(f' -> {maior}',end='')
             maior = soma + menor
             count += 1
             if qnt > count:
                 print(f' -> {soma}',end=' -> ')
                 soma = menor + maior
                 count += 1
'''

n1 = int(input('Digite a quantidade de termos que você deseja: '))
t1 = 0
t2 = 1
count = 3
print(f'{t1} - > {t2}',end=' ')
while count <= n1:
    t3 = t1 + t2
    print(f'- > {t2}',end=' ')
    count +=1
    t1 = t2
    t2 = t3
