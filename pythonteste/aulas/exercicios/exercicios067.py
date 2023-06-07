count = 1
resultado = 0

print(f'\033[32m=\033[m'*47)
n = int(input('\033[34mDigite um numero para eu lhe mostrar a tabuada:\033[m '))
print(f'\033[32m=\033[m'*47)
while True:
    if n < 0:
        print('\033[31mPROGRAMA FECHADO')
        break
    if count <= 10:

        resultado = n * count
        print(f'\033[33m{n} x {count:2}',end=' = ')
        print(f'{resultado:3}')
        count +=1
    if count == 11:
        count = 0
        print(f'\033[32m=\033[m'*47)
        n = int(input('\033[34mDigite um numero para eu lhe mostrar a tabuada: '))
        print(f'\033[32m=\033[m'*47)

