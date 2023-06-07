numero = int(input("Digite um número: "))
if numero <= 10:
    print("O número digitado é menor ou igual a 10")
else:
    letra = chr(numero + 86) # converte o número em letra do alfabeto
    print("O número", numero, "corresponde à letra", letra)
