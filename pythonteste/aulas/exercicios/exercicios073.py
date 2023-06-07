
tabelabr = 'Palmeiras - SP', 'Internacional - RS', 'Fluminense - RJ', 'Corinthians - SP', 'Flamengo - RJ', 'Athletico ' \
                                                                                                           'Paranaense - ' \
                                                                                                           'PR', \
    'Atlético Mineiro - MG', 'Fortaleza - CE', 'São Paulo - SP', ' América Fc Saf - MG', \
    ' Botafogo - RJ', 'Santos - SP', 'Goiás - GO', 'Red Bull Bragantino - SP', 'Coritiba - PR', \
    'Cuiabá Saf - MT', 'Ceará - CE', 'Atlético - GO', ' Avaí - SC', 'Juventude - RS'





print('\033[3;36m{:*^150}\033[36m'.format('\033[33mBrasileirão\033[36m'))
print('\033[35m')
print('-='*67)
print(f'Os 5 primeiros colocados são:{tabelabr[0:6]}')
print('-='*67)
print(f'Os 4 ultimos colocados são:{tabelabr[-5:]}')
print('-='*67)
print(f'Os times em ordem alfabeticas são:{sorted(tabelabr)}')
print('-='*67)
print(f'O Corinthians - SP terminou em {tabelabr.index("Corinthians - SP") +1  }° colocado do brasileirão serie A de 2022')
print('-='*67)

print('\n\033[3;36m{:*^150}\033[36m'.format('\033[33mBrasileirão\033[36m'))