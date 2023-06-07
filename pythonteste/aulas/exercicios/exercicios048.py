s = 0
count = 0
for c in range(3,500,2):
    t = c % 3

    if t ==0:
        count += 1
        s +=c

        print(c, end=' ')
        print('=',end=' ')
        print(s,end=' ')
        print('+',end=' ')

print(f'\nA soma de todos os {count} valores solicitados é: {s}')
