from random import randint
randint
n = randint(0, 5) # o computardor pensa em um número de 0 a 5
print('\033[33m-=-' * 20)
print('\033[1;35mVou pensar em um número de 0 a 5, tente adivinhar!')
print('\033[33m-=-\033[m' * 20)
nu = int(input('\033[34mEm qual número pensei? '))#jogador tenta adivinhar
if nu == n:
    print('\033[4;30mPARABÉNS!! Você acertou!\033[m')
else:
    print('\033[mVocê ERROU! Eu pensei no número \033[4;1;36m{}\033[m e não no número \033[4;1;31m{}'.format(n, nu))