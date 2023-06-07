valores = []
while True:
    valores.append(int(input('Digite um valor: ')))

    for c,m in enumerate(valores):
        if c >= 1:
            if valores.count(valores[c]) > 1:
                print('Valor duplicado não adicionado')
                valores.pop()
            elif valores.count(valores[c] <=1):
                print('Valor adicionado com sucesso!')

    res = input('Quer continuar?[S/N]: ')
    if res in 'Nn':
        print(f'{"-"*50}')
        print('APLICATIVO FECHADO')
        print(f'Voce digitou os valores {sorted(valores)}')
        break
