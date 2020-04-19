'''from math import factorial
numero = int(input('Digite um número para saber seu fatorial: '))
f = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, f))'''
n = int(input('Digite um número: '))
c = n
f = 1 # quando somamos o valor é 0, mas quando é multiplicação o valor é 1.
print('Calculando o {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')#Depois do = ja poderia colocar a importação do factorial
    f *= c
    c -= 1
print('{}.'.format(f))
