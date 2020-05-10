n = soma = cont = 0
n = int(input('digite um número: '))
r = str(input('Quer continuar? [S/N]: ')).upper()
while r != 'N':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    cont += 1
    soma += n
    med = soma / cont
print('Você digitou {} números, a soma entre eles é {}.\nA média é {:.1f}.'.format(cont, soma, med))
