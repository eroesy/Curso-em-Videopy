def notas(*num,sit=False):
    """
    -> função para analisar as notas dos alunos
    :param n: uma ou mais notas dos alunos(aceita varias)
    :param sit: opicional, idicando se deve ou não mostrar a situação.
    :return: dicionario com varias informaçoes da turma


    """
    maior = menor = soma =0
    dic = {}
    for i,c in enumerate(num):
        if i == 0:
            maior = c
            menor = c
        elif c > maior:
            maior = c
        elif c < menor:
            menor = c

        dic['Total'] = i +1
        dic['Maior'] = maior
        dic['Menor'] = menor
    media = sum(num) / len(num)
    dic['Media'] = media
    if sit == True:
        if media >6:
            dic['Situação'] = 'Aprovado'
        elif media == 6:
            dic['Situação'] = 'Recuperação'
        elif media <6:
            dic['Situação'] = 'Reprovado'

    return dic


resp = notas(1,2,3,4,5,6,7,8,sit=True)
print(resp)
help(notas)
resp = notas(6,6,sit=True)
print(resp)
