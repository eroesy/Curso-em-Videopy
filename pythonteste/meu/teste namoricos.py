import random

pessoa1 = input("Digite o nome da primeira pessoa: ")
pessoa2 = input("Digite o nome da segunda pessoa: ")

compatibilidade = random.randint(0,100)

print(f"A compatibilidade entre {pessoa1} e {pessoa2} é de {compatibilidade}%")