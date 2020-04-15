from random import randint
from time import sleep
cont = 0
novopalpite = 0
computador = randint(0, 10)
print('De 0 á 10, tente adivinhar em qual número estou pensando.')
sleep(3)
usuario = int(input('Qual é o número que pensei? '))
while usuario != computador:
    usuario = int(input('ERROU! Continue tentando: '))
    cont += 1
if usuario == computador:
    print('PARABÉNS VOCÊ CONSEGUIU ACERTAR!')
print('Você usou {} tentativas.'.format(cont + 1))
'''programa do guanabara
acertou = false
palpites = 0
while not acertou:
    jogador = int(input(Qual pe o se palpite? ))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(Mais... Tente mias uma vez.)
        elif jogador > computador:
            print(Menos... Tente mais uma vez.)
print(Acertou com {} tentativas. Parabéns!.format(palpites)) '''