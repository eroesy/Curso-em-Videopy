num = int(input("DIGITE UM NUMERO INTEIRO: "))
print(f"""Escolha uma das bases de conversão a seguir:
\033[33m
{'-=-'*20}                                                 

\033[32m     [ 1 ] PARA A BASE BINARIA                              
\033[32m     [ 2 ] PARA A BASE OCTAL                                
\033[32m     [ 3 ] PARA A BASE HEXADECIMAL                          
\033[33m
{'-=-'*20}                                                 
""")
opção = int(input('\033[36mDigite o numero da sua opção: \033[m'))

if opção == 1:
    print(f'\033[31m{num}\033[m em base binaria, fica: \033[34m{bin(num)[2:]}\033[m')
elif opção == 2:
    print(f'\033[31m{num}\033[m em base octal, fica: \033[34m{oct(num)[2:]}\033[m ')

elif opção == 3:
    print(f'\033[31m{num}\033[m em base hexadecimal, fica: \033[34m{hex(num)[2:]}\033[m')

else:
    print(f'\033[31mO numero {num} não atende aos requisitos!')
