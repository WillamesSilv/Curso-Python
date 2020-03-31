# Regra pra formação do triangulo: Cada um  dos segmentos tem que ser menor
# do que a soma do comprimento dos outros.
from time import sleep
print('\033[32m-=- ' * 11)
print(' ' * 7, '\033[1;33mAnalisador de TRIÂNGULOS')
print('\033[32m-=- \033[m' * 11)
sleep(2)
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[1;34mAs retas acima podem formar um triângulo')
else:
    print('\033[1;31mAs retas acima não podem formar um triângulo')
