frase = str(input('Digite uma frase: ')).strip('')
frase1 = frase.replace(' ',"").upper()
frase2 = frase1[::-1]


' '.join(frase1)
' '.join(frase2)
print(frase1)
print(frase2)
if frase2 == frase1[::1]:

   print(f'A frase {frase} é um palindromo, pois o inverso de {frase} é {frase2}')
else:
    print(f'Não é um palindromo, pois o inverso de {frase} é {frase2}')

#resultado no curso

'''frase =input('Digite uma frase: ').strip()
palavras = frase.split()
junto = ''.join(palavras).upper()
inverso = ''
for letra in range(len(junto) -1,-1,-1 ):
    inverso += junto[letra]#importar letra fora do laço
print(junto,inverso)
if inverso == junto:
    print(f'Temos um palindromo, pois a palavra: {frase}, invertida fica: {frase}')
else:
    print('Não é um palindromo')'''

