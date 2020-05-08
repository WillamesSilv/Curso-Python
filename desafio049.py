from time import sleep
tabuada = int(input('Digite um número para ver a sua tabuada: '))
print('=-=' * 5)
for c in range(0, 11):
    sleep(1)
    print('\033[32m{} x {:2} = {}'.format(tabuada, c, tabuada * c))
print('\033[m=-=' * 5)
