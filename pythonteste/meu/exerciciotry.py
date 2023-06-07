n = int(input('Digite um numero: '))
ft = soma =1
while soma <= n:

    ft = ft * soma
    #   1 = 1 * 1
    #   2 = 1 * 2
    #   6 = 2 * 3
    #  24 = 6 * 4
    # 120 = 24 * 5
    soma += 1
    print(ft)
