from random import randint
from time import sleep
cont = 0
novopalpite = 0
computador = randint(0, 10)
print('De 0 á 10, tente adivinhar em qual número estou pensando.')
print(computador)
sleep(5)
usuario = int(input('Qual é o número que pensei? '))
while usuario != computador:
    usuario = int(input('ERROU! Continue tentando: '))
    cont += 1
if usuario == computador:
    print('PARABÉNS VOCÊ CONSEGUIU ACERTAR!')
print('Você usou {} tentativas.'.format(cont))
