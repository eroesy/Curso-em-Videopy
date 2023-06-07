
n = int(input('Digite um numero de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente um numero de 0 a 20: '))
extenso = 'zero', 'um', 'dois', 'Três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
    'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete','dezoito', 'dezenove',\
    'vinte'


print(f'Voce digitou {extenso[n]}')
