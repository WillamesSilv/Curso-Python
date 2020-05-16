import random
n = s = c = 0
print('='*20)
print('JOGO DO PAR OU IMPAR')
print('='*20)
while True:
    n = int(input('Digite um número: '))
    r = str(input('Você quer par ou impar? [P/I] ')).upper().strip()[0]
    c = random.randint(1, 10)
    s = n + c

