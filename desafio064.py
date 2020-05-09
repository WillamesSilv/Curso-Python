n = cont = soma = 0 #todas as atribuições em uma linha.
n = int(input('Digite um número [999 código de parada]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 código de parada]: '))
print('Você digitou {} números e a soma destes é {}.'.format(cont, soma))
