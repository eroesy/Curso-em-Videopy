a = str(input('Digite um frase: ')).strip().upper()
print(f'A primeira vez que aparece a letra a é no',a.find('A')+1,'°caracter')
print('A letra a aparece:',a.count('A'),'vezes.')
print(f'A letra a aparece por ultimo no:',a.rfind('A')+1,'°caracter')
