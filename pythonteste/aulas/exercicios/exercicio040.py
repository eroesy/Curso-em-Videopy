n1 = float(input('Qual a sua primeira nota?: '))
n2 = float(input('Qual a sua segunda nota?: '))
n3 = float(input('Qual a sua terceira nota?: '))

media = (n1 + n2 + n3) / 3
if 5 <= media <= 6.9:
    print(f'A media do aluno em recuperação é de: {media:.1f}!')
elif media >= 7:
    print(f'A media do aluno aprovado é de: {media:.1f}!')
else :
    print(f'A media do aluno reprovado é de: {media:.2f}!')
