from random import randint
from time import sleep
rank = {}
jogadores ={}
count = 1
maior =  menor =0
for c in range(1,5):
   jogadores[f'jogador[ {c} ] '] = randint(0,20)
print('=='*30)
print(f'{"No dado":^60}')
print('=='*30)

for k,v in jogadores.items():

    print(f'                  O {k}Tirou {v}')
    sleep(0.8)

rank = sorted(jogadores.items(),key=lambda item: item[1],reverse=True)



print('=='*30)
print('               \033[33m_-==RANKING DOS JOGADORES==-_\033[m')
for i,v in enumerate(rank):
    print(f'               {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.8)
print('=='*30)


