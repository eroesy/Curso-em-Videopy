c = ('\033[m',  # 0 - sem cor
     '\033[31m',  # 1 - vermelho
     '\033[32m',  # 2 - verde
     '\033[33m',  # 3 - azul
     '\033[7m', # 4 - preto e branco
     )
def printo(sexo,cor=0):

    from time import sleep
    print(c[cor])
    print('~' * (len(sexo)+4))
    print(f'  {sexo}')
    print('~' * (len(sexo)+4))
    print(c[0])
    sleep(1)



def ajuda(com):
    print(f'Acessando o manual do comando \'{com}\'')
    print(c[4])
    help(com)
    print(c[4])


while True:
    printo('SISTEMA DE AJUDA PYHELP',2)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

printo('ATÉ LOGO', 1)