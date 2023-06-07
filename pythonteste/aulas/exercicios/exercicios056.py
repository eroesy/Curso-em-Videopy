'''
idade2 = 0
idade = 0
n = 0
velho = 0
velh = 'seu pai'
abaixo = 0

for c in range(1,5):
 pessoa = f'{c}ªPESSOA'
 print(f'{pessoa:=^40}')
 nome = input('Qual o seu nome?: ')
 idade = int(input('Qual sua idade?: '))
 sexo = input('Qual seu sexo[F/M]?: ').upper()
 n = nome,idade,sexo

 if 'M' in n:
  if n[1] > velho:
   velho = n[1]
   velh = n[0]
  print(velho,velh,n)
 if 'F' in n:
  if n[1] < 20:
    abaixo += + 1

 idade2 =+ idade




#print(f'O homem mais velho tem {maior} anos eo mais novo tem {menor} anos!')
print(f'{abaixo} mulheres possuem idade menor que 20 anos')
print(f'A media entre as idades do grupo é de {idade2/4:.0f} anos')
print(f'{velh.capitalize()} com {velho} anos. É o homem mais velho do grupo')
'''
maior= 0
menor = 0
media = 0
velho = 0
idade = 0
totmulher = 0
for c in range(1,6):
 nome = input('Digite o nome: ')
 idade = int(input('Digite a idade'))
 sexo = input('Digite o sexo[F/M]')

 media += idade
 if c == 1 and sexo in 'Mn':
  maior = idade
  velho = nome
 if sexo in 'Mm' and  idade > maior:
  maior = idade
  velho = nome
 if sexo in 'Ff' and idade < 20:
  totmulher =+ 1

print(f'a media de idade do grupo é {media/5}')
print(f'O {velho} é o homem mais velho do grupo ten {maior} anos')
print(f'No grupo existe {totmulher} mulheres com menos de 20 anos')
