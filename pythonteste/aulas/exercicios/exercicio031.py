d = float(input('Qual a distancia da viagem em km?: '))
if d <=200:
    print(f'Sua viagem ficara no valor total de: {d*0.5:.2f}$')
else:
    print(f'Como você vai para bem longe, te daremos um desconto. AO total sua viagem ficara de: {d*0.45}$')