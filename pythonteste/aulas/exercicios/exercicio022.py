nome = str(input('Difite seu nome completo: ')).strip()


print('Seu nome em maiusculas fica:',nome.upper())


print('seu nome em minusculas fica: ',nome.lower())
print('Seu nome tem o total de letras: ',len(nome)-nome.count(' '))
div = nome.split()
l = len(div[0])
print(f'Seu primeiro nome tem o total de letras igual a:\033[33;40m{l}\033[m ')
print ('Seu primeiro nome sem espaço',nome.find(' '))