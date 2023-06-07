peso = float(input('Qual o seu peso?:(Kg) '))
altura = float(input('Qual a sua altura?:(M) '))

imc = peso / (altura ** 2)

print(f'O seu imc é: \033[34m{imc:.1f}\033[m')

if imc < 18.5:
    print('Você esta abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você esta no \033[32mpeso ideal!')
elif 25 <= imc < 30:
 print('Você esta com sobrepeso!')
elif 30 <= imc < 40:
    print('Você esta com obesidade!')
elif imc >= 40:
    print('Você esta com \033[31mobesidade morbida!')
print(f'imc é igual a: {imc:.2f}')
