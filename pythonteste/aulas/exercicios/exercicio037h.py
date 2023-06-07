d = int(input('Digite um numero '))
print('Digite 1 para transformar o numero em base binaria')
print('Digite 2 para transformar o numero em base octal')
print('Digite 3 para transformar o numero em base hexadecimal')
e = int(input('Digite aqui a sua escolha: '))

if e == 1:
   da = d //2 # 6

   d0 = d % 2 # 1

   db = da // 2 # 3

   d1 = da % 2  # 0

   dc = db // 2  # 1

   d2 = db % 2

   dd = dc // 2

   d3 = dc % 2

   de = dd // 2

   d4 = dd % 2

   print(f'a posição {d}° na base decimal equivale a{d4,d3,d2,d1,d0} em formato binario')

if e == 2:
   da = d // 8

   d0 = d % 8

   db = da // 8

   d1 = da % 8

   dc = db // 8

   d2 = db % 8

   dd = dc // 8

   d3 = dc % 8

   de = dd // 8

   d4 = dd % 8

   print(f'A posição {d}° na base decimal equivale aos numeros{d4,d3,d2,d1,d0} em formato octal')

if e == 3:
   da = d // 16

   d0 = d % 16

   db = da // 16

   d1 = da % 16

   dc = db // 16

   d2 = db % 16

   dd = dc // 16

   d3 = dc % 16

   de = dd // 16

   d4 = dd % 16




   print(f'A posição {d}° na base decimal equivale aos numeros {d4,d3,d2,d1,d0} na base hexadecimal')