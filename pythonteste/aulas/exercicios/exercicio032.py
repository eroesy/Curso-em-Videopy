
from datetime import date
a = int(input('digite um ano para analisar! Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f' O ano de {a} É um ano bissexto')
else:
    print(f'Ó ano de {a} não é um ano bissexto')