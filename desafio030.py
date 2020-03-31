numero = int(input('\033[1;36mDigite um número: '))
resultado = numero % 2
if resultado == 0:
    print('\033[1;32mO número {} é PAR'.format(numero))
else:
    print('\033[1;33mO número {} é ÍMPAR'.format(numero))