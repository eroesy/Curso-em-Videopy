def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f*= c
    return  f



num = int(input('Digite um valor: '))
fat = fatorial(5)
print(f'O fatorial de {num} é {fat}')