numero = int(input('Digite um número: '))
cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[33mO número {} foi divisível {} vezes.'.format(numero, cont))
if cont == 2:
    print('Isso prova que o número {} é PRIMO!'.format(numero))
else:
    print('Isso prova que o número {} NÃO É PRIMO!'.format(numero))
