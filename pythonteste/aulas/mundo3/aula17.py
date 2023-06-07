#LISTA PARTE 1!
'''
lanche.append('cookie')

lanche.insert(0,'cookie')


del lanche[3]
lanche.pop(3)

#pelo conteudo

lanche.remove('cookie')



valores = list(ranged(4,11))
valores = [2,4,1,5,7,9,8,6]
valores.sort()
valores = [1,2,3,4,6,7,8,9]


valores.sort(reverse=True)
vai inverter

'''
'''
num = [2,5,7,9,3]
num[2] = 8
num.append(12)
num.sort(reverse=True)
num.insert(4,99)
num.pop(5)




print(num)
print(f'Essa lista tem {len(num)} elementos')
'''

valores = list()
valores.append(int(input('Digite um valor: ')))
valores.append(int(input('Digite um valor: ')))
valores.append(int(input('Digite um valor: ')))
valores.append(int(input('Digite um valor: ')))
#for cont in range(0,5):

#valores.append(int(input('Digite um valor: ')))

#print(valores)


for v in valores:
    print(f'O valor {v}...',end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')



#OBS:QUANDO LIGAR UMA LISTA EM OUTRA O PYTHON FORAM UMA LIGAÇÃO:
#a = [2,6,8,9]
#porem se fizer isso
#b = a

#b = a[:]

#é feita somente a copia
#b[2] = 999999

#print(f'fEssa é a lista A: {a}')
#print(f'Essa é a lista B: {b}')