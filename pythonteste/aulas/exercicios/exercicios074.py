from random import randint

nums = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),\
    randint(0,10),randint(0,10),randint(0,10),
print('Os valores sorteados foram: ',end='')
for c in nums:
    print(f'{c} ',end=' ')
print(f'\nO menor valor digitado foi: {max(nums)}')
print(f'O maior valor digitado foi: {min(nums)}')