#n1 = int(input('Digite um numero inteiro'))

#for c in range(1,7):
#    a= c+n1
 #   if a % 2 == 0:
  #     print(f'A soma entre {n1} e os 6 numeros par são: {a} ')

soma = 0
cont = 0

for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 ==0:
        soma += num
        cont += 1
print(f'Voce iseriu {cont} numeros PARES eo resultado foi {soma}!')