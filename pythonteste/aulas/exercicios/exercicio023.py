numero = int(input('Digite um numero de 0 a 9999: '))
#unidade = str(int(numero) // 1)
#dezena = str(int(numero) // 10)
#centena = str(int(numero)//100)
#milhar = str(int(numero) // 1000)
#print(f'unidade: = ',{unidade[len(unidade)-1]})
#print(f'dezena: = ',{dezena[len(dezena)-1]})



#print('Centena: = ',{centena[len(centena)-1]})
#print('Milhar: = ',{milhar[len(milhar)-1]})
##print(dezena)
#print(len(dezena)-1)
#print(len(dezena))
#print(dezena[len(dezena)-1])





#forma do video

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10




print(f'\033[36;40mUnidade: \033[36;40m{u}')
print(f'dezena: \033[36;40m{d}')
print(f'centena: \033[36;40m{c}')
print(f'milhar: \033[36;40m{m}')