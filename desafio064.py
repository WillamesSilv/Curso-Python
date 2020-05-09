n = 1
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 código de parada]: '))
    cont += 1
    soma += n
print('Você digitou {} números e a soma destes é {}.'.format(cont - 1, soma - 999))
