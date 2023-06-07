n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
dec = n1 + (10 -1 ) * r
for c in range(n1,n1+r*10,r):
    print(c,end=' ->')
print('ACABOU')