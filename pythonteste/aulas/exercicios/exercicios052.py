#n1 = int(input('Digite um numero inteiro: '))

#n2 = n1%2%3%5%11

#if n2 != 0 or n1 == 2 or n1 == 9 or n1 == 1 :
 #   print(n2)
  #  print('O numero é primo')
# else:
 #   print('O numero n é primo')

num = int(input('Digite um numero: '))
cont = 0

for c in range(1,num + 1):
     if num % c == 0:
        print('\033[34m',end=' ')
        cont += 1
     else:
        print('\033[31m',end=' ')
     print(f'{c}',end=' ')
if cont <= 2:
    print(f'\n\033[32m{num}\033[34m é um numero primo')
else:
    print(f'\n\033[332m{num}\033[31m não é primo, pois ele é divivel por \033[35m{cont}\033[34m numeros'
          f'')



