soma = count = 0
n = int(input('Digite um numero ou digite 999 para fechar o programa: '))
while n != 999:
        soma += n
        count +=1
        n = int(input('Digite um numero ou digite 999 para fechar o programa: '))
print(f'A quantidade de numero digitado foi: {count}\nA soma deles é igual a {soma}')