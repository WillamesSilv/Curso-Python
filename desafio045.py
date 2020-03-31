from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('*' * 40)
print('{:^40}'.format('JOKENPÔ'))
print('*' * 40)
usuario = int(input('''Vamos jogar JOKENPÔ? faça sua escolha:
[0]-PEDRA
[1]-PAPEL
[2]-TESOURA
Já escolheu? Qual foi sua opção? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 21)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[usuario]))
print('-=' * 21)
if computador == 0:# computador escolheu pedra
   if usuario == 0:
     print('EMPATE')
   elif usuario == 1:
       print('JOGADOR VENCEU!')
   elif usuario == 2:
       print('COMPUTADOR VENCEU!')
   else:
       print('OPÇÃO INVÁLIDA!')
elif computador == 1:#computador escolheu papel
    if usuario == 0:
      print('COMPUTADOR VENCEU!')
    elif usuario == 1:
      print('EMPATE')
    elif usuario == 2:
        print('JOGADOR VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA!')
elif computador == 2:#computador escolheu tesoura
    if usuario == 0:
      print('JOGADOR VENCEU!')
    elif usuario == 1:
      print('COMPUTADOR VENCEU!')
    elif usuario == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA!')
