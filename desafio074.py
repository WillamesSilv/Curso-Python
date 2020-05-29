from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('\033[35mOs valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\n\033[33mO maior valor sorteado foi: {max(numeros)}')
print(f'\033[31mO menor valor sorteado foi: {min(numeros)}')
