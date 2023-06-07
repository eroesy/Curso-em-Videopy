n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite o ultimo numero'))

#if n1 > n2 and n1 > n3:
   # print(F'{n1} É o maior numero')
#else:
   # if n1< n2 and n1 < n3:
    # print(f'{n1} É o menor numero')
#if n2 > n1 and n2 >n3:
    #print(f'{n2} É o maior numero')
#else:
    #if n2 < n1 and n2 < n3:
    # print(f'{n2} É o menor numero')
#if n3 > n1 and n3 > n2:
   # print(f'{n3} É o maior numero')
#else:
 #   if n3 < n1 and n3 < n2:
  #   print(f'{n3} É o menor numero')
menor = n3
if n1 < n2 and n1 < n3:
    menor = n2
if n2 < n1 and n2 < n3:
    menor = n2
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
print(f'O maior numero é: \033[32m{maior}\033[m')
print(f'O menor numero é: \033[31m{menor}\033[m')