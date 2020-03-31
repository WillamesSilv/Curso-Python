from time import sleep
n = int(input('\033[33mOlá, digite um número:\033[m '))
print('\033[1;30;42mPROCESSANDO...\033[m')
sleep(2)
d = n*2
t = n*3
r = n**(1/2)
print('Considerando o valor \033[1;35m{}\033[m, o seu dobro é \033[1;32m{}\033[m, o triplo é \033[1;34m{}\033[m e '.format(n, d, t), end='')
print('a raiz quadrada é \033[1;31m{:.2f}\033[m.'.format(r))
