from datetime import  date
maior = 0
menor = 0
atual = date.today().year
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento'))
    idade = ( atual - ano )
    print(idade)
    if idade >= 18:
        maior = maior + 1
    else :
        menor = menor + 1


print(f'Ao total são maiores {maior}')
print(f'Ao total são menores {menor}')
print('Fim')