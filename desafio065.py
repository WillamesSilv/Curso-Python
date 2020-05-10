n = soma = cont = med = maior = menor =0
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    soma += n
    med = soma / cont
print('Você digitou {} números, a soma entre eles é {}.\nA média é {:.1f}.'.format(cont, soma, med))
print('O {} é o MAIOR. O {} é o MENOR.'.format(maior, menor))
