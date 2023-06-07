total = count = barato1 = barato = mil = 0

print('.'*20,'CADASTRO FODA','.'*20)

while True:
    produto = input('Qual o nome do produto?: ')
    preço = float(input('Qual o preço do produto?: '))
    total += preço
    if preço > 1000:
        mil += 1

    count += 1

    if count == 1:
        barato = produto
        barato1 = preço

    if barato1 > preço:
        barato1 = preço
        barato = produto



    ir = input('Quer continual?[S/N]:')


    if ir in 'Nn':

        break

print(f'O total da compra é R${total}!')
print(f'São {mil} produtos que custam mais de R$1000 ')
print(f'O produto mais barato é o {barato} que custa R${barato1}')