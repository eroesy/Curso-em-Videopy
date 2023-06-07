n = count = maior = menor = soma =0
resposta = 'S'

while resposta == 'S':
    n = int(input('Digite um numero: '))
    resposta = input('Voce quer continuar a digitar valores?[S/N]:').upper().strip()
    count += 1
    soma += n
    if count == 1:
        menor = n
       
    if maior < n:
        maior = n
    if menor > n:
        menor = n


print(f'A media dos valores é {soma/count}\nO maior numero digitado foi {maior} é o menor é {menor}')


