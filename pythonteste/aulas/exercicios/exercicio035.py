print('Der os valores dos lados')
l1 = float(input('segmento 1: '))
l2 = float(input('segmento 2: '))
l3 = float(input('segmento 3: '))


#if l1 >= l2 and l1 >= l3:
  #  if l2 + l3 >=l1:
       # print('Com os seguimentos acima pode-se fazer um triangulo!')
#if l2 >= l1 and l2 >= l3:5
 #   if l1 + l3 >= l2:
#        print('Com os seguimentos a cima pode-se fazer um triangulo!')
#if l3 >= l1 and l3 >= l2:
   # if l1 + l2 >= l3:
  #      print('Com os seguimentos a cima pode-se fazer um triangulo!')
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:

      print('Com os seguimentos acima pode-se fazer um triangulo!')
else:

    print('Não da pra se fazer um triangulo!')


