n = input(print('Digite seu nome completo: ')).strip()
b = n.split()
c = len(b)

print(f'O primeiro nome é: {n.split()[0]}')
print(f'O ultimo nome é: {n.split()[c-1]}')
