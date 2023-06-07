'''
teste = []
teste.append('Gustavo')
teste.append(22)

galera = []
galera.append(teste[:]) # [:] para copiar se não fazer isso, vai criar uma ligação(elas serão iguais todo o tempo!)
teste[0] = 'laura'
teste[1] = 34
galera.append(teste[:])
print(galera)
'''
lista = []
dados = [2,3,4,5,6,7,8,9,10]
lista.append(dados[:])

print(lista)