n = 1
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
print('Você digitou {} números e a soma destes é {} desconsiderando o 999.'.format(cont, soma - 999))
