from emoji import emojize
from time import sleep
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print(emojize(':fireworks::fireworks::fireworks:\033[31mPOW. FELIZ ANO NOVO\033[m:fireworks::fireworks::fireworks:',language = 'alias'))