c = float(input('Qual o valor da casa?: R$'))
s = float(input('Qual o seu salario do comprador?: R$ '))
q = int(input('Sabendo-se que, a prestação mensal \033[31mnão pode exceder 30% do salario\033[m. Digite em quantos anos pretende financiar o imovel: '))

pres = c /q /12

taxa = s*30/100

if pres > taxa:
    print('\033[31mO empréstimo não poderar ser aceito\033[m')
    print(f'Ja que o a parcela ficaria no valor de: \033[34mR${pres:.2f}\033[m. Sendo seu 30% do seu salario correspodente a \033[36mR${taxa:.2f}.')
elif pres <= taxa:
    print('\033[32mParabens o empréstimo sera aceito!\033[m')
    print(f'A parcela ficarar no valor de: \033[33mR${pres:.2f} ao mês \033[m')

