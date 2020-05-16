import random
n = s = c = v = 0
print('='*20)
print('JOGO DO PAR OU IMPAR')
print('='*20)
while True:
    n = int(input('Digite um número: '))
    c = random.randint(0, 10)
    s = n + c
    r = ' '
    while r not in 'PI':
        r = str(input('Você quer par ou impar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador {c}, total de {s}.')
    if r == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você  PERDEU!')
            break
    elif r == 'I':
        if s % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
        print('='*20)
        print('Vamos mais uma vez! Digite um número: ')
print('='*20)
print(f'GAME OVER =( !! Você venceu {v} vezes.')

