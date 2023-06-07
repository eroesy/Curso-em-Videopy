'''estados = {}
brasil = []
for c in range(0,2):
    estados['uf']=str(input('Digite o estado: '))
    estados['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estados.copy())

for c in brasil:

    #for k, v in c.items():

        #print(f'O estado {k} é represeentado por {v}')
    for v in c.values():
        print(v,end=' ')
    print()
'''
d={'oi':1}
print(d['oi'])





