def escreva(txt):
    print("~"*(len(txt)+4))
    print(f'  {txt}')
    print("~"*(len(txt)+4))

while True:
    escreva(str(input('Digite um frase: ')))