count = soma = 0
while True:

    n = int(input('Digite um valor ou digite [ 999 ] para fechar o programa!: '))
    if n == 999:
        break
    soma += n
    count +=1

print(f'A soma é igual a: {soma}')
print(f'Você digitou {count} valores!')