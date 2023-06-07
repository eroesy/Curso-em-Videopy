def leiaint(sint):
    while True:
        ler = input(sint).strip()
        if ler.isnumeric():
            break
        print('\033[31mERROR digite um numero apropriado!\033[m')
    return ler


n = leiaint('Digite um numero: ').strip()
print(f'\033[32mVocê acabou de digitar o numero {n}.')
