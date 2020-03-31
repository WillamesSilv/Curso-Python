print('+' * 20)
print(' ' * 3, '\033[33mVamos somar!\033[m')
print('+' * 20)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('\033[1;35mA soma entre {} e {} vale {}'.format(n1, n2, s))
