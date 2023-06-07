print('Dê os segmentos seguintes')

seg1 = float(input('Qual o tamanho do 1° segmento?: '))
seg2 = float(input('Qual o tamanho do 2° segmento?: '))
seg3 = float(input('Qual o tamanho do 3° segmento?: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print('Com os seguimentos acima pode-se fazer um triangulo!')
    if seg1 == seg2 == seg3:
        print('O triangulo formado será EQUILÁTERO!')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('Podera se formar o triangulo ISÓCELES!')
    else:
        print('Todos os lados são diferentes. Sendo assim se formara o triangulo Escaleno!')

