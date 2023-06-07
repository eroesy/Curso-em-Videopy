print('\033[4;31m===='*18,'LOJAS MATEUS','===='*20)
#loja = 'LOJAS MATEUS'
#print(f'{loja:=^160}')

pr = float(input('\033[mQual o valor da compra?:R$ '))
print(''' a forma de pagamento?
[ 1 ] PARA A VISTA DINHEIRO/ CHEQUE!
[ 2 ] PARA A VISTA NO CARTÃO!
[ 3 ] PARA EM ATÉ 2X NO CARTÃO
[ 4 ] PARA 3X OU MAIS NO CARTÃO!''')

pag = int(input('Digite um numero correspondente a forma de pagamento escohlida!: '))

cores = {'Verde':'\033[32m',
         'Vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'limpar':'\033[m',
}

if pag == 1:
  pr = pr - 10 / 100 * pr
  print('O modo de pagamento oferece {}10% de desconto{}'.format(cores['amarelo'],cores['limpar']))
  print(f'Assim o preço final saira no total de \033[32mR${pr:.2f}!\033[m')
elif pag == 2:
    pr = pr - 5 /100 * pr
    print('O modo de pagamento oferece \033[33m5% de descontoz\033[m')
    print(f'Assim o prexo final saira no total de \033[32mR${pr:.2f}\033[m!')
elif pag == 3:
    print('O modo de pagamento solicitado não ha de alerar o valor final!')
    print(f'Sendo assim o valor final saira no total de \033[33mR${pr:.2f}!\033[m')
elif pag ==4:
    par = int(input('Quantas parcelas deseja pagar?: '))
    pr1 = pr + 20 /100 * pr
    par1 = pr1 / par
    print('O modo de pagamento selecionado oferece \033[33m20% de juros!\033[m')
    print(f'Sua compra de \033[32mR${pr:.2f}\033[m vai ficar no valor final de \033[31mR${pr1:.2f}\033[m')
    print(f'Parcelado em \033[36m{par}X\033[m de \033[31mR${par1:.2f}. COM JUROS\033[M')
else:
    print('Informe o numero certo \033[31mBURRÃO!!!\033[m')